import assistant
from patient import Patient

class MedicalAssistant:
    def __init__(self):
        self.patient = Patient()

    def ask_patient_info(self):
        self.patient.add_patient_info("nombre", assistant.listen_with_retry("¡Bienvenido! Por favor, dime tu nombre."))
        self.patient.add_patient_info("edad", assistant.listen_with_retry("¿Cuál es tu edad?"))

    def ask_medical_history(self):
        self.patient.add_medical_history("historial", assistant.listen_with_retry("¿Tienes algún historial médico relevante? Por favor, descríbelo."))
        self.patient.add_medical_history("condiciones_preexistentes", assistant.listen_with_retry("¿Tienes alguna condición médica preexistente?"))
        self.patient.add_medical_history("medicamentos", assistant.listen_with_retry("¿Estás tomando algún medicamento actualmente?"))
        self.patient.add_medical_history("cirugias", assistant.listen_with_retry("¿Has tenido alguna cirugía en el pasado? Si es así, ¿cuándo y por qué?"))

    def ask_symptoms(self):
        self.patient.add_medical_history("sintomas", assistant.listen_with_retry("¿Cuáles son tus síntomas actuales?"))
        self.patient.add_medical_history("comienzo_sintomas", assistant.listen_with_retry("¿Cuándo comenzaron tus síntomas?"))
        self.patient.add_medical_history("frecuencia_sintomas", assistant.listen_with_retry("¿Con qué frecuencia experimentas estos síntomas?"))
        self.patient.add_medical_history("factores_desencadenantes", assistant.listen_with_retry("¿Hay algo que mejore o empeore tus síntomas?"))

    def ask_lifestyle_habits(self):
        self.patient.add_medical_history("habitos", assistant.listen_with_retry("¿Fumas o consumes alcohol? Si es así, ¿con qué frecuencia?"))
        self.patient.add_medical_history("ejercicio", assistant.listen_with_retry("¿Haces ejercicio regularmente? ¿Qué tipo y con qué frecuencia?"))
        self.patient.add_medical_history("dieta", assistant.listen_with_retry("¿Cómo describirías tu dieta diaria?"))

    def ask_family_history(self):
        self.patient.add_medical_history("antecedentes_familiares", assistant.listen_with_retry("¿Hay antecedentes de enfermedades en tu familia, como diabetes, hipertensión o cáncer?"))

    def ask_general_assessment(self):
        self.patient.add_medical_history("alergias", assistant.listen_with_retry("¿Tienes alguna alergia conocida?"))
        self.patient.add_medical_history("ultima_visita", assistant.listen_with_retry("¿Cuándo fue la última vez que visitaste a un médico?"))
        self.patient.add_medical_history("preocupaciones", assistant.listen_with_retry("¿Tienes alguna preocupación específica sobre tu salud que te gustaría discutir?"))

        
    def generate_medical_report(self):
        print("   ")


