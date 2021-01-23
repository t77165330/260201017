season = str(input("Enter a season: "))
day = int(input("Enter a day: "))
seasons = ("january","fabruar","march","april","may","june","july","august","september","october","november","december")
if season not in seasons:
  print("Enter a valid season please!")
if season == "march" and day >= 20 or season == "april" or season == "may" or season == "june" and day < 21:
  print("spring")

elif season == "june" and day >= 21 or season == "july" or season == "august" or season == "september" and day <22:
  print("summer")

elif season == "september" and day >= 22 or season == "october" or season == "november" or season == "december" and day <21:
  print("fall")
else:
  print("winter")
  
