import json

from patient import Patient
from doctor import Doctor
from appointment import Appointment


class Hospital:

    def __init__(self):

        self.patients = {}

        self.doctors = {}

        self.appointments = {}

    # ==================================
    # REGISTER PATIENT
    # ==================================

    def register_patient(self, patient_id, name, age, gender, contact):

        patient_id = str(patient_id)

        if patient_id in self.patients:
            raise ValueError("Patient ID already exists!")

        patient = Patient(
            patient_id,
            name,
            age,
            gender,
            contact
        )

        self.patients[patient_id] = patient

        print("Patient registered successfully!")

        return patient

    # ==================================
    # REGISTER DOCTOR
    # ==================================

    def register_doctor(self, doctor_id, name, specialization, availability):

        doctor_id = str(doctor_id)

        if doctor_id in self.doctors:
            raise ValueError("Doctor ID already exists!")

        doctor = Doctor(
            doctor_id,
            name,
            specialization,
            availability
        )

        self.doctors[doctor_id] = doctor

        print("Doctor registered successfully!")

        return doctor

    # ==================================
    # SEARCH PATIENT
    # ==================================

    def search_patient(self, patient_id):

        patient_id = str(patient_id)

        if patient_id not in self.patients:
            raise ValueError("Patient not found!")

        patient = self.patients[patient_id]

        patient.display_patient()

        return patient

    # ==================================
    # DISPLAY ALL PATIENTS
    # ==================================

    def display_patients(self):

        if not self.patients:
            print("No patients registered.")
            return

        for patient in self.patients.values():

            patient.display_patient()

    # ==================================
    # DISPLAY ALL DOCTORS
    # ==================================

    def display_doctors(self):

        if not self.doctors:
            print("No doctors registered.")
            return

        for doctor in self.doctors.values():

            doctor.display_doctor()

    # ==================================
    # BOOK APPOINTMENT
    # ==================================

    def book_appointment(
        self,
        appointment_id,
        patient_id,
        doctor_id,
        date,
        time
    ):

        appointment_id = str(appointment_id)

        patient_id = str(patient_id)

        doctor_id = str(doctor_id)

        # Check appointment ID
        if appointment_id in self.appointments:
            raise ValueError("Appointment ID already exists!")

        # Check patient
        if patient_id not in self.patients:
            raise ValueError("Patient does not exist!")

        # Check doctor
        if doctor_id not in self.doctors:
            raise ValueError("Doctor does not exist!")

        patient = self.patients[patient_id]

        doctor = self.doctors[doctor_id]

        # Create appointment object
        appointment = Appointment(
            appointment_id,
            patient,
            doctor,
            date,
            time
        )

        # Check overlapping appointments
        new_start = appointment.date_time

        new_end = new_start + Appointment.__dict__.get(
            "DURATION_MINUTES", 30
        ) * __import__("datetime").timedelta(minutes=1)

        for existing in self.appointments.values():

            if existing.doctor.doctor_id == doctor_id:

                if existing.status == "Booked":

                    old_start = existing.date_time

                    old_end = old_start + __import__("datetime").timedelta(
                        minutes=Appointment.DURATION_MINUTES
                    )

                    # Check whether appointments overlap
                    if new_start < old_end and old_start < new_end:

                        raise ValueError(
                            "Doctor already has an appointment "
                            "during this time!"
                        )

            # Prevent a patient from booking two overlapping appointments
            if existing.patient.patient_id == patient_id:

                if existing.status == "Booked":

                    old_start = existing.date_time

                    old_end = old_start + __import__("datetime").timedelta(
                        minutes=Appointment.DURATION_MINUTES
                    )

                    if new_start < old_end and old_start < new_end:

                        raise ValueError(
                            "Patient already has another appointment "
                            "during this time!"
                        )

        self.appointments[appointment_id] = appointment

        print("Appointment booked successfully!")

        return appointment

    # ==================================
    # CANCEL APPOINTMENT
    # ==================================

    def cancel_appointment(self, appointment_id):

        appointment_id = str(appointment_id)

        if appointment_id not in self.appointments:
            raise ValueError("Appointment not found!")

        appointment = self.appointments[appointment_id]

        appointment.cancel_appointment()

    # ==================================
    # PATIENT APPOINTMENT HISTORY
    # ==================================

    def patient_history(self, patient_id):

        patient_id = str(patient_id)

        if patient_id not in self.patients:
            raise ValueError("Patient not found!")

        print("\n===== PATIENT APPOINTMENT HISTORY =====")

        found = False

        for appointment in self.appointments.values():

            if appointment.patient.patient_id == patient_id:

                appointment.display_appointment()

                found = True

        if not found:
            print("No appointment history found.")

    # ==================================
    # DISPLAY APPOINTMENTS BY DATE
    # ==================================

    def appointments_by_date(self, selected_date):

        print(f"\n===== APPOINTMENTS FOR {selected_date} =====")

        found = False

        for appointment in self.appointments.values():

            if appointment.date == selected_date:

                appointment.display_appointment()

                found = True

        if not found:
            print("No appointments found for this date.")

    # ==================================
    # DISPLAY APPOINTMENTS BY DOCTOR
    # ==================================

    def appointments_by_doctor(self, doctor_id):

        doctor_id = str(doctor_id)

        if doctor_id not in self.doctors:
            raise ValueError("Doctor not found!")

        print("\n===== DOCTOR APPOINTMENTS =====")

        found = False

        for appointment in self.appointments.values():

            if appointment.doctor.doctor_id == doctor_id:

                appointment.display_appointment()

                found = True

        if not found:
            print("No appointments found for this doctor.")

    # ==================================
    # DAILY REPORT GROUPED BY DOCTOR
    # ==================================

    def daily_report(self, selected_date):

        print("\n===== DAILY HOSPITAL REPORT =====")

        print(f"Date: {selected_date}")

        report = {}

        for appointment in self.appointments.values():

            if (
                appointment.date == selected_date
                and appointment.status == "Booked"
            ):

                doctor_name = appointment.doctor.name

                if doctor_name not in report:
                    report[doctor_name] = []

                report[doctor_name].append(appointment)

        if not report:

            print("No appointments scheduled.")

            return

        for doctor_name, appointments in report.items():

            print(f"\nDoctor: {doctor_name}")

            print("-------------------------")

            for appointment in appointments:

                print(
                    f"Time: {appointment.time} | "
                    f"Patient: {appointment.patient.name} | "
                    f"Status: {appointment.status}"
                )

            print(
                f"Total Appointments: {len(appointments)}"
            )

    # ==================================
    # SAVE ALL RECORDS
    # ==================================

    def save_records(self):

        patients_data = []

        doctors_data = []

        appointments_data = []

        for patient in self.patients.values():

            patients_data.append(patient.to_dictionary())

        for doctor in self.doctors.values():

            doctors_data.append(doctor.to_dictionary())

        for appointment in self.appointments.values():

            appointments_data.append(
                appointment.to_dictionary()
            )

        with open("patients.json", "w") as file:

            json.dump(patients_data, file, indent=4)

        with open("doctors.json", "w") as file:

            json.dump(doctors_data, file, indent=4)

        with open("appointments.json", "w") as file:

            json.dump(appointments_data, file, indent=4)

        print("All hospital records saved successfully!")

    # ==================================
    # LOAD ALL RECORDS
    # ==================================

    def load_records(self):

        try:

            with open("patients.json", "r") as file:

                patients_data = json.load(file)

            with open("doctors.json", "r") as file:

                doctors_data = json.load(file)

            with open("appointments.json", "r") as file:

                appointments_data = json.load(file)

            # Restore patients
            for item in patients_data:

                patient = Patient(
                    item["patient_id"],
                    item["name"],
                    item["age"],
                    item["gender"],
                    item["contact"]
                )

                self.patients[patient.patient_id] = patient

            # Restore doctors
            for item in doctors_data:

                doctor = Doctor(
                    item["doctor_id"],
                    item["name"],
                    item["specialization"],
                    item["availability"]
                )

                self.doctors[doctor.doctor_id] = doctor

            # Restore appointments
            for item in appointments_data:

                patient_id = item["patient_id"]

                doctor_id = item["doctor_id"]

                if (
                    patient_id not in self.patients
                    or doctor_id not in self.doctors
                ):

                    raise ValueError(
                        "Appointment refers to a missing patient or doctor."
                    )

                appointment = Appointment(
                    item["appointment_id"],
                    self.patients[patient_id],
                    self.doctors[doctor_id],
                    item["date"],
                    item["time"]
                )

                appointment.status = item["status"]

                self.appointments[appointment.appointment_id] = appointment

            print("Hospital records loaded successfully!")

        except FileNotFoundError:

            print("Some hospital files were not found. Starting with available records.")

        except json.JSONDecodeError:

            print("Error: One of the JSON files contains invalid data.")

