import re

def password_complexity_checker(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_character_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_character_criteria])

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    feedback = f"Password Strength: {strength}\n"
    if not length_criteria:
        feedback += "- Your password should be at least 8 characters long.\n"
    if not uppercase_criteria:
        feedback += "- Your password should include at least one uppercase letter.\n"
    if not lowercase_criteria:
        feedback += "- Your password should include at least one lowercase letter.\n"
    if not number_criteria:
        feedback += "- Your password should include at least one number.\n"
    if not special_character_criteria:
        feedback += "- Your password should include at least one special character.\n"

    return feedback

password = input("Enter your password: ")
print(password_complexity_checker(password))