import re

def check_password_strength(password):
    #Score
    score = 0

    #check length of password
    if len(password) >= 8:
        score += 1
    else:
        print("Password is too short, must be at least 8 characters")
    
    #check for uppercase letter
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        print("password must contain an uppercase letter")
    
    #check for lowercase letter
    if re.search(r'[a-z]', password):
        score += 1
    else:
        print("password must contain a lowercase letter")
    
    #check for number
    if re.search(r'\d', password):
        score += 1
    else:
        print("password must contain a number")
    
    #check for special character
    if re.search(r'[!@#$%^&*(),./<>?-_=+\|{}]', password):
        score += 1
    else:
        print("password must contain a special character")

    #Sum of Score
    if score == 5:
        print("Your password is very strong")
    else:
        print("Password is not strong enough.")
    
    return score

if __name__ == "__main__":
    #password input
    password = input("Enter your new password to check strength: ")
    #Password Strength
    check_password_strength(password)
