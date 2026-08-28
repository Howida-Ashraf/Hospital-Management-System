from datetime import datetime

class Bill:
    _id_counter = 1  

    def __init__(self, patient, appointment=None, services=None):
        self.bill_id = Bill._id_counter
        Bill._id_counter += 1
        self.patient = patient            
        self.appointment = appointment    
        self.services = services if services else []   
        self.total_amount = 0.0
        self.is_paid = False
        self.date_issued = datetime.now()

    def add_service(self, service_name, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.services.append((service_name, price))

    def calculate_bill(self):
        self.total_amount = sum(price for _, price in self.services)
        return self.total_amount

    def mark_as_paid(self):
        self.is_paid = True

    def display_bill(self):
        print("=" * 42)
        print(f"Bill ID       : {self.bill_id}")
        patient_id = getattr(self.patient, "id", "N/A")
        print(f"Patient       : {self.patient.name} (ID: {patient_id})")
        if self.appointment:
            apt_id = getattr(self.appointment, "appointment_id", getattr(self.appointment, "id", "N/A"))
            doctor = getattr(self.appointment, "doctor", None)
            doctor_name = getattr(doctor, "name", "N/A") if doctor else "N/A"
            date_time = getattr(self.appointment, "date_time", None)
            if date_time is None:
                date_ = getattr(self.appointment, "date", "")
                time_ = getattr(self.appointment, "time", "")
                date_time = f"{date_} {time_}".strip()
            print(f"Appointment   : #{apt_id} with Dr. {doctor_name} on {date_time}")
        print(f"Date Issued   : {self.date_issued.strftime('%Y-%m-%d %H:%M')}")
        print("-" * 42)
        for name, price in self.services:
            print(f"  {name:<28}{price:>10.2f} EGP")
        print("-" * 42)
        print(f"  {'Total':<28}{self.total_amount:>10.2f} EGP")
        print(f"Status        : {'Paid' if self.is_paid else 'Unpaid'}")
        print("=" * 42)


def generate_patient_bill(patient, appointment, services):

    if patient is None:
        raise ValueError("A valid Patient is required to generate a bill.")

    if appointment is not None and getattr(appointment, "patient", None) is not patient:
        raise ValueError("This Appointment does not belong to this Patient!")

    if not services:
        raise ValueError("At least one service is required to calculate the bill.")

    for name, price in services:
        if price < 0:
            raise ValueError(f"Invalid price for service '{name}'.")

    
    bill = Bill(patient, appointment, services)
    bill.calculate_bill()

    
    if not hasattr(patient, "bills"):
        patient.bills = []
    patient.bills.append(bill)

    return bill



class ClinicSystemBillingMixin:
    
    def __init__(self):
        self.bills = []

    def generate_bill(self, patient, appointment, services):
        bill = generate_patient_bill(patient, appointment, services)
        self.bills.append(bill)
        return bill

    def get_bills_for_patient(self, patient):
        return [b for b in self.bills if b.patient is patient]



if __name__ == "__main__":
    from models import Patient
    from doctor_departments import Doctor, Department
    from appointments import Appointment

    system = ClinicSystemBillingMixin()

    p1 = Patient(1, "Ahmed Ali", 30, "01000000000")
    p2 = Patient(2, "Mona Youssef", 25, "01565656565")
    cardiology = Department("D001", "Cardiology")
    d1 = Doctor("DR001", "Dr. Hanan", 40, "01111111111", cardiology)
    appt1 = Appointment(101, p1, d1, "2026-08-20", "10:00")
    appt1.book_appointment()

    print("### 1) Generate a valid bill linked to a real Appointment ###")
    services = [("Consultation", 300), ("ECG Test", 150), ("Medication", 80)]
    bill1 = system.generate_bill(p1, appt1, services)
    bill1.display_bill()
    bill1.mark_as_paid()
    print(f"\nStatus after payment: {'Paid' if bill1.is_paid else 'Unpaid'}\n")

    print("### 2) Validation case: appointment belongs to a different patient ###")
    try:
        system.generate_bill(p2, appt1, services)
    except ValueError as e:
        print("Validation Error:", e)

    print("\n### 3) Validation case: negative price ###")
    try:
        system.generate_bill(p1, None, [("X-Ray", -50)])
    except ValueError as e:
        print("Validation Error:", e)

    print("\n### 4) Retrieve all bills for a specific patient ###")
    for b in system.get_bills_for_patient(p1):
        print(f"Bill #{b.bill_id} - Total: {b.total_amount} EGP")
