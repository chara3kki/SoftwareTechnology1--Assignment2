# Assignment 2 - Case Study Stage 4 Tutorial Activities Object-Oriented Design Decisions

<h1><b> Activity 1 - Encapsulation Review </b></h1> 

<h3><b> Class </b></h3>

1. Patient
2. Practitioner
3. Appointment 

<h3><b> Protected state / invariant </b></h3>

1. patient_id, name, dob, contact validated non-empty/correct type at construction; name/ contact re-validated on edit. 
2. practitioner_id, name, specialty validated non-empty at construction. 
3. appointment_id, patient, pracittioner, date, time_slot validated at constructed. Cancelled -> Completed transition blocked in update_status() overlap conflict blocked in book() 

<h3><b> Public Operations </b></h3>

1. __init__, edit_patient()
2. __init__
3. __init__, book(), cancel(), update_status(), check_overlap()

<h1><b> Activity 2 - Composition or Inheritance? </b></h1> 

1. Appointment and Patient = Composition. 
2. Appointment and Practitioner = Composition.
3. Doctor and Practitioner = Association. 
4. Clinic and Appointment = Composition.

<h3><b> Reasoning </b></h3>

1. An Appointment references a Patient. It needs to know hwich patient it's for, but neither object is a specialised version of the other.
2. Same logic. An Appointment links to a Practitioner to know who's running it, but they're independend objects with their own identity and lifecycle. 
3. A Doctor is a Practitioner. A more specific kind of the same concept, likely sharing all of Practitioner's attributes and operations plus extra ones of its own (e.g. the ability to prescribe). 
4. Not inheritance, since an Apppointment clearly isn't a type of Clinic. Composition is arguably the closer fir if Clinic existed as a class. An appointment plausibly can't exist independently of the clinic that hosts it. 

<h1><b> Activity 3 - Responsibility Allocation </b></h1> 

<h3><b> Who decides whether SCHEDULED can become CANCELLED? </b></h3>

Appointment itself, via update_status(). The class that owns the status attribtue is the one that owns the rules about how that attribute can change. In this case there's no restriction blocking SCHEDULED -> CANCELLED. (only CANCELLED -> COMPLETED is blocked), so the method allows it, but the point is the decision-making authority lives inside Appointment, not in whatever code happens to call it. 

<h3><b> Who validates a patient name? </b></h3>

Patient itself, via its constructor (and edit_patient() if the name changes later). This is the same principle: whichever class owns a piece of data is responsible for guarding it, so validation lives at the source, not scattered across every place that happens to create or touch a Patient. 

<h3><b> Should Appointment execute SQL? Why? </b></h3> 

No. Appointment is a domain/business-logic class. Its job is to represent what a valid appointment is and what rules govern it (overlap checking, status transitions). SQL execution is a persistence concern: how data gets saved or loaded, which is a completely different responsibiility. Mixing them would violate seperation of concermns. It's make Appointment harder to test, and harder to reuse. 

<h3><b> Should the UI decide whether a status transition is legal? </b></h3> 

No. If the UI enforced the Cancelled -> Completed rule (e.g. just greying out a button), that logic would need to be duplicated anywhere else the system might trigger a status change. 

<h1><b> Exit question </b></h1>

You can write code that uses class, self, inheritance, and methods everywhere, and still end up with design that works functionally but unoptimised. 

Compilers don't care whether the code is optimised or not, they only care whether or not the code works in the first place, and if it runs then it runs. This is terrible practice when working in a team environment though as it can slow down development and hinder future maintanance. 

