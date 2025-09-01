# Example: Check grade based on marks

marks = int(input("Enter your marks: "))

if marks >= 80:
    print("Grade: A+")
elif marks >= 70:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F (Fail)")

print("\n")
# Example: Age category checker

age = int(input("Enter your age: "))

if age < 13:
    print("You are a Child")
elif age < 20:
    print("You are a Teenager")
elif age < 60:
    print("You are an Adult")
else:
    print("You are a Senior Citizen")
