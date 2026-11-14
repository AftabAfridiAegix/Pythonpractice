
import os
import json


class RecordManager:
    def __init__(self):
        self.filename = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "records.json"
        )

    def save_record(self, patient_data):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            try:
                with open(self.filename, "r") as file:
                    records = json.load(file)
            except json.JSONDecodeError:
                records = []
        else:
            records = []

        records.append(patient_data)

        with open(self.filename, "w") as file:
            json.dump(records, file, indent=4)

    def view_records(self):
        if not os.path.exists(self.filename):
            return []

        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []