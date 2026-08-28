# Hospital-Management-System
Hospital-Management-System
# 🏥 Clinic / Hospital Management System

## 1. Project Name

**Clinic / Hospital Management System**

A Python-based Object-Oriented Programming (OOP) system designed to manage patients, doctors, departments, appointments, medical records, and billing.

---

## 2. Problem Description

A small clinic needs an internal system to manage its daily operations without using a database or graphical user interface.

The system allows the clinic to:

* Register patients.
* Add doctors.
* Add medical departments.
* Book and cancel appointments.
* Display patient and doctor appointments.
* Create medical records.
* Generate and calculate patient bills.
* Search for patients and doctors.
* Validate appointment availability.

The project is implemented using **Python, OOP, modules, and imports**, with multiple classes interacting with each other.

---

## 3. Team Members

| Student   | Responsibility                                    |
| --------- | ------------------------------------------------- |
| Student 1 | Person, Patient, Doctor classes                   |
| Student 2 | Department, MedicalRecord, Bill classes           |
| Student 3 | Appointment class and ClinicSystem business logic |
| Student 4 | Integration, main.py, README, and testing         |

### Team Names

* **Student 1:** [Name]
* **Student 2:** [Name]
* **Student 3:** [Name]
* **Student 4:** [Name]

---

## 4. Classes

The system contains the following main classes:

### 4.1 Person

The base class for people in the clinic.

**Main attributes:**

* ID
* Name
* Age
* Contact information

---

### 4.2 Patient

Inherits from `Person`.

Represents a patient who can book appointments and receive medical records and bills.

**Additional functionality:**

* Patient information
* Medical history
* Appointments

---

### 4.3 Doctor

Inherits from `Person`.

Represents a doctor who is assigned to appointments and belongs to a specific department.

**Additional functionality:**

* Specialty
* Department
* Schedule
* Doctor appointments

---

### 4.4 Department

Represents a medical department such as:

* Cardiology
* Pediatrics
* Dermatology
* Internal Medicine

A department can have multiple doctors.

---

### 4.5 Appointment

Represents an appointment between a patient and a doctor at a specific date and time.

**Main information:**

* Appointment ID
* Patient
* Doctor
* Date
* Time
* Status

The appointment can be booked, cancelled, or checked for availability.

---

### 4.6 MedicalRecord

Stores medical information related to a patient's appointment.

**Main information:**

* Record ID
* Patient
* Appointment
* Diagnosis
* Notes

---

### 4.7 Bill

Represents the charges for a patient's visit.

**Main information:**

* Bill ID
* Patient
* Appointment
* Consultation fee
* Additional charges
* Total amount

The bill can be calculated based on the different charges.

---

### 4.8 ClinicSystem

The central manager class of the project.

It coordinates the different parts of the system, including:

* Patients
* Doctors
* Departments
* Appointments
* Medical records
* Bills

It also contains the main business operations such as registration, booking, cancellation, searching, and billing.

---

## 5. Modules

The project is divided into multiple Python modules:

```text
Hospital_Project/
│
├── models.py
├── doctor_department.py
├── appointments.py
├── medical_records.py
├── billing.py
└── main.py
```

### `models.py`

Contains:

* `Person`
* `Patient`

It represents the main people/entities in the clinic and demonstrates inheritance.

---

### `doctor_department.py`

Contains:

* `Department`
* doctor

It manages medical departments and their doctors.

---

### `appointments.py`

Contains:

* `Appointment`

It manages appointments between patients and doctors.

---

### `records.py`

Contains:

* `MedicalRecord`

It handles medical records and patient billing.

---

### `billing.py`

Contains:

* `ClinicSystem`
* billing

It is the central system that coordinates all entities and implements the main business operations.

---

### `main.py`

The main demonstration file.

It imports the required classes and demonstrates how the complete system works.

---

## 6. Relationships Between Classes

The system contains multiple relationships between objects.

### Patient → Appointment

A patient can book one or more appointments.

```text
Patient
   │
   └── books ──> Appointment
```

---

### Appointment → Patient and Doctor

Each appointment is connected to exactly one patient and one doctor.

```text
Appointment
   ├──> Patient
   └──> Doctor
```

---

### Doctor → Department

A doctor belongs to a medical department.

```text
Doctor
   │
   └── belongs to ──> Department
```

---

### MedicalRecord → Patient / Appointment

A medical record is associated with a patient and typically with an appointment.

```text
MedicalRecord
   ├──> Patient
   └──> Appointment
```

---

### Bill → Patient / Appointment

A bill is associated with a patient and typically with an appointment.

```text
Bill
   ├──> Patient
   └──> Appointment
```

---

### Overall Relationship

```text
                 Person
                /      \
               /        \
          Patient       Doctor
             |             |
             |             |
             v             v
        Appointment --> Department
             |
        ┌────┴────┐
        ↓         ↓
 MedicalRecord   Bill
```

---

## 7. Inheritance

