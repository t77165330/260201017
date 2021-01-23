GPA = float(input("Enter the GPA: "))
NoL = float(input("Enter the number of lectures: "))

if GPA < 2 and NoL < 47:
  print("Not enough number of lectures and GPA!")
elif GPA < 2 and NoL >= 47:
  print("Not enough GPA!")
elif GPA >= 2 and NoL < 47:
  print("Not enough number of lectures!")
else:
  print("GRADUATED!!!")
 