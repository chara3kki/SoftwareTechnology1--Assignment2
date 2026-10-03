#  SmartCare v0.1 - Initial Engineering Brief and AI Activity Card 

<h1><b> SmartCare Scenario </b></h1>
<p><i> SmartCare Community Clinic currently uses spreadsheets and paper records to manage patients and appointments. The client says: 'We need software to help manage patients, practitioners and appointments.' This is not yet a complete specification. 

<h1><b> Initial Engineering Brief </b></h1>

<h1><b> 1. Problem Summery </b></h1>
<p><i> Write approximately 100 words. </i></p> 

<p> The SmartCare Community Clinic utilises spreadsheets and paper records to manage patients and appointments. This is seriously inefficient and can cause major issues long-term. The "database" is loosely constructed and poses huge security risks. Also doesn't allow for quick access to patient's medical histories and current bookings. Create a software that utilizes a centralized system, enabling staff to efficiently search patients' information, view schedules, and book patients in. Improve the accuracty of information added and make it easier to highlight booking conflicts. 

<h1><b> Initial Stakeholders </b></h1> 

- Match the numbers of "stakeholders" to the numbers of the "possible need".

<h3><b> Stakeholder </b></h3>

1. Patients 
2. Receptionists
3. Doctors 
4. Owner 

<h3><b> Possible need </b></h3>

1. An efficient program that can book and reschedule appointments quickly and safely. 
2. Fast way to check patients in and avoid double-bookings. Assistance in rescheduling appointments. 
3. Reliable access to patients' medical history and schedule. 
4. Reports on the number of patients. 

<h1><b> 3. Initial features </b></h1> 

<h3><b> Feature </b></h3>

1. Booking Patients 
2. Timetable conflicts
3. Booking suggestions 
4. Patient information 

<h3><b> Confirmed or provisional? </b></h3> 

1. Confirmed 
2. Confirmed
3. Provisional
4. Confirmed 

<h3><b> Why? </b></h3>

1. Booking patients is the whole point of the software. 
2. Must know the doctors schedule with the patients to avoid conflicts and assist with booking. 
3. Helps avoid overloading one doctor by assisting receptionist in spreading out the workload. Not essential but can help. 
4. Must know the patient's previous medical history to assist the doctors. 

<h1><b> 4. Questions for the client </b></h1> 

1. What OS do the computers primarily use?
2. How many people on average book in the clinic every month? 
3. Do you have to save the patients information on the database or delete it after session with the doctors is complete? 
4. How many computers are going to be connected to the software at the same time?
5. Are there any other stakeholders that must be able to access the database? 

<h1><b> What we do not yet know </b></h1> 

1. Do we need the software to create documents of the patients nad their appointments?
2. How many doctors are there going to be? 
3. How many patients can a doctor handle in a single day? 
4. How long does a single appointment take on average? 

<h1><b> AI Activity Card - Ask, Check, Explain </b></h1>

<h1><b> Before AI </b></h1>
<p><i> What do I think the code does? What problems can I already identify? </i></p>

The code just prints "Welcome to SmartCare" and such. It stores in the practitioners name and the patients name. It also tells us when the appointment is going to happen. It's a pretty barebones program. 

1. The code is bad because it takes too long to log in the patients into the database. It also just assigns them into variables that aren't reusable to its just inefficient. 
2. There is no user input. You have ot edit the code to add in the patients. 
3. There is no database, just stores the patieents in the code and thats bad for code security [really easy to gain personal information]. 
4. If there was supposed to be user into in the task1 code, there is no try/catch or error handling in general. 
5. The code isn't asynchronous so it just runs top to bottom. It doesn't run when the user prompts it to and that is really bad for applications. 

<h1><b> AI request </b></h1> 

<p><i> Act as a tutor. Explain this code and identify potential problems. Do not provide a complete replacement. Ask me questions that help me reason about the solution. </i></p> 

<h3><b> Suggestion </b></h3> 

1. Use input() to collect at least one patient's name, practitioner and time. 
2. Add a space after Time: in the f-strings 
3. Store appointment times as datetime objects 
4. "Make the code more modular"

<h3><b> Rating </b></h3> 

1. Useful 
2. Useful (minor) 
3. Out of scope 
4. Unclear 

<h3><b> Reasoning </b></h3> 

1. The taks asks for basic input and output, and your code only has output. 
2. It fixes the output formatting: Time: 2024... becomes Time: 2024... 
3. It's valid Python, but Task 1 only needs simple strings.
4. It gives no specific change, and it also goes beyond a basic input/output task. 

<h1><b> Decide </b></h1>

<p><i> For each significant suggestion: Accept / Modify / Reject / Keep unverified. </i></p> 

- Following the reasonings stated in the previous question. 

1. Accept 
2. Accept 
3. Reject 
4. Modify

<h1><b> Explain </b></h1> 

<p><i> Can I explain the final code without reading the AI response? What do I still need to understand? </i></p> 

<p> The code is pretty simple at this stage. Because python syntax is relatively easy to understand. I understand what is happening within the program at this stage. </p> 

