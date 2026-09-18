# Assignment 2 - Case Study Stage 3 Lab Activities SmartCare Domain Modelling

<!-- Please change the curriculum. This assignment is such a joke it's not even funny. If you are reading this, why are these things even required. I know you want to see us working on this assignment every week but still, this is so monotonous and repetitive... -->

<h1><b> A - Requirements Review </b></h1>
<p><i> Highlight nouns, verbs and business rules in SmartCare v0.2 </i></p>

<p><b> Nouns: </b></p>

- Patients
- Appointment
- Practitioner
- Time Allocation [for the Appointment]
- Receptionist

<p><b> Verbs: </b></p>

- Booking
- Cancelling the bookings
- Searching patients names and bookings
- Editing the bookings
- Checking if there is overlap for each bookings

<p><b> Business rules: </b></p>

- Bookings must not overlap with an already existing appointment. 
- Cancelled appointments cannot be marked as complete. 

<h1><b> B - Candidate Classes </b></h1>
<p><i> Record candidate concepts, supporting requirements, state and behaviour. </i></p>

<p><b> Candidate Concept and Supporting Requirements: </b></p>

1. Patient: FR-01, FR-02, FR-03, and NFR-02
2. Practitioner: FR-04, and FR-06
3. Receptionist: FR-01, and FR-05
4. Appointment: FR-05, and FR-06

<p><b> Behaviour: </b></p>

1. Add, search, edit, and view appointment history.
2. Create/register and view schedule.
3. Add patient and book appointment. 

<h1><b> C - CRC Cards </b></h1>
<p><i> Create CRC cards for Patient, Practitioner, and Appointment. </i></p> 

<p><b> Collaborators are written inside the square brackets. </b></p>

<h3> Patients [CRC Card]: </h3>

<p><b> Responsibilities: </b></p>

- Store patient details [No one] 
- Allow staff to add a new patient record [Receptionist]
- Allow staff to search/find patient by name or ID [Receptionist]
- Allow staff to edit patient details [Receptionist]
- Provide list of associted appointments [Appointment, Practitioner]

<h3> Practitioner [CRC Card]: </h3>

- Store practitioner details [No one]
- Allow admin/staff to add a new pratitioner [Receptionist]
- Provide current schedule/timetable for viewing [Appointment]
- Check own timetable for overlap when a new booking is requested [Appointment]

<h3> CRC Card: Appointment </h3>

<p><b> Responsibilities </b></p>

- Store appointment details [Patient, Practitioner]
- Track and update status [No one]
- Validate status transitions [No one]
- Check for scheduling conflicts before confirming a booking [Practitioner]
- Support cancellation/deletion while retaining record in history [Patient]
- Supporting sorting/filtering appointments by date range [Receptionist]

<h1><b> D - UML Model </b></h1>
<p><i> Draw classes, attributes, operations, associations, and multiplicities </i></p>

![alt text](<Screenshot 2026-09-18 215928.png>)

<h1><b> E - AI Design Review </b></h1>
<p><i> Ask AI to suggest and relationships using only confirmed requirements; require supporting requirement IDs. </i></p>

<h3><b> Suggested Classes </b></h3>

<p><b> Class </b></p>

1. Patient
2. Practitioner 
3. Appointment 

<p><b> Supporting requirement ID(s) </b></p>

1. FR-01, FR-02, FR-03, NFR-02
2. FR-04, FR-06
3. FR-05, FR-06, FR-08, FR-09, User Story 1, User Story 3

<p><b> Rationale </b></p>

1. Explicitly created, searched, edited; needs unique ID per NFR-02
2. Explicitly created; timetable checked for overlap
3. Booked, checked for overlap, has status, can be deleted/cancelled

<h3><b> Suggested relationships </b></h3>

<p><b> Relationship </b></p>

1. Patient -- Appointment 
2. Practitioner -- Appointment

<p><b> Multiplicity </b></p>

1. 1 to 0..*
2. 1 to 0..*

