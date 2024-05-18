class Patient:
    def __init__(self):
        self.patient_info = {}
        self.medical_history = {}

    def add_medical_history(self, key,value):
        self.medical_history[key] = value

    def add_patient_info(self, key, value):
        self.patient_info[key] = value

    def mostrar(self):
        print(self.patient_info)
        print(self.medical_history)
