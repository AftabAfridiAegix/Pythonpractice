
from Patient import Patient
from Medical_Data import MedicalData
from Symptom_checker import SymptomChecker
from Record_manager import RecordManager

medical_data = MedicalData()
checker = SymptomChecker(medical_data.get_conditions())

record_manager = RecordManager()

while True:
    print("\n**********************************")
    print("      MEDCHECK - SYMPTOMS CHECKER")
    print("____________________________________")
    print("1. Check Symptoms")
    print("2. View Patient Records")
    print("3. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        name = input("Enter patient name: ").strip().title()

        try:
            age = int(input("Enter patient age: "))
            if age <= 0:
                print("Age must be greater than zero.")
                continue
        except ValueError:
            print("Please enter a valid age.")
            continue

        symptoms_input = input(
            "Enter symptoms separated by comma: "
        )

        symptoms = [
            symptom.strip().lower()
            for symptom in symptoms_input.split(",")
            if symptom.strip()
        ]

        if not symptoms:
            print("Please enter at least one symptom.")
            continue

        patient = Patient(name, age, symptoms)
        results = checker.check_symptoms(symptoms)

        print("\n**__**__** RESULT **__**__**")
        patient.show_patient()

        if results:
            print("\nPossible conditions:")

            for condition, matches in results.items():
                print(
                    condition,
                    "->",
                    matches,
                    "matching symptom(s)"
                )
        else:
            print("No matching condition found.")

        patient_dictionary = {
            "name": patient.name,
            "age": patient.age,
            "symptoms": patient.symptoms
        }

        record_manager.save_record(patient_dictionary)

        print("\nPatient record saved successfully.")

    elif choice == "2":
        records = record_manager.view_records()

        print("\n__________ PATIENT RECORDS __________")

        if records:
            for record in records:
                print("\nName:", record["name"])
                print("Age:", record["age"])
                print("Symptoms:", ", ".join(record["symptoms"]))
        else:
            print("No records found.")

    elif choice == "3":
        print("Thank you for using MedCheck.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")