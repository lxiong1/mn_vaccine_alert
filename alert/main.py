import schedule
import time
from icecream import ic
from client.AppointmentDataClient import AppointmentDataClient
from service.AppointmentService import AppointmentService
from service.AlertService import AlertService


def main():
    appointment_service = AppointmentService(AppointmentDataClient())
    available_appointments = appointment_service.get_available_appointments()
    alert_service = AlertService(available_appointments)

    alert_service.send_text_alert()


if __name__ == "__main__":
    seconds = 30
    schedule.every(seconds).seconds.do(main)

    while True:
        schedule.run_pending()
        ic(f"Waiting {seconds} seconds for next run")
        time.sleep(seconds)
