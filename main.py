Q1 = float(input("Tentative Grade for 1st Quarter:"  ))
Q2 = float(input("Tentative Grade for 2nd Quarter:"  ))
Q3 = float(input("Tentative Grade for 3rd Quarter:"  ))
Q4 = float(input("Tentative Grade for 4th Quarter:"  ))
quarter_1st= Q1
quarter_2nd = quarter_1st + (2 * Q2) / 3
quarter_3rd = quarter_2nd + (2 * Q3) / 3
quarter_4th = quarter_3rd + (2 * Q4) / 3
print("1st Quarter Grade: ", Q1)
print("2nd Quarter Grade: ", Q2)
print("3rd Quarter Grade: ", Q3)
print("4th Quarter Grade: ", Q4)
