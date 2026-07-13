wage=float(input("Hourly wage:"))
hour=int(input("Hours worked:"))
day=input("Day of the week:")
if day=="Sunday":
    print(f"Daily wages: {wage*hour*2} euros")
else:
    print(f"Daily wages: {wage*hour} euros")
