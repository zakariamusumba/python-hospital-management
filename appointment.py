from datetime import datetime, timedelta


class Appointment:

    DURATION_MINUTES = 30

    def __init__(self, appointment_id, patient, doctor, date, time):

        self.appointment_id = str(appointment_id)

        self.patient = patient
        self.doctor = doctor

        try:

            self.date_time = datetime.strptime(
                f"{date} {time}",
                "%Y-%m-%d %H:%M"
            )

        except ValueError:

            raise ValueError(
                "Invalid date or time. Use YYYY-MM-DD and HH:MM."
            )

        if self.date_time <= datetime.now():
            raise ValueError("Appointment must be scheduled in the future.")

        self.date = date
        self.time = time

        self.status = "Booked"

    def display_appointment(self):

        print("\n===== APPOINTMENT DETAILS =====")

        print(f"Appointment ID: {self.appointment_id}")

        print(f"Patient: {self.patient.name}")

        print(f"Patient ID: {self.patient.patient_id}")

        print(f"Doctor: {self.doctor.name}")

        print(f"Specialization: {self.doctor.specialization}")

        print(f"Date: {self.date}")

        print(f"Time: {self.time}")

        print(f"Status: {self.status}")

    def cancel_appointment(self):

        if self.status == "Cancelled":
            raise ValueError("Appointment is already cancelled.")

        self.status = "Cancelled"

        print("Appointment cancelled successfully!")

    def to_dictionary(self):

        return {
            "appointment_id": self.appointment_id,
            "patient_id": self.patient.patient_id,
            "doctor_id": self.doctor.doctor_id,
            "date": self.date,
            "time": self.time,
            "status": self.status
        }

self.patient = patient
self.doctor = doctor

datetime.strptime(
    f"{date} {time}",
    "%Y-%m-%d %H:%M"
)

self.status = "Cancelled"

