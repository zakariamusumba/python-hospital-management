class Doctor:

    def __init__(self, doctor_id, name, specialization, availability):

        if not doctor_id:
            raise ValueError("Doctor ID cannot be empty.")

        if not name:
            raise ValueError("Doctor name cannot be empty.")

        if not specialization:
            raise ValueError("Specialization cannot be empty.")

        if not availability:
            raise ValueError("Availability cannot be empty.")

        self.doctor_id = str(doctor_id)
        self.name = name
        self.specialization = specialization
        self.availability = availability

    def display_doctor(self):

        print("\n===== DOCTOR DETAILS =====")

        print(f"Doctor ID: {self.doctor_id}")
        print(f"Name: {self.name}")
        print(f"Specialization: {self.specialization}")
        print(f"Availability: {self.availability}")

    def to_dictionary(self):

        return {
            "doctor_id": self.doctor_id,
            "name": self.name,
            "specialization": self.specialization,
            "availability": self.availability
        }

doctor1 = Doctor(
    "D001",
    "Dr. James",
    "Cardiology",
    "Monday-Friday, 09:00-17:00"
)

