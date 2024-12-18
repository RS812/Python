age = int(input("Enter your age: "))
if age >= 0 and age <= 12:
  print("Your age group is Child")
elif age >= 13 and age <= 19:
  print("Your age group is Teenager")
elif age >= 20 and age <= 35:
  print("Your age group is Young")
elif age >= 36 and age <= 50:
  print("Your age group is Younger")
else:
  print("Your age group is Senior Citizen")
