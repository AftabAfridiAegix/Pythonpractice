class SymptomChecker:
    def __init__(self, conditions):
        self.conditions = conditions

    def check_symptoms(self, symptoms):
        results = {}

        for condition, condition_symptoms in self.conditions.items():

            matches = 0 
            for symptom in symptoms:
                if symptom in condition_symptoms:
                    matches +=1

            if matches > 0:
                results[condition] = matches

        return results

