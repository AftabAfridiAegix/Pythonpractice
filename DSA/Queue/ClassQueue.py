patients = []

def add_patient():
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    disease = input("Enter disease: ")

    patient = {
        "name": name,
        "age": age,
        "disease": disease
    }

    patients.append(patient)
    print("Patient added successfully.")

def treat_patient():
    if len(patients) == 0:
        print("No patients waiting.")
    else:
        patient = patients.pop(0)
        print("Now treating:", patient["name"])
        print("Age:", patient["age"])
        print("Disease:", patient["disease"])

def show_patients():
    if not patients:
        print("No patients in queue.")
    else:
        print("\nWaiting Patients:")
        for patient in patients:
            print(patient["name"], patient["age"], patient["disease"])

def search_patient():
    name = input("Enter patient name: ")
    found = False

    for patient in patients:
        if patient["name"].lower() == name.lower():
            print("Patient found.")
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Disease:", patient["disease"])
            found = True

    if not found:
        print("Patient not found.")

while True:
    print("\n--- Hospital Queue ---")
    print("1. Add Patient")
    print("2. Treat Patient")
    print("3. Show Patients")
    print("4. Search Patient")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        treat_patient()

    elif choice == "3":
        show_patients()

    elif choice == "4":
        search_patient()

    elif choice == "5":
        print("Hospital system closed.")
        break

    else:
        print("Invalid choice.")