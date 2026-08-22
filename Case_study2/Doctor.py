departments = [ "Cardiology", "Orthopedics", "Neurology", "Dermatology", "Pediatrics","ENT", "General Medicine" ]

available = { "Cardiology", "Neurology", "Orthopedics","Pediatrics" }

emergency = { "Cardiology", "Neurology" }

doctors = [ "Dr. Tanishq", "Dr. Amrit", "Dr. laveena", "Dr. palak", "Dr. kritika", "Dr. Nishchat" ]

doctors_available = {
    "Dr. Tanishq Sharma",
    "Dr. Jay Patel",
    "Dr. Himanshu Verma",
    "Dr. Hardik Gupta"
}

name = input("Enter Patient Name:- ")

print("\n Hospital Departments:-")

for i in range(len(departments)):
    print(i + 1, "-", departments[i])

choice = input("\nEnter department numbers: ")

requested = []

for x in choice.split(","):
    x = x.strip()

    if x != "":
        requested.append(departments[int(x) - 1])

old = input("Enter previously visited department:- ")
visited = []

for x in old.split(","):
    x = x.strip()

    if x != "":
        visited.append(departments[int(x) - 1])

print("\n--- Doctors ---")

for i in range(len(doctors)):
    print(i + 1, "-", doctors[i])

doctor_choice = input("\n Enter preferred doctor numbers:- ")

preferred = []

for x in doctor_choice.split(","):
    x = x.strip()

    if x != "":
        preferred.append(doctors[int(x) - 1])

# List operations
first = preferred[0] if preferred else "None"
top_two = preferred[:2]

new_list = preferred.copy()
new_list.append("Dr. Extra")
new_list.remove("Dr. Extra")

# Finding duplicate requests
duplicate = []
checked = []

for dept in requested:
    if dept in checked:
        if dept not in duplicate:
            duplicate.append(dept)
    else:
        checked.append(dept)

# Converting lists into sets
requested_set = set(requested)
visited_set = set(visited)

# Set operations
available_dept = requested_set.intersection(available)
not_available = requested_set.difference(available)
same_dept = requested_set.intersection(visited_set)
urgent_dept = requested_set.intersection(emergency)

# Finding an available doctor
doctor = "None"

for d in preferred:
    if d in doctors_available:
        doctor = d
        break

# Appointment status
if urgent_dept:
    selected_dept = list(urgent_dept)[0]
    status = "Confirmed - Emergency"

elif same_dept:
    selected_dept = list(same_dept)[0]
    status = "Confirmed - Follow-up"

elif available_dept:
    selected_dept = list(available_dept)[0]
    status = "Confirmed - Regular"

else:
    selected_dept = "None"
    status = "Rejected - Department Not Available"

if "Confirmed" in status and doctor != "None":
    status = status + " with " + doctor

# Final result
print("\n APPOINTMENT REPORT ")
print("Patient Name:", name)
print("Requested Departments:", requested)
print("Available Departments:", list(available_dept))
print("Unavailable Departments:", list(not_available))
print("Duplicate Requests:", duplicate)
print("Common Departments:", list(same_dept))
print("Previously Visited:", visited)
print("Emergency Departments:", list(urgent_dept))
print("First Preferred Doctor:", first)
print("Top 2 Doctors:", top_two)
print("Assigned Doctor:", doctor)
print("Recommended Department:", selected_dept)
print("Final Appointment Status:", status)