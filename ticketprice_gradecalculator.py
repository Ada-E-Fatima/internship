##------------------------------TICKET PRICE & GRADE CALCULATOR ----------------------------------
# PART 1: Ticket prices
age = int(input("Age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

if age <= 5:
    price = 0
elif age <= 18:
    price = 300
elif age < 30 and is_student:
    price = 500
elif age >= 65:
    price = 200
else:
    price = 800

print(f"Your ticket price is: {price} rupees")

# PART 2: Grade calculator
print("--------------- Welcome to Grade Calculator ---------------")
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")
print("--------------------------- END ---------------------------")