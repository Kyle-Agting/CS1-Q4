Q1 = float(input("Tentative Grade of first Quarter: "))
Q2 = float(input("Tentative Grade of second  Quarter: "))
Q3 = float(input("Tentative Grade of third Quarter: "))
Q4 = float(input("Tentative Grade of fourth Quarter: "))
quarter_1st = Q1 
quarter_2nd = (quarter_1st + (2 * Q2)) / 3
quarter_3rd = (quarter_2nd + (2 * Q3)) / 3
quarter_4th = (quarter_3rd + (2 * Q4)) / 3
print("1st Quarter Grade: ", quarter_1st)
print("2nd Quarter Grade: ", quarter_2nd)
print("3rd Quarter Grade: ", quarter_3rd)
print("4th Quarter Grade: ", quarter_4th)
rounded_off = round(quarter_4th, 0)
print("Final Grade (Rounded off): ", rounded_off)
if quarter_4th >= 96 or quarter_4th == 100:
    print("Status: EXCELLENT")
elif quarter_4th >= 84 or quarter_4th == 95.99:
    print("Status: VERY GOOD")
elif quarter_4th >= 72 or quarter_4th == 83.99:
    print("Status: GOOD")
elif quarter_4th >= 60 or quarter_4th == 71.99:
    print("Status: SATISFACTORY")
elif quarter_4th >= 50 or quarter_4th == 59.99:
    print("Status: FAIR")
elif quarter_4th >= 40 or quarter_4th == 49.99:
    print("Status: FAILED ON CONDITION")
else:
    print("Status: FAILED")
