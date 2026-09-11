# Assignment 2 Case Study Stage 2 Tutorial From Problems to Requirements

<h1><b> Activity 1 - Stakeholder Map </b></h1>

- The numbers help match the elements of the table together, because you can't make a table in MD files.

<h3><b> Stakeholders: </b></h3>

1. Receptionists and Clinic Administrator.
2. Practitioners.
3. Patients.
4. Owners and Managers.
5. IT Support [IT field for the software in general]

<h3><b> Need: </b></h3>

1. Fast, reliable booking with no duplicates. 
2. Accurate date schedules and patient history. 
3. Appointments booked correctly. Make sure that the visits are not double-booked or lost [appointment conflicts].
4. Low cost and highly maintainable system. Few erros within the program. 
5. Simple architecture. Easy to maintain and build upon. 

<h3><b> Potential Conflict: </b></h3>

1. If they want a more flexible booking set of rules, it may conflict with strict duplicate-prevention logic. 
2. May want more clinical detail recorded that admin staff are willing to enter [tedious]. 
3. May want direct online booking access. This dramatically increases the scope/complexity of the software and is hard to implement at a low cost. 
4. May want a minimal and cheap build, which conflicts with the patients ideals listed above. 
5. May push back against feature requests because it increases the maintenance burden due to complexity.

<h1><b> Activity 2 - Funcitonal or Non-Functional? </b></h1>

<p><i>
The system shall allow staff to cancel an appointment. </i>: <b> Functional </b>
</p>

<p><i>
The system should remain responsive for the course-scale dataset. </i>: <b> Non-functional </b>

<p><i>
The system shall retain cancelled appointments. </i>: <b> Functional </b>

<p><i>
Core business logic should be independently testable. </i>: <b> Non-functional </b> 

<p><i>
The system shall search for a patient by ID. </i>: <b> Functional </b>

<h1><b> Activity 3 - Repair Ambiguous Requirements </b></h1> 

<h3><i><b> The should be easy to use: </b></i></h3> 

<b> Problem: </b> The statement "easy to use" is subjective. Without any criteria, you cannot check if a program is easy to use or not. 

<b> Clarification question: </b> What specific task and success measure defined "easy". (e.g. least amount of clicks when performing a given task). 

<h3><i><b> Patient search should be fast: </b></i></h3>

<b> Problem: </b> "Fast" has no defined threshold, so it can't be tested/verified. Fast needs to be more specific rather a broad statement.

<b> Clarification question: </b> What is the maximum acceptable response time for a patient search?

<h3><i><b> The system should securely manage data: </b></i></h3>

<b> Problem: </b> Securely is also vague. It doesn't specify which threats the system should be able to defend against or what mechanisms to apply. 

<b> Clarification question: </b> Are there specifc security/compliance requirements (eg. access control, encryption, regulations) that the system must meet? 

<h3><i><b> Appointments should normally be easy to cancel </b></i></h3>

<b> Problem: </b> "Normally" and "easy" are both undefined. Just like with the previous problems, you can't define something as without criteria so this statement is just suggestive. 

<b> Clarification question: </b> Who is authorised to cancel an appointment and what is the criteria for easy? [e.g. easy means less clicks to perform the given task].

<h1><b> Activity 4 - Ai Requirements Audit </b></h1> 
<p><i> Classify each suggestion: Confirmed / Assumption requiring validation / Unsupported / Out of scope. </i></p>

- Numbered list to form a table again. Just like how I implemented it in the previous questions. 

<h3><b> AI Suggestion: </b></h3>

1. Patients receive SMS reminders.

2. Facial recognition login.

3. Receptionists create appointments. 

4. Online payment.

5. Practitioners view schedules. 

6. AI recommends treatments.

7. Cancelled appointments remain in history. 

<h3><b> Classification: </b></h3>

1. Assumption requiring validation.

2. Unsupported.

3. Confirmed.

4. Out of Scope. 

5. Confirmed 

6. Unsupported 

7. Assumption requiring validation

<h3><b> Evidence / Reason </b></h3> 

1. Not mentioned in the brief as a requirement. Good idea but it's unconfirmed. 

2. Nothing in the brief asks for anything like this for security/authentication. Far beyond stated scope.

3. Directly matches brief's description. This is quite literally the purpose of the program. 

4. Brief is only about the bookings. You can't handle the payments on the clinics side, thus out of scope. 

5. Directly stated in the brief. This is a must for the program.

6. Terrible idea and the idea is unsupported by the brief. 

7. Reasonable. Could never hurt to have extra information but this type of information can also be completely useless so it depends on what the client wants. 

<h1><b> Exit Question: </b></h1>

<h3><b> Why is 'AI suggested it' not sufficient evidence for a requirement? </b></h3>

AI's rely heavily on information from the internet and are currently unable to fully comprehend the situation, reflecting patterns rather than understanding what the client and scenario requires. 

It can generate features like facial recognition login or treatment recommendations which sounds cool but are completely out of scope and not in the requirements/brief. 



