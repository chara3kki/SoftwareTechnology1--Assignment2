# Assignment 2 - Case Study Lab Stage 2 Lab Activities SmartCare Requirements Engineering

<h1><b> Part A - Client Brief: AI OFF </b></h1>

<p><i>
SmartCare uses spreadsheets and paper records. Staff report duplicate bookings, difficulty finding patient information, 
inconsistent appointment status and limited appointment history. Management wants a small, maintainable patient, 
practitioner and appointment system.
</i></p>

- This is not a question. I am not going to write anything here...

<h1><b> Part B - Stakeholders and Scope: AI OFF </b></h1>

<p><i>
Identify at least four stakeholders. Create In Scope and Out of Scope lists.
Label uncertain features as provisional rather than confirmed.
</i></p>

<h2><b> Stakeholders </b></h2>
- Receptionist <br>
- Practitioners <br> 
- Patients <br>
- Clinic Management 


<h2><b> In Scope </b></h2> 
- Patient record management <br>
- Practitioner record management <br>
- Appointment bookings <br>
- Appointment status <br>
- Appointment history [medical records] 

<h2><b> Out of Scope </b></h2>
- Billing <br>
- Mobile app [definitely should not have this]

<h1><b> Part C - Functional Requirements: AI OFF </b></h1>

<p><i>
Write 8 - 12 numbered functional requirements using FR-01, FR-02 and so on. Each should describe one observale capability. 
</i></p>

<b> FR-01: Patient Add -- </b> The Receptionist must have the ability to add patients into the system with the requirements being a name, date of birth, contact details, and possibly a unique patient ID. 

<b> FR-02: Patient Search -- </b> The system should allow the staff to easily search through the patient lists and practitioners list through a search engine. 

<b> FR-03: Patient Editing -- </b> The system should allow the staff to easily edit a patients details allowing for easy re-scheduling for appointments. 

<b> FR-04: Practitioner Creation -- </b> The system should allow administrators to easily add in practitioners and more join the company. 

<b> FR-05: Bookings -- </b> The receptionist must be able to book patients in for an appointment with a practitioner with ease. It requires a time slot, practitioner and a patient. 

<b> FR-06: Overlap Checker -- </b> The system should automatically check the practitioners timetables and check whether they are busy or not. If there is overlap with the bookings, it will alert the receptionist to sort out the problem.

<b> FR-07: Date Sort -- </b> The system should allow the receptionist to sort through the amount of appointments within a given time frame. 

<b> FR-08: Status -- </b> The system should show the status of the appointment. For example: Completed, Cancelled, Ongoing, and Scheduled. 

<b> FR-09: Appointment Deletion -- </b> The system should allow the receptionist to delete appointments if the patient wants to cancel. 

<h1><b> Part D - Non-Functional Requirements </b></h1> 

<p><i> 
Write 4 - 6 numbered non-functional requirements covering appropriate qualities such as reliability, maintainability, data integrity, or testability. 
</i></p>

<b> NFR-01: Maintainablity -- </b> The code must be written as efficient, simple and clean as possible, allowing for better maintainability of the program. 

<b> NFR-02: Data Integrity -- </b> Unique patient identifiers can help distinguish patients with the same name [especially if their names are really common]. 

<b> NFR-03: Usability -- </b> Everything in the software must be readily available and easy to use. The less clicks the better unless the action is dangerous like deleting patients and things like that. 

