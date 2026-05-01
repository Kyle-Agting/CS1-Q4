Q2 = float(input(“Q2 Tentative: ”))
Q2 = float(input(“Q2 Tentative: ”))
Q2 = float(input(“Q2 Tentative: ”))
Q2 = float(input(“Q2 Tentative: ”))

# Cumulative Calculations
q1 = Q1 
q2 = (q1 + 2 * Q2) / 3
q3 = (q2 + 2 * Q3) / 3
q4 = (q3 + 2 * Q4) / 3

# Optimized Printing and Status
print("1st Quarter Grade: ", q1)
print("2nd Quarter Grade: ", q2)
print("3rd Quarter Grade: ", q3)
print("4th Quarter Grade: ", q4)

# Adjectival logic for the Final Grade (q4)
if q4 >= 96:
    print("Status: EXCELLENT")
elif q4 >= 84:
    print("Status: VERY GOOD")
elif q4 >= 72:
    print("Status: GOOD")
elif q4 >= 60:
    print("Status: SATISFACTORY")
elif q4 >= 50:
    print("Status: FAIR")
elif q4 >= 40:
    print("Status: FAILED ON CONDITION")
else:
    print("Status: FAILED")

