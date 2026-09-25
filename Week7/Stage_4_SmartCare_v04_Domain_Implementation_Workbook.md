# SmartCare v0.4 - Domain Implementation Workbook

<h1><b> 1. UML-to-Code Trace </b></h1>

<h3><b> UML Element </b></h3>

1. Patient - attributes
2. Patient - editPatient()
3. Patient - addPatient() / searchPatient()
4. Practitioner - attributes
5. Pracitioner - register() / viewSchedule()
6. Appointment - attributes
7. Appointment - book(), cancel(), updateStatus(), checkOverlap()
8. Associations: Patient 1 - 0..* Appointment, Practitioner 1 - 0..* APpointment 

<h3><b> Python Element </b></h3>

1. patient_id, name, dob, contact
2. edit_patient()
3. not implemented
4. practitioner_id, name, specialty
5. not implemented
6. appointment_id, date, time_slot, status
7. all four methods
8. self.patient, self.practitioner on Appointment 

<h3><b> Implemented? </b></h3>

1. Yes 
2. Yes
3. No
4. Partial
5. No
6. Yes
7. Yes
8. Partial 

<h3><b> Notes </b></h3>

1. None 
2. None
3. Need a patient collection to add/serach into.
4. None
5. register() is handeled by the constructor. viewSchedule() needs an appointment collection that doesn't exist.
6. status is a proper AppointmentStatus enum.
7. book() / checkOverlap() take existing_appointments as a parameter. A necessary addition not shown on the diagram. 
8. Navigable only from Appointment outward. 

<h1><b> 2. Domain Invariants </b></h1> 

<h3><b> Class </b></h3>

1. Patient
2. Practitioner
3. Appointment

<h3><b> Invariant / Rule </b></h3> 

1. patient_id, name, dob, contact must all be non-empty; dob must be a real date
1b. name/contact cannot be overwritten with an empty value
2. practitioner_id, name, specialty must all be non-empty
3. appoinment_id, patient, practitioner, appt_date, time_slot must all be present and correctly typed.
3b. A practitioner cannot hold two active (non-cancelled) appointments at the same date and time slot. 

<h3><b> How Protected </b></h3>

1. _require() raises ValueError before the object can be created. 
1b. check_overlap() scans existing appointments; book() blocks the booking if a conflict is found. 
2. Constructor validation, same pattern as Patient. 
3. Constructor validation. An Appointment cannot be built without a valid patient, practitioner, date, and time slot linked. 
3b. check_overlap() scans the supplied appointment list and book() raises AppointmentError if a conflict is found, enforced before hte booking is confirmed, not after. 

<h1><b> 3. Composition / Inheritance Decisions </b></h1>

<h3><b> Relationship </b></h3>

1. Patient - Appointment
2. Practitioner - Appointment
3. Appointment - Patient/Practitioner
4. Manager/Controller classes
5. AppointmentStatus - Appointment

<h3><b> Decision </b></h3>

1. Association (not composition, not inheritance)
2. Association
3. No inheritance
4. No composition
5. Composition-like (Appointment status), implemented as a plain attribute, not a class. 

<h3><b> Rationale </b></h3>

1. Both are independant objects with their own identity and lifecycle. An appointment references a Patient, but neither owns the other's existence. 
2. Same logic as above. A practitioner isn't destroyed or altered by an appointment's lifecycle, and vice versa. They simply reference each other. 
3. Inheritance would mean "Appointment is a Patient," which is conceptually wrong. An appointment is a booking event, not a kind of person. This was explicitly checked and rejected back in Part B. 
4. These were AI-suggested wrapper classes with no supporting requirement. 
5. Status is a simple value with a fixed set of options. Modelling it as an Enum rather than a separate class avoids unnecessary object overhead while still constraining it to valid values. 

<h1><b> 4. AI Pair-Programming Record </b></h1>

<h3><b> AI contribution </b></h3>

1. Apppointment class - attributes, constructor validation, type hints
2. AppointmentStatus enum
3. AppointmentError exception (single class for both violations)
4. book() / check_overlap() taking existing_appointment as a parameter
5. Cancelled appointments excluded from overlap checks
6. Redundant self.status = SCHEDULED inside book() 
7. AppointmentManager/ ScheduleEngine / ClinicController / NotificationManager
8. Receptionist/Staff class with login/auth attributes

<h3><b> Conforms? </b></h3>

1. Yes
2. Yes
3. Yes
4. Partially 
5. Partially 
6. No 
7. No
8. No

<h3><b> Decisions </b></h3>

1. Accepted
2. Accepted
3. Accepted
4. Accepted with a flag
5. Accepted with a flag
6. Rejected/removed
7. Rejected
8. Rejected

<h3><b> Reason </b></h3>

1. Matches approved UML attribute list exactly. 
2. Diagram specifies status: enum; four values match. 
3. Prompt specified one "agreed... exception," keeping the exception surface minimal
4. Necessary since neither Patient nor Practitioner store their own appointment list. Not on the UML, but require to make FR-06 actually runnable. 
5. Not stated in any FR, but follows logically from FR-09. A cancelled slot isn't an active booking
6. Status is already set to SCHEDULED by the constructor. This line was dead code implying book() changes state it doesn't. 
7. Brief never mentions user accounts or authentication. Same category of overreach as "facial recognition login"
8. Identified as a real gap. Status can be set directly, bypassing update_status()'s validation. But full encapsulation wasn't in scope for this phase. 

<h3><b> Verification </b></h3>

1. Part H consistency check. All attributes traced to diagram 
2. Manual checks confirm status transitions work as enum values
3. Manual checks confirm it's correctly raised for both overlap and invalid transition
4. Noted as a legitimate, non-invented dependency in Part E's review. 
5. Flagged as an inferred rule in the engineering log, not traceable to a requirement ID
6. Removed in Part G refactor; re-ran manual checks, output unchanged
7. Never implemented. Excluded explicitly in Part E's AI Model Critique 
8. Never implemented. Confirmed absent in Part A's re-confirmation of approved UML.

<h1><b> Updated UML </b></h3>

<h3><b> Patient </b></h3>

- patientId: string
- name: string
- dob: date
- contact: string

+addPatient()
+editPatient()
+searchPatient()

<h3><b> Practitioner </b></h3>

- practitionerId: string
- name: string
- specialty: string

+ register()
+ viewSchedule()

<h3><b> Appointment </b></h3>

- appointmentId: string
- date: date
- timeSlot: string
- status: AppointmentStatus 

+ book(existingAppointments)
+ cancel()
+ updateStatus(newStatus)
+ checkOverlap(existingAppointments)



