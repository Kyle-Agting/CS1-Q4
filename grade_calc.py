Q1 = float(input(“Q1 Tentative: ”))
Q2 = float(input(“Q2 Tentative: ”))
Q3 = float(input(“Q3 Tentative: ”))
Q4 = float(input(“Q4 Tentative: ”))

# Cumulative Calculations
quarter_1st = Q1 
quarter_2nd = (quarter_1st + (2 * Q2)) / 3
quarter_3rd = (quarter_2nd + (2 * Q3)) / 3
quarter_4th = (quarter_3rd + (2 * Q4)) / 3

# Optimized Printing and Status
print("1st Quarter Grade: ", quarter_1st)
print("2nd Quarter Grade: ", quarter_2nd)
print("3rd Quarter Grade: ", quarter_3rd)
print("4th Quarter Grade: ", quarter_4th)

# Adjectival logic for the Final Grade (q4)
if quarter_4th >= 96 and quarter_4th == 100:
    print("Status: EXCELLENT")
elif quarter_4th >= 84 and quarter_4th == 95.99:
    print("Status: VERY GOOD")
elif quarter_4th >= 72 and quarter_4th == 83.99:
    print("Status: GOOD")
elif quarter_4th >= 60 and quarter_4th == 71.99:
    print("Status: SATISFACTORY")
elif quarter_4th >= 50 and quarter_4th == 59.99:
    print("Status: FAIR")
elif quarter_4th >= 40 and quarter_4th == 49.99:
    print("Status: FAILED ON CONDITION")
else:
    print("Status: FAILED")

