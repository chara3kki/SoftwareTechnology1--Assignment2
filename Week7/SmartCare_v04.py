from datetime import date, datetime
from enum import Enum

class Patient: 
    def __init__(self, patient_id: str, name:str, dob: date, contact: str):

        if not patient_id:
            raise ValueError("Patient ID is required.")
        if not name:
            raise ValueError("The Name is Required.")
        if not isinstance(dob, date): 
            raise ValueError("DOB must be a date.")
        if not contact:
            raise ValueError("Contact is required")

        self.patient_id: str = patient_id
        self.name: str = name
        self.dob: date = dob
        self.contact: str = contact 

    def edit_patient(self, name: str = None, contact: str = None) -> None:
        if name is not None:
            if not name:
                raise ValueError("Name cannot be empty")
            
            self.name = name
        if contact is not None:
            if not contact:
                raise ValueError("Contact cannot be empty")
        
            self.contact = contact 

class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        if not practitioner_id:
            raise ValueError("Pracitioner ID is required.")
        
        if not name:
            raise ValueError("The Name is required.")
        
        if not specialty:
            raise ValueError("Specialty is required.")

        self.practitioner_id: str = practitioner_id
        self.name: str = name
        self.specialty: str = specialty

class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    ONGOING = "Ongoing"


class AppointmentError(Exception):
    """Raised for scheduling conflicts and invalid status transitions."""
    pass


class Appointment:
    def __init__(self, appointment_id: str, patient, practitioner,
                 appt_date: date, time_slot: str):
        if not appointment_id:
            raise ValueError("appointment_id is required.")
        if patient is None:
            raise ValueError("patient is required.")
        if practitioner is None:
            raise ValueError("practitioner is required.")
        if not isinstance(appt_date, date):
            raise ValueError("appt_date must be a date.")
        if not time_slot:
            raise ValueError("time_slot is required.")

        self.appointment_id: str = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date: date = appt_date
        self.time_slot: str = time_slot
        self.status: AppointmentStatus = AppointmentStatus.SCHEDULED

    def check_overlap(self, existing_appointments: list) -> bool:
        """FR-06: True if this appointment's practitioner/date/time_slot
        conflicts with any appointment already in existing_appointments."""
        for other in existing_appointments:
            if other is self:
                continue
            if other.status == AppointmentStatus.CANCELLED:
                continue
            if (other.practitioner is self.practitioner
                    and other.date == self.date
                    and other.time_slot == self.time_slot):
                return True
        return False

    def book(self, existing_appointments: list) -> None:
        """FR-05: confirm booking, rejecting it if the practitioner
        already has a conflicting appointment."""
        if self.check_overlap(existing_appointments):
            raise AppointmentError(
                "Practitioner already has an appointment at this date and time slot."
            )
        self.status = AppointmentStatus.SCHEDULED

    def cancel(self) -> None:
        """FR-09: cancel the appointment; the record is retained, not deleted."""
        self.status = AppointmentStatus.CANCELLED

    def update_status(self, new_status: AppointmentStatus) -> None:
        """FR-08 / User Story 3: change status, rejecting invalid transitions."""
        if self.status == AppointmentStatus.CANCELLED and new_status == AppointmentStatus.COMPLETED:
            raise AppointmentError("Cancelled appointments cannot be marked complete.")
        self.status = new_status


patients = []
practitioners = []
appointments = []


def find_by_id(items, attr, value):
    for item in items:
        if getattr(item, attr) == value:
            return item
    return None


def read_date(prompt):
    return datetime.strptime(input(prompt).strip(), "%Y-%m-%d").date()


def add_patient():
    try:
        patient = Patient(
            input("Patient ID: ").strip(),
            input("Name: ").strip(),
            read_date("Date of birth (YYYY-MM-DD): "),
            input("Contact: ").strip(),
        )
    except ValueError as e:
        print(f"Could not add patient: {e}")
        return
    patients.append(patient)
    print(f"Patient {patient.name} added.")


def edit_patient():
    patient = find_by_id(patients, "patient_id", input("Patient ID to edit: ").strip())
    if patient is None:
        print("Patient not found.")
        return
    new_name = input("New name (leave blank to keep): ").strip()
    new_contact = input("New contact (leave blank to keep): ").strip()
    try:
        patient.edit_patient(new_name or None, new_contact or None)
    except ValueError as e:
        print(f"Could not edit patient: {e}")
        return
    print("Patient updated.")


def add_practitioner():
    try:
        practitioner = Practitioner(
            input("Practitioner ID: ").strip(),
            input("Name: ").strip(),
            input("Specialty: ").strip(),
        )
    except ValueError as e:
        print(f"Could not add practitioner: {e}")
        return
    practitioners.append(practitioner)
    print(f"Practitioner {practitioner.name} added.")


def book_appointment():
    patient = find_by_id(patients, "patient_id", input("Patient ID: ").strip())
    practitioner = find_by_id(practitioners, "practitioner_id", input("Practitioner ID: ").strip())
    if patient is None or practitioner is None:
        print("Patient or practitioner not found. Add them first.")
        return
    try:
        appt = Appointment(
            input("Appointment ID: ").strip(),
            patient,
            practitioner,
            read_date("Date (YYYY-MM-DD): "),
            input("Time slot (e.g. 10:00-10:30): ").strip(),
        )
        appt.book(appointments)
    except (ValueError, AppointmentError) as e:
        print(f"Could not book: {e}")
        return
    appointments.append(appt)
    print("Appointment booked.")


def cancel_appointment():
    appt = find_by_id(appointments, "appointment_id", input("Appointment ID to cancel: ").strip())
    if appt is None:
        print("Appointment not found.")
        return
    appt.cancel()
    print("Appointment cancelled (record kept).")


def change_status():
    appt = find_by_id(appointments, "appointment_id", input("Appointment ID: ").strip())
    if appt is None:
        print("Appointment not found.")
        return
    options = list(AppointmentStatus)
    for i, s in enumerate(options, 1):
        print(f"  {i}) {s.value}")
    try:
        new_status = options[int(input("New status number: ").strip()) - 1]
        appt.update_status(new_status)
    except (ValueError, IndexError):
        print("Invalid status choice.")
        return
    except AppointmentError as e:
        print(f"Could not update: {e}")
        return
    print(f"Status is now {appt.status.value}.")


def show_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    for a in appointments:
        print(f"{a.appointment_id} | {a.patient.name} | {a.practitioner.name} "
              f"({a.practitioner.specialty}) | {a.date} {a.time_slot} | {a.status.value}")


def main():
    print("Welcome to SmartCare: Community Clinic Appointment Booking System!")
    actions = {
        "1": add_patient,
        "2": edit_patient,
        "3": add_practitioner,
        "4": book_appointment,
        "5": cancel_appointment,
        "6": change_status,
        "7": show_appointments,
    }
    while True:
        print("\n1) Add patient  2) Edit patient  3) Add practitioner  4) Book appointment")
        print("5) Cancel appointment  6) Change status  7) Show appointments  8) Quit")
        choice = input("Choose: ").strip()
        if choice == "8":
            print("Goodbye.")
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()