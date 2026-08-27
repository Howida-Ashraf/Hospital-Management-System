class Doctor:
    def __init__(self, doctor_id, name, age, phone, department):
        self.doctor_id = doctor_id
        self.name = name
        self.age = age
        self.phone = phone
        self.department = department
        self.appointments = []

    def display(self):
        print("Doctor ID:", self.doctor_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Phone:", self.phone)
        print("Department:", self.department.name)

    def update(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    def display_appointments(self):
        if not self.appointments:
            print("No appointments found.")
            return

        print(f"Appointments for Dr. {self.name}:")

        for appointment in self.appointments:
            appointment.display_appointment()


# Department class
class Department:
    def __init__(self, department_id, name):
        self.department_id = department_id
        self.name = name
        self.doctors = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def display(self):
        print("Department ID:", self.department_id)
        print("Department Name:", self.name)
        print("Doctors:")

        for doctor in self.doctors:
            print("-", doctor.name)


departments = []
doctors = []


def add_department():
    department_id = "D001"
    name = "Cardiology"

    if department_id == "" or name == "":
        print("Invalid department data")
        return

    department = Department(department_id, name)
    departments.append(department)

    print("Department added successfully")


def add_doctor():
    doctor_id = "DR001"
    name = "Ahmed Ali"
    age = 35
    phone = "01012345678"
    department_id = "D001"

    if doctor_id == "" or name == "" or phone == "":
        print("Invalid doctor data")
        return

    if age <= 0:
        print("Invalid age")
        return

    department = None

    for d in departments:
        if d.department_id == department_id:
            department = d
            break

    if department is None:
        print("Department not found")
        return

    doctor = Doctor(doctor_id, name, age, phone, department)
    doctors.append(doctor)
    department.add_doctor(doctor)

    print("Doctor added successfully")


def search_doctor():
    doctor_id = "DR001"

    for doctor in doctors:
        if doctor.doctor_id == doctor_id:
            doctor.display()
            return

    print("Doctor not found")


def display_doctors():
    for doctor in doctors:
        doctor.display()
        print()


def display_departments():
    for department in departments:
        department.display()
        print()


# Run program
add_department()
add_doctor()

print("\nAll Doctors")
display_doctors()

print("\nAll Departments")
display_departments()

print("\nSearch Doctor")
search_doctor()