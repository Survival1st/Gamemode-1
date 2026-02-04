#1 example
age = int(input())
has_card = True

if age > 60 and has_card:
    print("You get a discount!")
else:
    print("No discount available.")

#2 example
is_vip = False
has_ticket = True

if is_vip or has_ticket:
    print("Welcome!")
else:
    print("Entry is only to VIP and ticket holders.")

#3 example
bag = ["laptop", "mouse"]
if not bag:
    print("Bag is empty!")
else:
    print("There is something in the bag.")

#4 example
lives = 3
level_complete = False
is_admin = False
if (lives > 0 and not level_complete) or is_admin:
    print("Game continues.")