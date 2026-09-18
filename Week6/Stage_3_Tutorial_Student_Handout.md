# Assignment 2 - Case Study Stage 3 Tutorial Activities From Requirements to Domain Models

<h1><b> Candidate Concepts </b></h1> 

<h3><b> Candidate </b></h3>

1. Patient 
2. Practitioner
3. Appointment 
4. Name
5. Clinic
6. Database
7. Cancellation
8. Status 

<h3><b> Class? </b></h3> 

1. Yes
2. Yes
3. Yes
4. No
5. No
6. No
7. No
8. No

<h3><b> Reason </b></h3>

1. Has its own identity (patientId), and holds state (name, dob, contact). Yes of course we need the Patient as a candidate. 
2. Same pattern. It has identity, availability, and it's own behaviour (register, view schedule). Of course the practitioner is going to be a candidate. 
3. Has identity, state (status), and behaviour (book, cancel, check overlap). Yes of course we need the appointment as a candidate.
4. Just a piece of data belonging to another object. 
5. Never appreas as something the system creates, stores, or manages a list of. 
6. No. This is implementation/infrastructure, not a domain concept. 
7. Not a separate object. It is a state transition on Appointment. 
8. This is an attribute. 

<h1><b> CRC Cards </b></h1>

<p><b> I just copy and pasted everything from the previous document. </b></p>

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

<h1><b> Relationship Reasoning </b></h1>

<p><i> Patient to Appointment: which relationship and why? </i></p>

<p><b> Association </b> because a patient and an appointment are two independent things tha reference each other. </p>

<p><i> Practitioner to Appointment: what multiplicity? </i></p>

<p><b> 1 to 0..* </b> Each appointment links to exactly one practitioner, but a practitioner can have no appointments yet, or many over time. 

<p><i> Should Appointment inherit from Patient? </i></p>

<p><b> No. </b> An Appointment would have to be a kind of Patient, which doesn't make sense; they're difference concepts entirely. 

<p><i> Does Clinic need to own every object? </i></p>

<p><b> No. </b> I don't even know what this means because there is no Clinic class. How is the clinic going to own every object?

<h1><b> AI Model Critique </b></h1>
<p><i> Critique AI proposals: PatientManager, PractitionerManager, AppointmentManager, ClinicController, NotificationManager, ScheduleEngine. </i></p>

<p><b> AI Proposal </b></p>

1. PatientManager
2. PractitionerManager
3. AppointmentManager
4. ClinicController
5. NotificationManager
6. ScheduleEngine

<p><b> Critique </b></p>

1. Unsupported as a separate class. I think it wants add_patient(), edit_patient(), search_patient() under PatientManager but that duplicates the responsibility from Patient. 
2. Same reason as PatientManager. Practitioner already owns register() and view_schedule(). This could just be an issue on my part and the program is susceptible to change, but as of now, this is unsupported.
3. Same pattern again. Not going to expand on this. 
4. Unsupported because we don't even have clinic as a modelled entity. Maybe i'm supposed to have this, but as of now, this remains unsupported.
5. Unsupported. Didn't even have the idea of having any sort of SMS reminders so this remains unsupported.
6. Unsupported. Probably the closest one to being considered, but we already have something like that within Practitioner.check_overlap() and stuff like that so we don't really need this one. 

