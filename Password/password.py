import re
def check11_password(password):
  if len(pass1) < 8:
    return "Password must be at least 8 characters long."
  if not re.search(r'[A-Z]', pass1) or not re.search(r'[a-z]', pass1):
    return "Error: Password must contain at least one capital letter and one small letter."
  if not re.search(r'[!@#$%^&*(),.?":{}|<>]', pass1):
    return "Password cannot start with a number or special character."
  if pass1 in passwords:
    return "Password is not allowed."
  

passwords = ["A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd", "M!n3r4L^", "T7r$eN8f", "MyStrongPassword123!"]
pass1=input("Enter Password:")
result= check_password(pass1)
if result:
    print(f"Password '{pass1}' is invalid: {result}")
else:
    print(f"Password '{pass1}' is valid.")