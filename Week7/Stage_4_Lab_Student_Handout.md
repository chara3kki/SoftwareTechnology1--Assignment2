# Assignment 2 - Case Study Stage 4 Lab Activities Implementing the SmartCare Domain Layer

<h1><b> A - Revisit Approved UML </b></h1>
<p><i> Confirm responsiblities, attributes and relationships before coding. </i></p>

<h3><b> Patient </b></h3>

- Responsibilities: create, etid, search, and provide appointment history. 
- Attributes: patientId, name, dob, and contact. 
- Relationships: assocition to Appointment, 1 to 0..*
- Implemented? <b> Yes </b>

<h3><b> Practitioner </b></h3>

- Responisibilities: register, view schedule, and check overlap. 
- Attributes: practitionerId, name, availability
- Relationships: association to Apppointment, 1 to 0..*
- Implemented? <b> Yes </b>

<h3><b> Appointment </b></h3> 

- Responsibilities: book, cancel, update status, and check overlap.
- Attributes: appointmentId, date, timeSlot, and status.
- Relationships: association to Patient, and Practitioner. 
- Implemented? <b> Yes </b>

<h1><b> B - Implement Patient: AI OFF </b></h1> 
<p><i> Implement Patient with type hints and basic validation. </i></p>

```
from datetime import date

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

    def edit_patinet(self, name: str = None, contact: str = None) -> None:
        if name is non None:
            if not name:
                raise ValueError("Name cannot be empty")
            
            self.name = name
        if contact is not None:
            if not contact:
            rase ValueError("Contact cannot be empty")
        
            self.contact = contact 
```

<h1><b> C - Implement Practitioner: AI OFF </b></h1>
<p><i> Implement Practitioner with identifier, name and specialty; no database logic. </i></p>

- Here is what it gave me.

```
class Practitioner:
    def __init__(self, practitioner_id: str, name: str, specialty: str):
        if not practitioner_id:
            raise ValueError("Pracitioner ID is required.")
        
        if not name:
            raise ValueError("The Name is required.")
        
        if not specialty:
            raise ValueError("Specialty is required.")

        self.practitioner_id: str = pracititoner_id
        self.name: str = name
        self.specialty: str = specialty
```

<h1><b> D - Implement Appointment: AI ON </b></h1>
<p><i> Give AI the approved Appointment UML, business rules and explicit constraints. Ask it to implement only Appointment and agreed enum/exception. </i></p>

```
from enum import Enum
from datetime import date


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
```

<h1><b> E - Review Generated Code </b></h1>
<p><i> Check model consistency, unsupported features, public state mutation, unnecessary inheritance, invented dependencies and error handling. </i></p>

<h3><b> Model Consistency </b></h3>

- Matches the UML.
- Same operations and everything. 

<h3><b> Unsupported Features </b></h3>

- Added nothing.

<h3><b> Public State Mutation </b></h3>

- self.status is set directly (self.status - AppointmentStatus.SCHEDULED< etc.) rather than going through a private field with a settter. 

<h3><b> Invented Dependencies </b></h3> 

- check_overlap() and book() require being passed an existing_appointments list. I did not invent this. 

<h3><b> Error Handling </b></h3>

- No try and catch. Just basic error handling found using "if patient is None:" and things like that. Exactly like how I implemented in my code because I'm lazy. 

<h1><b> F - Manual Behaviour Checks </b></h1>
<p><i> Create valid objects, test invalid input, cancel a scheduled appointment and attempt an illegal repeated transition. </i></p> 



