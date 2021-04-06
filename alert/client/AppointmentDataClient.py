import requests
import sys
import traceback
from icecream import ic

ic.configureOutput(includeContext=True)


class AppointmentDataClient:
    def get_mn_vaccine_appointments(self):
        ic("Retrieving available MN vaccine appointments")

        try:
            response = requests.get(
                url="https://www.vaccinespotter.org/api/v0/states/MN.json"
            )

            if response.status_code == 200:
                ic("Sucessfully retrieved available MN vaccine appointments")
                return response.json()["features"]
            else:
                return None
        except:
            ic(traceback.print_exc())
            sys.exit()
