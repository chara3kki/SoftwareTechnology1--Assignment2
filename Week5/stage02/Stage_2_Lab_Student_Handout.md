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

<b> NFR-04: Performance -- </b> The system has to run decently, returning search results or appointment lookups under 2 seconds under normal single-clinic usage loads [would be really annoying if it took more seconds on average].

<h1><b> Part E - User Stories and Acceptance Criteria: AI OFF </b></h1>

<p><i>
Write 4 - 6 user stories. For at least three, create Given-When-Then acceptance criteria including one negative or failure scenario. 
</i></p>


<h2><b> User Story 1 </b></h2>
<p><i>
As a receptionist, I want to book an appointment for a patient with a specific practitioner so that the patient's visit is scheduled without conflicting with other bookings. 
</i></p>

<h3><b> Scenario 1 -- Successful Booking </b></h3>

- This is <b> Given </b> when the practitioner has an available time slot on a selected date. <br>
- <b> When </b> staff select the patient, practitioner, date, and time and confirm the booking. <br>
- <b> Then </b> the appointment is saved with status "Scheduled" 

<h3><b> Scenario 2 -- Failure: Double Booking </b></h3>
<b> User Story 1: </b>

- This is <b> Given </b> when a practitioner already has an appointment booked at a selected date a and time. <br>
- <b> When </b> staff attempt to book another appointment for that same practitioner in a way that it interferes with an already existing appointment. <br>
- <b> Then </b> the system rejects the booking and displays an error message.

<h2><b> User Story 2 </b></h2>

<p><i>
As a receptionist, I want to seach for a patient by name or ID allowint me ot quickly find their record instead of searrching paper files.
</i></p>

<h3><b> Scenario 1 - Successful search </b></h3>

- This is <b> Given </b> when a patient record exists in the system.
- <b> When </b> staff enter the patient's name or ID is entered into the search field.
- <b> Then </b> the matching patient record is displayed within 2 seconds. 

<h3><b> Scenario 2 - Failure: No match found </b></h3>

- This is <b> Given </b> when no patient records matches the entered search term.
- <b> When </b> staff submit the search prompt. 
- <b> Then </b> the system displays a "no results found" message instead of an error. 

<h2><b> User Story 3 </b></h2>

<p><i>
As a practitioner, I want to updaate the status of an appointment so that the clinic has an accurate record of what happened.
</p></i>

<h3><b> Scenario 1 - Successful status update </b></h3>

- This is <b> Given </b> when an appointment exists with the status "Scheduled".
- <b> When </b> the practitioner changes the status to "Completed".

<h3><b> Scenario 2 - Failure: Invalid status change </b></h3>

- This is <b> Given </b> when an appointment has already been marked "Cancelled".
- <b> When </b> a practitioner attempts to change its status to "Completed".
- <b> Then </b> the system prevents the change and displays a message saying "cancelled appointments cannot be marked complete".

<h2><b> User Story 4 </b></h2>

<p><i>
As a practitioner, I want to view a patient's appointment history, so that I have context on their previous visits before their next appointment. 
</p></i>

- This is <b> Given </b> has one or more past appointments recorded. 
- <b> When </b> the practitioner opens that patient's record.
- <b> Then </b> a list of past and upcoming appointments is displayed. 

<h1><b> Part F - Ai Requirements Review: AI ON </b></h1>

<p><i>
Prompt: Act as a software requirements reviewer. Review the SmartCare requirements for ambiguity, inconsistency, missing clarification questions and testability. Do NOT invent new client requirements. For every suggestion, state whether it is based on evidence or is only a question/assumption requiring validation. 
</p></i>

- <b> Submitting the AI table because copy and pasting takes up way too much space </b>

![alt text](<Screenshot 2026-09-11 215554.png>)

<h1><b> Part G - VERIFY the Ai Review </b></h1>

<p><i>
Classify each significant AI suggestion as Accepted, Modified, Rejected, or Unverified. Explain the evidence used.
</i></p>

![alt text](<Screenshot 2026-09-11 220057.png>)

<h1><b> Part H - Finalise SmartCare v0.2 </b></h1>

<p><i>
Submit stakeholder analysis, scope, B-12FRs, 4-6 NFRs, 4-6 user stories, acceptance criteria, assumptions/open questions and selected AI review evidence. 
</i><p>

- Isn't this whole thing just the whole MD file that I just wrote? I don't know what to say hahahaa. 

<h1><b> Reflection </b></h1> 

<p><i>
In 150-250 words: What did AI notice that you missed? What did AI invent or overreach on? Which requirements changed after review? Why must requirements have evidence? 
</i></p>

When running the AI review, it caught that I hadn't defined the appointment duration, so FR-06's "overlap" check was technically unenforcable. I'd written a rule without the data needed to evaluate it. It also says that "FR-08 described status as an open list while my own acceptance criteria for User Story 3 treated it as a fixed, closed set."

Where the AI overreached was in supplying numbered I hadn't source from the brief. It was really pushing to have "3 clicks" in the usability target. That is ideal, but it just shows how the AI is overstepping onto my field and interjecting its own ideas into the project. This shows why it's important to check what the AI did carefully to make sure that it doesn't change something. 

<b> I would like to apologise for not following the template for this handout. I didn't know of its existence until I got around to it so I hope you can accept this </b> 



