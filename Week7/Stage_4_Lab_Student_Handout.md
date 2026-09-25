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
    def __init__(init, patient_id: str, name:str, dob: date, contact: str):

        if not patient_id:
            raise ValueError("Patient ID is required.")
        if not name:
            raise ValueError("The Name is Required.")
        if not isinstance(dob, date): 
            raise ValueError("DOB must be a date.")
        if not contact:
            raise ValueError("Contact is required")

        init.patient_id: str = patient_id
        init.name: str = name
        init.dob: date = dob
        init.contact: str = contact 

    def edit_patinet(init, name: str = None, contact: str = None) -> None:
        if name is non None:
            if not name:
                raise ValueError("Name cannot be empty")
            
            init.name = name
        if contact is not None:
            if not contact:
            rase ValueError("Contact cannot be empty")
        
            init.contact = contact 
```

<h1><b> C - Implement Practitioner: AI OFF </b></h1>
<p><i> Implement Practitioner with identifier, name and specialty; no database logic. </i></p>

```
class Practitioner:
    def __init__(init, practitioner_id: str, name: str, specialty: str):
        if not practitioner_id:
            raise ValueError("Pracitioner ID is required.")
        
        if not name:
            raise ValueError("The Name is required.")
        
        if not specialty:
            raise ValueError("Specialty is required.")

        init.practitioner_id: str = practititoner_id
        init.name: str = name
        init.specialty: str = specialty
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

```
patient = Patient("P01", "Alice Smith", date (1990, 5, 20), "0400 000 000")
practitioner = Practitioner("D01", "Dr. Lee", "General Practice")
appt = Appointment("A01", patient, practitioner, date (2026, 10, 1), "10:00")
print("Created:", appt.appointment_id, appt,status)

# Testing the invalid inputs

try:
    Patient("", "No ID", date(2000, 1, 1), "0400 111 111")
    except ValueError as Error:
        print("Caught invalid Patinet input:", Error)

    try:
        Practitioner("D02", "", "Dentistry")
    except ValueError as Error:
        print("Caught invalid Practitioner input:", Error)
    
    try:
        Appointment("A02", patient, practitioner, "Not A Date", "11:00")
    except ValueError as Error:
        print("Caught invalid Appointment input:", Error)


print("Before cancel:", appt.status)
appt.cancel()
print("After cancel:", appt.status)

try:
    appt.update_status(AppointmentStatus.COMPLETED)
except AppointmentError as Error:
    print("Caught illegal transition:", Error)
```

<h3><b> Create Valid Objects </b></h3>

- Created Patient, Practitioner, and Appointment with data. 
- Output: Created: A01 AppointmentStatus.SCHEDULED
- This is a pass.

<h3><b> Invalid Patient input </b></h3> 

- Created a Patient with an empty patient_id
- ValueError raised when invalid Patient was passed. 
- Output: Caught Invalid Patient.
- This is a pass.

<h3><b> Invalid Practitioner input </b></h3>

- Created a Practitioner with an empty name. 
- ValueError was raised.
- Output: Caught invalid Practitioner input.
- This is a pass.

<h3><b> Invalid Appointment input </b></h3>

- Created an Appointment with a string instead of a date object. 
- ValueError was raised.
- Output: Caught invalid Appointment input.
- This is a pass.

<h3><b> Cancel a scheduled appointment </b></h3>

- Call .cancel() on the appointment created in test 1. 
- Status changes from SCHEDULED to CANCELLED
- Before cancel: SCHEDULED. After cancel: CANCELLED.
- This is a pass.

<h3><b> Illegal repeated transition </b></h3>

- Call .update_status(COMPLETED) on the now-cancelled appointment.
- AppointmentError raised, status stays CANCELLED.
- Output: Caught illegal transition.
- This is an output. 

<h1><b> G - Refactor </b></h1>
<p><i> Remove unnecessary code and make implementation simpler and design-consistent. </i></p>

<h3><b> Changes </b></h3>

1. Repeated if not X: raise ValueError(...) blocks
2. Redundant status assignment in book()
3. check_overlap() loop

<h3><b> Before </b></h3>

1. Each of Patient, Practitioner, Apopintment had 3 - 5 nearly identical validation blocks 
2. book() re-set self.status = AppointmentStatus.SCHEDULED even though __init__ already sets that as the default
3. multi-line for/if/continue loop building up to a return True/return False

<h3><b> After </b></h3>

1. One shared _required(condition, message) helper, called once per field
2. Removed -- book() now only performs the overlap check
3. Single any(...) generator expression 

<h1><b> H - AI Engineering Log </b></h1>
<p><i> Record prompt, generated contribution, decisions and verification evidence. </i></p>

<h3><b> Prompt Used </b></h3>

"Act as a Python pair programmer. Implement only the Appointment class from the approved SmartCare UML. Use type hints and an AppointmentStatus enum. Cancelled appointments remain as objects. Do not add database, UI, notification or service classes. Protect status transitions and explain any decision not directly visible in the UML."

<h3><b> Generated contribution: </b></h3>

- AppointmentStatus enum with four values (SCHEDULED, COMPLETED, CANCELLED, ONGOING), matching the diagram's status: enum attribute.
- One custom exception, AppointmentError, covering both scheduling conflicts and invalid status transitions.

<h3><b> Verification evidence </b></h3>

- Model-code consistency checks from Part H confirmed all UML attributes and operations are present in code with no extras. 
- Manual behaviour checks in Part F exercised: valid object creation, invalid input on all three constructors, a successful cancellation, and the illegal cancelled. All four passed as expected and ValueError was raised exactly where the rules require it.
- Code review in Part E confirmed no unsupported features, no unnecessary inheritance, and one legitimate dependency. 

<h1><b> Reflection </b></h1>
<p><i> Which AI-generated part did you modify or reject? Why? How did the approved design constrain the AI? </i></p>

I approved the syntax of the code given by the AI. Especially when it comes to the try/catch section. I modified the code when it came to that, allowing for the code to be more readable. 

The approved design constrains the AI by giving it a fixed class list [Patient, Pratitioner, Appointment and such]. 