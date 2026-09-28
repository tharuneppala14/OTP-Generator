import random

print("===== OTP Generator =====")

otp = random.randint(100000, 999999)

print("Your OTP is:", otp)

user_otp = input("Enter the OTP: ")

if user_otp == str(otp):
    print("OTP Verified Successfully!")
else:
    print("Invalid OTP!")
