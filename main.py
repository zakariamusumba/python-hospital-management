from hospital import Hospital

hospital = Hospital()
hospital.load_records()

def main():

    while True:

        print("\n========== HOSPITAL MANAGEMENT SYSTEM ==========")

        print("1. Register Patient")
        print("2. Register Doctor")
        print("3. Book Appointment")
        print("4. Search Patient")
        print("5. Display All Patients")
        print("6. Display All Doctors")
        print("7. View Patient Appointment History")
        print("8. Cancel Appointment")
        print("9. Display Appointments by Date")
        print("10. Display Appointments by Doctor")
        print("11. Generate Daily Report")
        print("12. Save Records")
        print("13. Save and Exit")

        choice = input("\nEnter your choice: ")

        try:

            if choice == "1":

                patient_id = input("Enter Patient ID: ")

                name = input("Enter Patient Name: ")

                age = int(input("Enter Patient Age: "))

                gender = input("Enter Patient Gender: ")

                contact = input("Enter Contact Number: ")

                hospital.register_patient(
                    patient_id,
                    name,
                    age,
                    gender,
                    contact
                )

            elif choice == "2":

                doctor_id = input("Enter Doctor ID: ")

                name = input("Enter Doctor Name: ")

                specialization = input(
                    "Enter Specialization: "
                )

                availability = input(
                    "Enter Doctor Availability: "
                )

                hospital.register_doctor(
                    doctor_id,
                    name,
                    specialization,
                    availability
                )

            # ==================================
            # BOOK APPOINTMENT
            # ==================================

            elif choice == "3":

                appointment_id = input(
                    "Enter Appointment ID: "
                )

                patient_id = input(
                    "Enter Patient ID: "
                )

                doctor_id = input(
                    "Enter Doctor ID: "
                )

                date = input(
                    "Enter Appointment Date (YYYY-MM-DD): "
                )

                time = input(
                    "Enter Appointment Time (HH:MM): "
                )

                hospital.book_appointment(
                    appointment_id,
                    patient_id,
                    doctor_id,
                    date,
                    time
                )

            # ==================================
            # SEARCH PATIENT
            # ==================================

            elif choice == "4":

                patient_id = input(
                    "Enter Patient ID: "
                )

                hospital.search_patient(patient_id)

            # ==================================
            # DISPLAY ALL PATIENTS
            # ==================================

            elif choice == "5":

                hospital.display_patients()

            # ==================================
            # DISPLAY ALL DOCTORS
            # ==================================

            elif choice == "6":

                hospital.display_doctors()

            # ==================================
            # PATIENT APPOINTMENT HISTORY
            # ==================================

            elif choice == "7":

                patient_id = input(
                    "Enter Patient ID: "
                )

                hospital.patient_history(patient_id)

            # ==================================
            # CANCEL APPOINTMENT
            # ==================================

            elif choice == "8":

                appointment_id = input(
                    "Enter Appointment ID: "
                )

                hospital.cancel_appointment(
                    appointment_id
                )

            # ==================================
            # APPOINTMENTS BY DATE
            # ==================================

            elif choice == "9":

                selected_date = input(
                    "Enter Date (YYYY-MM-DD): "
                )

                hospital.appointments_by_date(
                    selected_date
                )

            # ==================================
            # APPOINTMENTS BY DOCTOR
            # ==================================

            elif choice == "10":

                doctor_id = input(
                    "Enter Doctor ID: "
                )

                hospital.appointments_by_doctor(
                    doctor_id
                )

            # ==================================
            # DAILY REPORT
            # ==================================

            elif choice == "11":

                selected_date = input(
                    "Enter Report Date (YYYY-MM-DD): "
                )

                hospital.daily_report(
                    selected_date
                )

            # ==================================
            # SAVE RECORDS
            # ==================================

            elif choice == "12":

                hospital.save_records()

            # ==================================
            # SAVE AND EXIT
            # ==================================

            elif choice == "13":

                hospital.save_records()

                print(
                    "\nThank you for using "
                    "the Hospital Management System!"
                )

                break

            else:

                print("Invalid choice. Please try again.")

        except (ValueError, KeyError) as error:

            print(f"\nError: {error}")

        except Exception as error:

            print(f"\nUnexpected error: {error}")


if __name__ == "__main__":

    main()