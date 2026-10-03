# Stage 1 Lab - Human vs AI: Building Your First SmartCare Prototype

<h1><b> Part A - Understand the Problem: AI OFF </b></h1>
<p><i> SmartCare needs a small prototype that allows a receptionist to record patient appointments. Each appointment records patient name, practitioner name and appointment time. </i></p>

<h3><b> What data must be stored? </b></h3>

- Appointment information.
- Practitioners and patients.
- Date and time of appointment. 

<h3><b> What functions might be useful? </b></h3>

- Appointment 
- Practitioner 
- Patient 

<h3><b> What could go wrong? </b><h3>

- If the information is stored within the code, it could be really easy to extract personal information for malicious reasons. 

<h3><b> What requirements are unclear? </b></h3> 

- Are databases required within the program? 
- Is a GUI required? 

<h1><b> Part B - Build A Human-Written Prototype: AI OFF </b></h1> 

1. The task1 code is bad because it takes too long to log in the patients into the database. It also just assigns them into variables that aren't reusable so its just inefficient

2. There is no user input in any of them. You have to edit the code to add in the patients. 

3. There is no database, just stores the patients in the code and thats bad for code security [really easy to gain personal information].

4. If there was supposed to be user input in the task1 code, there is no try/catch or error handling in general.

5. The code isn't asynchronous so it just runs top to bottom. It doesn't run when the user prompts it to and that's really bad for applications.

<h1><b> Part C - Use AI as Tutor: AI ON (Use only UC approved GenAI Tool such as Microsoft CoPilot) </b></h1>

<h3><b> 1. What the code does </b></h3> 

<p><i> This part was done using the task1 enhanced </i></p> 

- appointments is a global list that stores every booking. 
- book_appointments(...) checks that the patient name isn't empty (otherwise it raises a ValueError). It then builds a dictionary with the patient, practitioner and time, and appends it to the list. 
- display_appointmetns() prints "No appointments recorded." If the list is empty. Otherwise it loops through the list and prints one line per appointment. 
- The last lines print a welcome message, book two appointments and display them. 

<h3><b> 2. Three limitations </b></h3> 

1. No double-booking check. The same practitioner can be booked at the same time twice. 
2. Weak validation. Only patient_name is checked. The practitioner and time can be empty, and the time is just a free-text string, so "banana" is accepted. A name of "   " (spaces) also passes. 
4. Global state. Appointments live in a module-level list, so they disappear when the program ends and any code can change them. There's also no way to cancel or look up a booking. 

<h3><b> 3. Improvements </b></h3> 

- Before appending, loop through appointments and raise an error if one already has the same practitioner and time.
- Validate all three arguments, and use .strip() so whitespace-only names are rejected. 
- Have book_appointment return the appointment, and pass the list in as a parameter instead of relying on a global. 

<h3><b> 4. Two questions to test you </b></h3> 

1. What happens if you call book_appointment("", "Dr. Roe", "10:00"), and why does the appointment never reach the list? 
2. Why does display_appointments() use return inside the if not appointments: block, and what would print if you removed it? 

<h4><b> My answers </b></h4>

1. It raises ValueError("Patient name cannot be empty"). not patient_name is True for an empty string, so the raise runs and the function stops right there. Nothing is added to the list. 

2. return exits the function early. Without it, "No appointment recorded." would print, and then the for loop would run over an empty list and do nothing. The output would be the same, but hte return makes the intent clear and skips unnecessary work. 

<h1><b> Part D - Generate an Alternative: AI ON </b></h1>
<p><i> Ask AI to create a simple beginner-friendly Python function that stores patient name, practitioner name and appointment time. Explicitly prohibit a database or GUI. </i></p>

```
def store_appointment(patient_name, practitioner_name, appointment_time):
    """Return one appointment as a dictionary."""
    return {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time,
    }


# Example use
appointments = []
appointments.append(store_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM"))

print(appointments)
```

<h1><b> Part E - Compare Human and AI Versions </b></h1> 

<h3> Question </h3>

1. Easy to understand? 
2. Runs successfully? 
3. Uses only required features?
4. Adds assumptions?
5. Handles errors? 
6. Could I explain it?

<h3><b> Human version </b></h3> 

1. Mostly. It has two functions and a global list, so there's more to follow. 
2. Yes it does run successfully 
3. No. It adds display_appointments, an empty-name check and a global list. 
4. Yes. It assumes the patient name is the only required field and that a global list is acceptable. 
5. Partly. It raises ValueError for an empty patient name, but nothing else is checked. 
6. Yes, I can most definitely explain this. 

<h3><b> AI version </b></h3>

1. Yes. It's one short function that returns a dictionary. 
2. Yes.
3. Yes. It's a very simple program that stores only the three details. 
4. Yes, a few. It assumes the caller manages the list, and that the time is a plain string. 
5. No. Any value, including empty strings, is accepted. 
6. Yes. A dictionary, a return and a list is all that is used basically. I can explain this. 

<h1><b> Part F - Verify Behaviour </b></h1>

<p><i> I'm assuming that we verify the behaviour of the AI code? That is what I'm going to proceed with here. </i></p>

<h3><b> Test </b></h3>

1. Normal Appointment
2. Blank patient name
3. Same practitioner and time 
4. patient_name = None
5. appointment_time = None 

<h3><b> Inputs used </b></h3>

1. Alice Smith, Dr. John Doe, 10:00 AM
2. ""
3. Bob Johnson and Carl Lee, both with Dr. Jane Roe at 11:30 AM
4. None 
5. None 

<h3><b> Result </b></h3>

1. Stored correcty as a dictionary 
2. Accepted and stored with an empty patient name [there is no error raised...]
3. Both stored [Double booking not detected...]
4. Accepted and stored [Fail, no error raised sadly...] 
5. Accepted and stored [Fail, no error raised again sadly...] 

<h1><b> Part G - Improve One Thing </b></h1> 

- Reject blank or missing patient name in store_appointment. 

<p> This can be done by writing: </p> 

```
if not patient_name:
    raise ValueError("Patient name can't be empty")
```

<p> This implementation is very simple error handling but it gets the job done </p> 

<h1><b> Part H - Reflection </h1></b> 

<h3><b> What did you build before using AI? </b></h3> 

<p> Just a really simple python program that stores the information of the practitioners and patients. </p>

<h3><b> What did AI help you understand? </b></h3> 

<p> AI helped break down what the code does to a structural level. It also helped me understand the specific types of implementation that I could go about using, and what implementation was the most optimal to achieve a specific goal in mind. </p> 

<h3><b> Did AI make assumptions? </b></h3> 

<p> Yes the AI did make various sorts of assumptions when assisting in creating the programs. That is why it is important for humans to double check the output of the AI to make sure that it isn't "hallucinating".

<h3><b> How did you verify the AI output? </b></h3> 

<p> I verified the AI output by checking similar problems on StackOverflow. It helps me verify whether or not I should trust the AI output. </p>

<h3><b> What engineering work remained for you? </b></h3> 

<p> Planning what types of implementation and how to achieve the goals through code. The AI can replace my coding skills, but it will never replace the management that I undergo when completing this assignment </p>

