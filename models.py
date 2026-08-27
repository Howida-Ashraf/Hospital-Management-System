class Person:
    def __init__(self, person_id, name, age, contact_info):
        self.id = person_id
        self.name = name
        self.age = age
        self.contact_info = contact_info

    def display_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Contact: {self.contact_info}")


class Patient(Person):
    def __init__(self, patient_id, name, age, contact_info, medical_history=""):
        if name == "":
            print("Invalid name, patient not created properly")

        super().__init__(patient_id, name, age, contact_info)
        self.medical_history = medical_history

    def display_info(self):
        print("Patient Information")
        super().display_info()
        print(f"Medical History: {self.medical_history}")

    def update_info(self, name=None, contact_info=None):
        if name:
            self.name = name
        if contact_info:
            self.contact_info = contact_info


def register_patient(patients_list, patient):
    patients_list.append(patient)
    print(f"Patient {patient.name} registered successfully")


def search_patient(patients_list, patient_id):
    for p in patients_list:
        if p.id == patient_id:
            return p
    print("Patient not found")
    return None
