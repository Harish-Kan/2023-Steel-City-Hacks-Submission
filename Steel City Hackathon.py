#Dictionary 
patients_name = {}
patients_symptoms = {}
patients_symptoms_start = {}
patients_symptoms_type = {} 
patients_family_history = {}
patients_12_months = {}
patients_perscription_medicine = {}
patients_perscription_medicine_in_the_past = {}
patients_alleriges = {}
patients_military = {}
patients_drugs = {}



#Loop 
print("Patients : Please use this tool appropriately ")
stop = input("Type in '!' to stop asking questions or type in anything else to contiune asking questions. (Press Enter) ")
while "!" not in stop:   
  #Qusetions 
  name = input("What is your name? ")  
  brings_you_in = input("What brings you in today? ")
  patients_name[name] = brings_you_in
###
  symptoms = input("What are your symptoms? ")
  patients_symptoms[name] = symptoms
###
  symptoms_start = input("When did your symptoms start? ")
  patients_symptoms_start[name] = symptoms_start
###
  symptoms_better_or_worse = input("Have your symptoms gotten better or worse? ") 
  patients_symptoms_type[name] = symptoms_better_or_worse
###
  family_history = input("Do you have a family history of this? ")
  patients_family_history[name] = family_history
### 
  past_12_months = input("Have you had any procedures or major illnesses in the past 12 months? ")
  patients_12_months[name] = past_12_months
###
  prescription_medicne = input("What prescription medications, over-the-counter medications, vitamins, and supplements do you take? ")
  patients_perscription_medicine[name] = prescription_medicne
###
  prescription_medicne_in_past = input("Which ones have you been on in the past? ")
  patients_perscription_medicine_in_the_past[name] = prescription_medicne_in_past
###
  allergies = input("What allergies do you have? ")
  patients_alleriges[name] = allergies
###
  military = input("Have you served in the military? ")
  patients_military[name] = military
###
  drugs = input("Do you use any kind of tobacco, illicit drugs or alcohol? ")
  patients_drugs[name] = drugs
###
  #
  stop = input("Type in '!' to stop asking questions. Type in anything else to contiune ").lower()
  #
print("------------------------------------------")

print("Patient Information --> ")
print('1 : ' + str(patients_name)) 
print('2 : ' + str(patients_symptoms))
print('3 : ' + str(patients_symptoms_start))
print('4 : ' + str(patients_symptoms_type))
print('5 : ' + str(patients_family_history))
print('6 : ' + str(patients_12_months))
print('7 : ' + str(patients_perscription_medicine))
print('8 : ' + str(patients_perscription_medicine_in_the_past))
print('9 : ' + str(patients_alleriges))
print('10 : ' + str(patients_military))
print('11 : ' + str(patients_drugs))

print("------------------------------------------")

print("Use this to access patient information -->")

stop_second = input("Type in '!' to stop accessing patient information. (Press Enter) ")

while '!' not in stop_second:
  patients_info = input("What patient's information would you like to pull up? ")
  print('1 : ' + str(patients_name[patients_info]))
  print('2 : ' + str(patients_symptoms[patients_info]))
  print('3 : ' + str(patients_symptoms_start[patients_info]))
  print('4 : ' + str(patients_symptoms_type[patients_info]))
  print('5 : ' + str(patients_family_history[patients_info]))
  print('6 : ' + str(patients_12_months[patients_info]))
  print('7 : ' + str(patients_perscription_medicine[patients_info]))
  print('8 : ' + str(patients_perscription_medicine_in_the_past[patients_info]))
  print('9 : ' + str(patients_alleriges[patients_info]))
  print('10 : ' + str(patients_military[patients_info]))
  print('11 : ' + str(patients_drugs[patients_info]))
  stop_second = input("Type in '!' to stop accessing patient information. (Type in anything else if you which to contiune) ")

print("------------------------------------------")
