#1 example
password = "admin"
input_attempt = input()
if password != input_attempt:
    print("No!")

#2 example
age = input()
legal_age = 21
can_buy_alcohol = int(age) >= legal_age
print(f"Can buy alcohol? {can_buy_alcohol}")

#3 example
score = input()
passing_score = 60
is_passed = int(score) >= passing_score
print(f"Exam passed: {is_passed}") 

#4 example
fruit1 = "apple"
fruit2 = "banana"
print(fruit1 < fruit2) 

#5 example
energy = 3
while energy > 0:
    print("Running...")
    energy -= 1

print("I am exhausted.")