# Hospital-Management-System
# 🏥 Clinic / Hospital Management System

## 1. Project Name

**Clinic / Hospital Management System**

A Python-based Object-Oriented Programming (OOP) system designed to manage patients, doctors, departments, appointments, medical records, and billing.

---

## 2. Problem Description

A small clinic needs an internal system to manage its daily operations without using a database or graphical user interface.

The system allows the clinic to:

* Register patients.
* Add and manage doctors.
* Add medical departments.
* Book and cancel appointments.
* Check doctor availability.
* Display patient and doctor appointments.
* Create and manage medical records.
* Generate and calculate patient bills.
* Search for patients and doctors.
* Validate different operations.

The project is implemented using **Python, OOP, modules, and imports**, with multiple classes interacting with each other.

---

## 3. Team Members

| Student   | Responsibility        |
| --------- | --------------------- |
| Student 1 | Person & Patient      |
| Student 2 | Doctor & Department   |
| Student 3 | Appointment           |
| Student 4 | Medical Record        |
| Student 5 | Billing & Integration |

### Team Names

* **Student 1:** Mariem Mohammed
* **Student 2:** Howida Ashraf
* **Student 3:** Nora Samir
* **Student 4:** Asmaa Sobhy
* **Student 5:** Rahma Atiaa

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

`Person` provides common information and behavior shared by other people in the system.

---

### 4.2 Patient

Inherits from `Person`.

Represents a patient who can book appointments and receive medical records and bills.

**Additional functionality:**

* Patient information
* Medical history
* Appointments
* Patient registration
* Patient search and update

---

### 4.3 Doctor

Inherits from `Person`.

Represents a doctor who is assigned to appointments and belongs to a specific department.

**Additional functionality:**

* Specialty
* Department
* Schedule
* Doctor appointments
* Doctor search and validation

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

The appointment class handles:

* Booking appointments
* Cancelling appointments
* Checking doctor availability
* Displaying patient appointments
* Displaying doctor appointments
* Appointment validation

---

### 4.6 MedicalRecord

Stores medical information related to a patient's appointment.

**Main information:**

* Record ID
* Patient
* Appointment
* Diagnosis
* Notes

The medical record class handles:

* Creating records
* Displaying records
* Searching records
* Updating records
* Validating records

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

The bill class handles:

* Generating patient bills
* Calculating the total bill
* Displaying bills
* Billing validation

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

It also supports the integration of the different modules and the main system operations.

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

It manages patient information and demonstrates inheritance through the `Person` base class.

---

### `doctor_department.py`

Contains:

* `Doctor`
* `Department`

It manages doctors and medical departments and handles the relationship between them.

---

### `appointments.py`

Contains:

* `Appointment`

It manages appointments between patients and doctors, including booking, cancellation, availability, and appointment validation.

---

### `medical_records.py`

Contains:

* `MedicalRecord`

It manages patient medical records and their relationship with patients and appointments.

---

### `billing.py`

Contains:

* `Bill`
* `ClinicSystem`

It manages patient billing and supports the integration and coordination of the different system components.

---

### `main.py`

The main demonstration file.

It imports the required classes from the different modules and demonstrates how the complete hospital management system works.

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

A medical record is associated with a patient and an appointment.

```text
MedicalRecord
   ├──> Patient
   └──> Appointment
```

---

### Bill → Patient / Appointment

A bill is associated with a patient and an appointment.

```text
Bill
   ├──> Patient
   └──> Appointment
```

---

### ClinicSystem → All Components

The `ClinicSystem` coordinates the main entities of the hospital system.

```text
ClinicSystem
   ├──> Patients
   ├──> Doctors
   ├──> Departments
   ├──> Appointments
   ├──> Medical Records
   └──> Bills
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
    MedicalRecord    Bill
           \         /
            \       /
             ClinicSystem
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

Extends `Person` with doctor-specific information such as specialty, department, and schedule.

Inheritance reduces code duplication and allows common functionality to be reused.

---

## 8. Main System Features

The system implements the required clinic operations:

### Patient Management

* Register patient
* Display patient
* Update patient
* Search patient
* Validate patient information

### Doctor & Department Management

* Add doctor
* Add department
* Display doctor
* Display department
* Search doctor
* Update doctor
* Assign doctor to department
* Validate doctor information

### Appointment Management

* Book appointment
* Cancel appointment
* Display patient appointments
* Display doctor appointments
* Check doctor availability
* Validate appointment availability

### Medical Records

* Create medical record
* Display medical record
* Search medical record
* Update medical record
* Link medical record to patient and appointment
* Validate medical record

### Billing

* Generate patient bill
* Calculate bill
* Display bill
* Link bill to patient and appointment
* Validate billing information

---

## 9. How to Run the Project

### Requirements

* Python 3.x
* No database
* No GUI
* No external libraries are required.

The project uses Python's standard functionality and focuses on Python OOP, modules, and imports.

### Steps

1. Clone or download the project.

2. Open the project folder in VS Code or another Python IDE.

3. Make sure all Python files are in the same project folder.

4. Run the main file:

```bash
python main.py
```

5. The program will demonstrate the different hospital management operations.

---

## 10. Example Output

Example output from the system:

```text
========== Hospital Management System ==========

--- Patient Management ---

Patient registered successfully!
ID: P001
Name: Ahmed Ali

Patient registered successfully!
ID: P002
Name: Sara Mohamed

Patient registered successfully!
ID: P003
Name: Omar Hassan


--- Doctor & Department Management ---

Department added successfully!
ID: DEP001
Name: Cardiology

Doctor added successfully!
ID: D001
Name: Dr. Ahmed
Specialty: Cardiology

