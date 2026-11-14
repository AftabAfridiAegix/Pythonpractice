
import pandas as pd
from pathlib import Path


class MedicalData:
    def __init__(self):
        self.file = Path(__file__).with_name("patients.csv")
        self.columns = ["ID", "Name", "Age", "Disease"]
        self.df = pd.DataFrame(columns=self.columns)
        self.load_data()

    def load_data(self):
        if not self.file.exists() or self.file.stat().st_size == 0:
            self.df = pd.DataFrame(columns=self.columns)
            self.save_data()
            return
        try:
            data = pd.read_csv(self.file, dtype={"ID": str})
        except pd.errors.EmptyDataError:
            self.df = pd.DataFrame(columns=self.columns)
            self.save_data()
            return

        data.columns = data.columns.str.strip()
        if list(data.columns) != self.columns:
            raise ValueError(
                "patients.csv must contain: ID, Name, Age, Disease"
            )
        for column in self.columns:
            data[column] = data[column].fillna("")

        data["ID"] = data["ID"].astype(str).str.strip()
        data["Name"] = data["Name"].astype(str).str.strip()
        data["Disease"] = data["Disease"].astype(str).str.strip()

        self.df = data

    def add_patient(self, patient_id, name, age, disease):
        patient_id = str(patient_id).strip()
        name = str(name).strip()
        disease = str(disease).strip()
        if not all([patient_id, name, disease]):
            raise ValueError("Please fill in all fields.")
        try:
            age = int(age)
        except (ValueError, TypeError):
            raise ValueError("Age must be a whole number.")

        if not 1 <= age <= 130:
            raise ValueError("Age must be between 1 and 130.")

        existing_ids = self.df["ID"].astype(str).str.strip()

        if existing_ids.str.casefold().eq(patient_id.casefold()).any():
            raise ValueError("This patient ID already exists.")

        new_patient = pd.DataFrame(
            [[patient_id, name, age, disease]],
            columns=self.columns
        )

        updated_data = pd.concat(
            [self.df, new_patient],
            ignore_index=True
        )

        updated_data.to_csv(self.file, index=False)
        self.df = updated_data

    def save_data(self):
        self.df.to_csv(self.file, index=False)
