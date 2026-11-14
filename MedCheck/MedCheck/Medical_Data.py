class MedicalData:
    def __init__(self):

       self.conditions = {
           "Common cold" : ["cough", "sore throat", "runny nose"],
           "Flu": ["fever", "cough", "fatigue", "body pain"],
           "Migrane": ["headache", "nausea", "sensitivity to light"],
           "Stomach Infection" : ["stomach pain", "vomiting", "diarrhea"]
    }
    def get_conditions(self):
        return self.conditions