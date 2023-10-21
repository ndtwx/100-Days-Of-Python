year = int(input("Enter a Year:"))

if (year%4 == 0):
  print("Leap year")
  if(year%100 == 0):
    print("Leap year")
    if(year%400==0):
      print("Leap year")
else:
    print("Not leap year")