class Appointment:
    def __init__(self, appointment_id, patient, doctor, date, time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = "Pending"

    def check_doctor_availability(self):
        for appointment in self.doctor.appointments:
            if (appointment.date == self.date and
                appointment.time == self.time and
                appointment.status == "Booked"):
                return False

        return True

    def book_appointment(self):
        if not self.check_doctor_availability():
            print("Doctor is not available at this time.")
            return False

        self.doctor.appointments.append(self)
        self.patient.appointments.append(self)

        self.status = "Booked"

        print("Appointment booked successfully.")
        return True

    def cancel_appointment(self):
        if self.status == "Booked":
            self.status = "Cancelled"
            print("Appointment cancelled successfully.")
            return True

        print("Appointment is already cancelled.")
        return False

    def display_appointment(self):
        print("\nAppointment Information")
        print(f"Appointment ID: {self.appointment_id}")
        print(f"Patient: {self.patient.name}")
        print(f"Doctor: {self.doctor.name}")
        print(f"Date: {self.date}")
        print(f"Time: {self.time}")
        print(f"Status: {self.status}")