Doctor added successfully!
ID: D002
Name: Dr. Sara
Specialty: Pediatrics


--- Appointment Management ---

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


Doctor Appointments:
Dr. Ahmed -> Ahmed Ali
Date: 2026-08-30
Time: 10:00 AM


--- Medical Record ---

Medical record created successfully!

Patient: Ahmed Ali
Diagnosis: Hypertension
Notes: Patient should follow up after one week.


--- Billing ---

Bill generated successfully!

Patient: Ahmed Ali
Consultation Fee: $100
Additional Charges: $50
Total Bill: $150


--- Cancellation ---

Appointment cancelled successfully!


--- Validation ---

Doctor is not available at this time.
Appointment cannot be booked.
```

---

## 11. OOP Concepts Used

### 11.1 Classes and Objects

The system is built using classes such as:

* `Person`
* `Patient`
* `Doctor`
* `Department`
* `Appointment`
* `MedicalRecord`
* `Bill`
* `ClinicSystem`

Objects are created from these classes to represent real entities in the hospital.

---

### 11.2 Constructors

Each class uses a constructor to initialize its object attributes.

For example:

```python
class Patient(Person):
    def __init__(self, patient_id, name, age, contact):
        ...
```

Constructors allow objects to be created with their required information.

---

### 11.3 Encapsulation

Each class keeps its related data and methods together.

For example, the `Appointment` class contains appointment information and methods related to appointment operations.

This keeps the code organized and makes each class responsible for its own functionality.

---

### 11.4 Inheritance

`Patient` and `Doctor` inherit from the `Person` class.

```python
class Patient(Person):
    ...

class Doctor(Person):
    ...
```

This allows common attributes and behavior to be reused instead of being duplicated.

---

### 11.5 Abstraction

The `ClinicSystem` provides high-level operations for managing the hospital system.

For example:

```python
register_patient()
add_doctor()
add_department()
book_appointment()
cancel_appointment()
generate_bill()
search_patient()
search_doctor()
```

The user can perform these operations without needing to know all the internal implementation details.

---

### 11.6 Object Relationships

The project demonstrates relationships between objects.

For example:

* A `Patient` can have multiple appointments.
* An `Appointment` connects a `Patient` with a `Doctor`.
* A `Doctor` belongs to a `Department`.
* A `MedicalRecord` is linked to a patient and appointment.
* A `Bill` is linked to a patient and appointment.
* The `ClinicSystem` coordinates the different entities.

---

## 12. Project Structure

```text
Hospital_Project/
│
├── models.py
│   ├── Person
│   └── Patient
│
├── doctor_department.py
│   ├── Doctor
│   └── Department
│
├── appointments.py
│   └── Appointment
│
├── medical_records.py
│   └── MedicalRecord
│
├── billing.py
│   ├── Bill
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
4. Assigning doctors to departments.
5. Booking several appointments.
6. Displaying patient appointments.
7. Displaying doctor appointments.
8. Creating a medical record for at least one appointment.
9. Generating and calculating a patient bill.
10. Cancelling an appointment.
11. Demonstrating a validation case where a doctor is unavailable.

The demonstration shows how the different modules and classes work together as one complete system.

---

## 14. Testing and Validation

Each module is tested individually before integration.

### Patient Testing

* Valid patient registration
* Searching for an existing patient
* Updating patient information
* Invalid patient information

### Doctor Testing

* Adding a doctor
* Searching for a doctor
* Assigning a doctor to a department
* Invalid doctor information

### Appointment Testing

* Booking an available doctor
* Cancelling an appointment
* Displaying appointments
* Trying to book an unavailable doctor

### Medical Record Testing

* Creating a medical record
* Searching for a record
* Updating a record
* Invalid record information

### Billing Testing

* Generating a bill
* Calculating the total amount
* Displaying the bill
* Invalid billing information

After individual testing, all modules are integrated and tested together through `main.py`.

---

## 15. Team Responsibilities

The project is divided among five team members:

### Student 1 — Patient & Person

Responsible for:

* `Person`
* `Patient`
* Patient operations
* Patient validation
* Patient README section
* Patient presentation section
* Patient testing

### Student 2 — Doctor & Department

Responsible for:

* `Doctor`
* `Department`
* Doctor and department operations
* Doctor-department relationship
* Doctor validation
* Doctor & Department README section
* Classes & Relationships presentation section
* Doctor and department testing

### Student 3 — Appointment

Responsible for:

* `Appointment`
* Booking
* Cancellation
* Availability checking
* Patient and doctor appointment display
* Appointment validation
* Appointment README section
* Appointment workflow presentation section
* Appointment testing

### Student 4 — Medical Record

Responsible for:

* `MedicalRecord`
* Creating records
* Searching and displaying records
* Updating records
* Patient/appointment relationships
* Record validation
* Medical Record README section
* Medical Record presentation section
* Medical Record testing

### Student 5 — Billing & Integration

Responsible for:

* `Bill`
* Generating bills
* Calculating bills
* Displaying bills
* Billing validation
* Integration between modules
* Final `main.py`
* Billing README section
* How to Run section
* Example Output section
* Billing presentation section
* Final demonstration

---

## 16. Conclusion

The Clinic / Hospital Management System demonstrates how Object-Oriented Programming can be used to model a real-world healthcare system.

The project applies:

* Classes and objects
* Constructors
* Encapsulation
* Inheritance
* Abstraction
* Object relationships
* Modules and imports
* Business logic
* Validation
* Multi-file project organization

The system provides a simple way to manage patients, doctors, departments, appointments, medical records, and billing while demonstrating the core Python OOP concepts required by the project.
