import pgeocode
import sys
import traceback
from icecream import ic
from domain.model.Appointment import Appointment


class AppointmentService:
    def __init__(self, appointment_data_client):
        self._appointment_data_client = appointment_data_client
        self._mn_vaccine_appointments = (
            self._appointment_data_client.get_mn_vaccine_appointments()
        )
        self._50_mile_radius_postal_codes = self.__get_50_mile_radius_postal_codes()

    def get_available_appointments(self):
        available_appointments = []

        try:
            for appointment in self._mn_vaccine_appointments:
                appointment_props = appointment["properties"]
                postal_code = appointment_props["postal_code"]

                if (
                    postal_code in self._50_mile_radius_postal_codes
                    and appointment_props["carries_vaccine"]
                    and appointment_props["appointments_available"] == True
                ):
                    available_vaccine_appointment = Appointment(
                        provider=appointment_props["provider_brand"],
                        url=appointment_props["url"],
                        location=f"{appointment_props['address']}, {appointment_props['city']}, {appointment_props['state']} {postal_code}",
                        vaccine_types=appointment_props["appointment_vaccine_types"],
                    )

                    available_appointments.append(
                        available_vaccine_appointment.__dict__
                    )

            return available_appointments
        except:
            ic(traceback.print_exc())
            sys.exit()

    def __get_50_mile_radius_postal_codes(self):
        postal_codes = []

        for appointment in self._mn_vaccine_appointments:
            postal_code = appointment["properties"]["postal_code"]
            if postal_code:
                postal_codes.append(postal_code)

        distance = pgeocode.GeoDistance("us")
        km_to_mile_conversion_factor = 0.621371
        valid_postal_codes = []

        for postal_code in postal_codes:
            miles = (
                distance.query_postal_code("55414", postal_code)
                * km_to_mile_conversion_factor
            )
            if miles <= 50:
                valid_postal_codes.append(postal_code)

        return valid_postal_codes
