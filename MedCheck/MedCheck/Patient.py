class Patient:

    def __init__(self, name, age, symptoms):
          self.name = name
          self.age = age
          self.symptoms = symptoms


    def show_patient(self):
         print("Patient Name:", self.name)
         print("Age:", self.age)
         print("Symptoms:", ", ".join(self.symptoms))