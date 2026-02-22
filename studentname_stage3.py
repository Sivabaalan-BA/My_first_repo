name = input()
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())

total = mark1 + mark2 + mark3
percentage = (total / 300) * 100

# Grade calculation
if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

# Output
print(name)
print("Total:", total, "/300")
print("Percentage:", percentage, "%")
print("Grade:", grade)

    
    