class Patient:

    def __init__(self, patient_id, name, age, gender, contact):

        if not patient_id:
            raise ValueError("Patient ID cannot be empty.")

        if not name:
            raise ValueError("Patient name cannot be empty.")

        if not isinstance(age, int) or isinstance(age, bool) or age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")

        if not contact:
            raise ValueError("Contact number cannot be empty.")

        self.patient_id = str(patient_id)
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact

    def display_patient(self):

        print("\n===== PATIENT DETAILS =====")

        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Contact: {self.contact}")

    def to_dictionary(self):

        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "contact": self.contact
        }