The project uses inheritance through the `Person` class.

`Patient` and `Doctor` inherit common attributes and behavior from `Person`.

```text
             Person
             /    \
            /      \
       Patient     Doctor
```

### Person

Contains common information such as:

* ID
* Name
* Age
* Contact information

### Patient

Extends `Person` with patient-specific information and behavior.

### Doctor

Extends `Person` with doctor-specific information such as specialty and schedule.

This reduces code duplication and demonstrates **inheritance** in OOP.

---

## 8. Main System Features

The system implements the required clinic operations:

* Register patient
* Add doctor
* Add department
* Book appointment
* Cancel appointment
* Display patient appointments
* Display doctor appointments
* Create medical record
* Generate patient bill
* Calculate bill
* Search patient
* Search doctor

These features correspond to the required operations specified in the project assignment.

---

## 9. How to Run the Project

### Requirements

* Python 3.x
* No database
* No GUI
* No external libraries are required.

The project uses Python's standard functionality, as required by the assignment.

### Steps

1. Clone or download the project.

2. Open the project folder in VS Code or another Python IDE.

3. Make sure all Python files are in the same project folder.

4. Run:

```bash
python main.py
```

5. The program will demonstrate the different hospital management operations.

---

## 10. Example Output

Example output from the system:

```text
========== Hospital Management System ==========

Patient registered successfully:
ID: P001
Name: Ahmed Ali

Patient registered successfully:
ID: P002
Name: Sara Mohamed

Patient registered successfully:
ID: P003
Name: Omar Hassan


Doctor added successfully:
ID: D001
Name: Dr. Ahmed
Specialty: Cardiology


Doctor added successfully:
ID: D002
Name: Dr. Sara
Specialty: Pediatrics


Department added successfully:
ID: DEP001
Name: Cardiology


Appointment booked successfully!

Appointment ID: A001
Patient: Ahmed Ali
Doctor: Dr. Ahmed
Date: 2026-08-30
Time: 10:00 AM
Status: Confirmed


Patient Appointments:
Ahmed Ali -> Dr. Ahmed
Date: 2026-08-30
Time: 10:00 AM


Medical record created successfully!

Diagnosis: Hypertension
Notes: Patient should follow up after one week.


Bill generated successfully!

Patient: Ahmed Ali
Consultation Fee: $100
Additional Charges: $50
Total Bill: $150


Appointment cancelled successfully!


Validation:
Doctor is not available at this time.
Appointment cannot be booked.
```

---

## 11. OOP Concepts Used

### 11.1 Classes and Objects

The system is built using classes such as:

* `Patient`
* `Doctor`
* `Department`
* `Appointment`
* `MedicalRecord`
* `Bill`
* `ClinicSystem`

Objects are created from these classes to represent real entities in the clinic.

---

### 11.2 Encapsulation

Each class keeps its related data and methods together.

For example, the `Appointment` class contains appointment information and methods related to appointment operations.

---

### 11.3 Inheritance

`Patient` and `Doctor` inherit from the `Person` class.

```python
class Patient(Person):
    ...

class Doctor(Person):
    ...
```

This allows common attributes and behavior to be reused.

---

### 11.4 Abstraction

The `ClinicSystem` class provides high-level operations such as:

```python
register_patient()
add_doctor()
book_appointment()
cancel_appointment()
generate_bill()
search_patient()
```

The user of the system does not need to know all the internal implementation details.

---

### 11.5 Object Relationships

The project demonstrates relationships between objects.

For example:

* A `Patient` has appointments.
* An `Appointment` connects a `Patient` with a `Doctor`.
* A `Doctor` belongs to a `Department`.
* A `MedicalRecord` belongs to a patient.
* A `Bill` belongs to a patient.

---

## 12. Project Structure

```text
Hospital_Project/
│
├── models.py
│   ├── Person
│   ├── Patient
│   └── Doctor
│
├── departments.py
│   └── Department
│
├── appointments.py
│   └── Appointment
│
├── records.py
│   ├── MedicalRecord
│   └── Bill
│
├── clinic.py
│   └── ClinicSystem
│
├── main.py
│
└── README.md
```

---

## 13. Demonstration

The `main.py` file demonstrates the complete system by:

1. Registering at least 3 patients.
2. Adding at least 2 doctors.
3. Adding at least 1 department.
4. Booking several appointments.
5. Creating a medical record for at least one appointment.
6. Generating and calculating a patient bill.
7. Cancelling an appointment.
8. Demonstrating a validation case where a doctor is unavailable.

These demonstrations are specifically required by the project instructions.

---

## 14. Conclusion

The Clinic / Hospital Management System demonstrates how Object-Oriented Programming can be used to model a real-world system.

The project applies:

* Classes and objects
* Constructors
* Encapsulation
* Inheritance
* Object relationships
* Modules and imports
* Business logic
* Validation

The system is designed as a multi-file Python project and focuses on practicing OOP concepts rather than building a production application.
