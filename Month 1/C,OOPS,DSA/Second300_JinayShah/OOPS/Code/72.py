class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.patients = set()

    def assign_patient(self, patient):
        self.patients.add(patient)
        print(f"{self.name} is now assigned to {patient.name}.")

    def view_assigned_patients(self):
        print(f"{self.name}'s assigned patients:")
        for patient in self.patients:
            print(f"- {patient.name}")

class Patient:
    def __init__(self, patient_id, name, age, gender):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.doctor = None

    def assign_doctor(self, doctor):
        self.doctor = doctor
        doctor.assign_patient(self)
        print(f"{self.name} is now assigned to Dr. {doctor.name}.")

    def view_doctor(self):
        if self.doctor:
            print(f"{self.name}'s assigned doctor: Dr. {self.doctor.name}")
        else:
            print(f"{self.name} does not have an assigned doctor yet.")

class Appointment:
    def __init__(self, appointment_id, doctor, patient, date, time):
        self.appointment_id = appointment_id
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.time = time

    def schedule_appointment(self):
        print(f"Appointment scheduled for {self.patient.name} with Dr. {self.doctor.name} on {self.date} at {self.time}.")

class Hospital:
    def __init__(self, hospital_name):
        self.hospital_name = hospital_name
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)

    def add_patient(self, patient):
        self.patients.append(patient)

    def schedule_appointment(self, doctor, patient, date, time):
        appointment_id = len(self.appointments) + 1
        appointment = Appointment(appointment_id, doctor, patient, date, time)
        self.appointments.append(appointment)
        appointment.schedule_appointment()
        return appointment


hospital = Hospital("City Hospital")

doctor1 = Doctor(1, "John Smith", "Cardiologist")
doctor2 = Doctor(2, "Jane Doe", "Pediatrician")

patient1 = Patient(101, "Alice Johnson", 25, "Female")
patient2 = Patient(102, "Bob Miller", 35, "Male")

hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

hospital.add_patient(patient1)
hospital.add_patient(patient2)

patient1.assign_doctor(doctor1)
patient2.assign_doctor(doctor2)

doctor1.view_assigned_patients()
doctor2.view_assigned_patients()

appointment1 = hospital.schedule_appointment(doctor1, patient1, "2024-02-01", "10:00 AM")
appointment2 = hospital.schedule_appointment(doctor2, patient2, "2024-02-02", "02:30 PM")