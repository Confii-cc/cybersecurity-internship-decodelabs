 # Password Strength Checker
password = input("Enter your password: ")

symbols = "!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/`~"

# Check each character
has_upper = any(char.isupper() for char in password)
has_number = any(char.isdigit() for char in password)
has_symbol = any(char in symbols for char in password)

length = len(password)

# Determine strength
if length < 8:
    strength = "Weak"
elif length >= 8 and has_upper and has_number and has_symbol:
    strength = "Strong"
else:
    strength = "Medium"

#suggestion
suggestions = []

if length < 8:
    suggestions.append("Make your password at least 8 characters long")
if not has_upper:
    suggestions.append("Add uppercase")   
if not has_number:
    suggestions.append("Add at least one digit")   
if not has_symbol:
    suggestions.append("Add special character")   

#determine suggestion
if suggestions:
    print ("Suggestions to improve your password:")
    for tip in suggestions:
        print("-", tip)

print("\nPassword Strength:", strength)
