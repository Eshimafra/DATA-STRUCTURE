# Project 20: Hostel Attendance Log

import array

# ---------------------------------------
# 1. Integers: Attendance values
attendance_counts = [20, 18, 22, 25, 19, 21, 23]  # Example: students present each day for a week

total_attendance = sum(attendance_counts)
average_attendance = total_attendance / len(attendance_counts)
min_attendance = min(attendance_counts)
max_attendance = max(attendance_counts)

# ---------------------------------------
# 2. Strings: Formatted report with f-strings
report = (
    f"Total attendance over the week: {total_attendance}\n"
    f"Average daily attendance: {average_attendance:.2f}\n"
    f"Minimum attendance in a day: {min_attendance}\n"
    f"Maximum attendance in a day: {max_attendance}\n"
)
print("=== Hostel Attendance Summary ===")
print(report)

# ---------------------------------------
# 3. Booleans: Threshold check with compound condition
threshold = 20
if average_attendance > threshold and max_attendance > 24:
    print("Status: Above Standard")
else:
    print("Status: Below Standard")

# ---------------------------------------
# 4. Lists: Modify and sort attendance log
attendance_log = ['Mon:20', 'Tue:18', 'Wed:22', 'Thu:25', 'Fri:19']

# Add new record for Saturday
attendance_log.append('Sat:21')

# Remove records below 19 (e.g., Tuesday)
attendance_log = [entry for entry in attendance_log if int(entry.split(':')[1]) >= 19]

print("\nAttendance log before sorting:")
print(attendance_log)

# Sort log alphabetically
attendance_log.sort()
print("Attendance log after sorting:")
print(attendance_log)

# ---------------------------------------
# 5. Arrays: Fixed-size numeric subset
attendance_array = array.array('i', attendance_counts[:5])  # first 5 days

array_sum = sum(attendance_array)
list_sum = sum(attendance_counts[:5])

print(f"\nSum using array: {array_sum}")
print(f"Sum using list: {list_sum}")

# ---------------------------------------
# 6. Dictionaries: Records of students
student_records = [
    {'id': 1, 'name': 'Ali', 'value': 5},
    {'id': 2, 'name': 'Zara', 'value': 4},
    {'id': 3, 'name': 'Ahmed', 'value': 6},
    {'id': 4, 'name': 'Sara', 'value': 3},
]

# Update Zara's attendance value
for record in student_records:
    if record['name'] == 'Zara':
        record['value'] = 5

# Delete Sara's record
student_records = [r for r in student_records if r['name'] != 'Sara']

# Compute total of 'value'
total_student_value = sum(r['value'] for r in student_records)

print("\nUpdated Student Records:")
for record in student_records:
    print(record)

print(f"Total individual values: {total_student_value}")
