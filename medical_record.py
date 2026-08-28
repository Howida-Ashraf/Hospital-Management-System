
from models import Patient
from appointments import Appointment
from doctor_departments import Doctor, Department

class MedicalRecord:
    def __init__(self, record_id, patient, appointment, diagnosis, notes):
        self._record_id = record_id
        self._patient = patient
        self._appointment = appointment
        self._diagnosis = diagnosis
        self._notes = notes

    def get_record_id(self):
        return self._record_id

    def get_patient(self):
        return self._patient

    def get_appointment(self):
        return self._appointment

    def get_diagnosis(self):
        return self._diagnosis

    def get_notes(self):
        return self._notes

    def set_diagnosis(self, new_diagnosis):
        if new_diagnosis and new_diagnosis.strip() != "":
            self._diagnosis = new_diagnosis
        else:
            print("Diagnosis can't be empty")

    def set_notes(self, new_notes):
        self._notes = new_notes

    def display_record(self):
        print("Record ID:", self._record_id)
        print("Patient:", self._patient.name, "ID:", self._patient.id)
        print("Appointment ID:", self._appointment.appointment_id, "Doctor:", self._appointment.doctor.name, "Date:", self._appointment.date, "Time:", self._appointment.time)
        print("Diagnosis:", self._diagnosis)
        print("Notes:", self._notes)
        print("------------------------")

    def update_record(self, new_diagnosis=None, new_notes=None):
        if new_diagnosis:
            self.set_diagnosis(new_diagnosis)
        if new_notes:
            self.set_notes(new_notes)
        print("Record", self._record_id, "updated")

class MedicalRecordManager:
    def __init__(self):
        self.records = []
        self.next_id = 1

    def create_medical_record(self, patient, appointment, diagnosis, notes):

        if appointment.patient.id != patient.id:
            print("this appointment doesn't belong to the patient")
            return None

        if appointment.status != "Booked":
            print("can't create a record for an appointment that isn't booked")
            return None

        if diagnosis.strip() == "":
            print("diagnosis can't be empty!")
            return None

        for i in self.records:
            if i.get_appointment().appointment_id == appointment.appointment_id:
                print("Error, record already exist for this appointment")
                return None

        new_record = MedicalRecord(self.next_id, patient, appointment, diagnosis, notes)
        self.records.append(new_record)
        self.next_id += 1
        print("Record created with ID:", new_record.get_record_id())
        return new_record

    def search_by_patient(self, patient_id):
        result = []
        for r in self.records:
            if r.get_patient().id == patient_id:
                result.append(r)
        if len(result) == 0:
            print("no records for this patient")
        return result

    def search_by_record_id(self, record_id):
        for a in self.records:
            if a.get_record_id() == record_id:
                return a
        print("record not found!")
        return None

    def display_all_records(self):
        if len(self.records) == 0:
            print("no records yet")
            return None
        for r in self.records:
            r.display_record()

    def update_record(self, record_id, new_diagnosis=None, new_notes=None):
        record = self.search_by_record_id(record_id)
        if record is not None:
            record.update_record(new_diagnosis, new_notes)

    def remove_record(self, record_id):
        record = self.search_by_record_id(record_id)
        if record is not None:
            self.records.remove(record)
            print("Record", record_id, "removed")
