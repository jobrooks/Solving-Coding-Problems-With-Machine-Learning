# Difficulty: 1.7
# Justification: 
# Result: accepted
# Tests passed: 52/52
# Error: none
# Response: 
def compare_aah(patient_aah, doctor_aah):
  """
  Compares the length of "aah" said by the patient and required by the doctor.

  Args:
      patient_aah: String representing the "aah" said by the patient.
      doctor_aah: String representing the "aah" required by the doctor.

  Returns:
      String: "go" if patient's "aah" is sufficient, "no" otherwise.
  """

  # Remove the trailing 'h' from both strings.
  patient_aahs = patient_aah[:-1]
  doctor_aahs = doctor_aah[:-1]

  # Compare the length of "aaah" parts.
  if len(patient_aahs) >= len(doctor_aahs):
    return "go"
  else:
    return "no"

# Get input from the user
patient_aah = input()
doctor_aah = input()

# Call the function and print the result
result = compare_aah(patient_aah, doctor_aah)
print(result)
