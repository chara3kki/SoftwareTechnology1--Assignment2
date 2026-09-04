#First program
"""
#task 1
# Create and run a simple Python file with basic input,output statements
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")
# First Appointment
patient1_name = 'Alice Smith'
practitioner1_name = 'Dr. John Doe'
appointment1_time = '2024-07-20 10:00 AM'
print(f"Patient: {patient1_name} | Practitioner: {practitioner1_name} | Time:{appointment1_time}")
# Second Appointment
patient2_name = 'Bob Johnson'
practitioner2_name = 'Dr. Jane Roe'
appointment2_time = '2024-07-20 11:30 AM'
print(f"Patient: {patient2_name} | Practitioner: {practitioner2_name} | Time:{appointment2_time}")
"""

#Second program

#task1enhanced

# Use lists, dictionaries and functions to enhance the Python file
 
appointments = []
 
 
def book_appointment(patient_name, practitioner_name, appointment_time):
    if not patient_name:
        raise ValueError("Patient name cannot be empty")
 
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }
    appointments.append(appointment)
 
 
def display_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
 
    for appointment in appointments:
        print(f"Patient: {appointment['patient']} | "
              f"Practitioner: {appointment['practitioner']} | "
              f"Time: {appointment['time']}")
 
 
print("Welcome to SmartCare: The Clinical Appointment Booking System!")
 
book_appointment('Alice Smith', 'Dr. John Doe', '2024-07-20 10:00 AM')
book_appointment('Bob Johnson', 'Dr. Jane Roe', '2024-07-20 11:30 AM')
 
display_appointments()

# List 5 limitations
# 1. The task1 code is bad because it takes too long to log in the patients into the database. It also just assigns them into variables that aren't reusable so its just inefficient
# 2. There is no user input in any of them. You have to edit the code to add in the patients. 
# 3. There is no database, just stores the patients in the code and thats bad for code security [really easy to gain personal information].
# 4. If there was supposed to be user input in the task1 code, there is no try/catch or error handling in general.
# 5. The code isn't asynchronous so it just runs top to bottom. It doesn't run when the user prompts it to and that's really bad for applications.