<p><b> Supporting requirement ID(s) </b></p>

1. FR-05
2. FR-05, FR-06

<p><b> Rationale </b></p>

1. Booking "requires... a patient" as one of the mandatory fields
2. Booking requires a practitioner; overlap check operates per-practitioner

<h1><b> F - Compare and Decide </b></h1>
<p><i> Record at least one accepted, modified and rejected AI suggestion. </i></p>

<p><b> AI Suggestion </b></p>

1. Add Patient, Practitioner, and Appointment as classes, each with a 1 to 0..* association to Appointment
2. Add a separate TimeSlot class associated with Appointment 
3. Add a Receptionist/Staff class with login and authentication attributes

<p><b> Decision </b></p>

1. Accepted
2. Modified
3. Rejected 

<p><b> Evidence/Reasoning </b></p>

1. FR-01, FR-06, FR-08, FR-09, and User stories 1 and 3. The classes and their multiplicities match the brief's own desciption of what a booking requires
2. FR-05/FR-06 mention a time slot as part of a booking, but the brief never specifies it needs its own class
3. Nothing in the brief mentions user accounts, roles, or authentication

<h1><b> G - Python Skeletons </b></h1>
<p><i> Create simple Patient, Practitioner, and Appointment class skeletons. </i></p>

<p><b> Just going to write everything here because I don't have to add a python file. Have fun reading this: </b></p>

``` 
class Patient:
    def __init__(self, patient_id, name, dob, contact):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.contact = contact

    def add_patient(self):
        pass
    
    def edit_patient(self):
        pass
    
    def search_patient(self):
        pass
    
class Practitioner:
def __init__(self, practitioner_id, name, availability):
    self.practitioner_id = practitioner_id
    self.name = name
    self.availability = availability

def register (self):
    pass

def view_schedule(self):
    pass
    
class Appointment:
    def __init__(self, appointment_id, patient, practitioner, date, time_slot, status):
        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date = date
        self.time_slot = time_slot
        self.status = status

    def book(self):
        pass
    
    def update_status(self):
        pass

    def check_overlap(self):
        pass

# Supposed to be a skeleton so the methods are empty
```

<h1><b> H - Consistency Check </b></h1>
<p><i> Check model-code consistency; do not implement full behaviour yet. </i></p>

<p><b> Patient </b></p>

- Nothing to note here. Everything lines up.

<p><b> Practitioner </b></p>

- Nothing to note here. Everything lines up. 

<p><b> Appointment </b></p>

<p><b> UML [Appointment] </b></p>

1. status: enum
2. not on diagram

<p><b> Code [Appointment] </b></p>

1. status
2. patient, practitioner

<p><b> Match? [Appointment] </b></p>

1. Diagram says enum, code stores plain constructor param with no type constraint. Not a mismatch in name, but the coe doesn't yet enforce the fixed set (Scheduled/Completed/Cancelled/Ongoing) the diagram implies
2. Code has these as constructor params (needed to actually link the objects) but they weren't drawn as seperate attraibute rows on the diagram. The diagram represents the link as an association line instead, which is the correct UML convention, so this isn't really an inconsistency, just two validd ways of showing the same relationship

<h1><b> Reflection </b></h1>
<p><i> What modelling decision was hardest? Where did AI over-design? What evidence supported your final choices? </i></p>

The hardest moddeling decision was whether TimeSlot deserved its own class or should just stay as an attribute on Appointment. FR-05 and FR-06 which made a case for promoting it to a fuill class with its own start/end times. But the brief never actually defines an appointment duration. 

Where the AI over-designed was suggesting a Receptionist/Staff class with login and authentication attributes. It's a reasonable thing for a booking system to eventually need, but nothing in the brief mentions user accounts or authentication. 

The evidence behing my final choices was requirement traceability, not plausibility. Every class, attribute and operation in the UML diagram and code skeleton maps back to a specific FR, NFR, or user story ID back in Stage02.
