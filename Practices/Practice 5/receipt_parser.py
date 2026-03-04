# First example
import re

text = "The Cat sat on the mat with another cat."
matches = re.findall(r"[Cc]at", text)

print(matches) 
# Output: ['Cat', 'cat']

# Second example
import re

contact_info = "Reach me at 555-123-4567 or the office at 800-555-9999."
phone_numbers = re.findall(r"\d{3}-\d{3}-\d{4}", contact_info)

print(phone_numbers)
# Output: ['555-123-4567', '800-555-9999']

# Third example
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(pattern, email):
        return "Valid Email"
    else:
        return "Invalid Email"

print(validate_email("hello.world@service.com")) # Valid
print(validate_email("bad-email@com"))           # Invalid

# Fourth example
import re

txt = "10 cats, 20 dogs, 30 birds"
x = re.findall("\d+", txt)
print(x)

# Fifth example
import re

txt = "The sun is shining in the sky"
x = re.findall("s[h|i]", txt)
print(x)

# Sixth example
import re

txt = "apple, orange, banana, cherry"
x = re.split(", ", txt)
print(x)

# Seventh example
import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

# Eighth example
import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

# Ninth example
import re

txt = "Python,Java;C++;Ruby"
x = re.split("[,;]", txt)
print(x)

# Tenth example
import re

txt = "Step1Wait2Finish3Done"
x = re.split("\d", txt)
print(x)

# Eleventh example
import re

txt = "apple orange banana cherry"
x = re.split("\s", txt, 2)
print(x)

# Twelfth example
import re

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)

# Thirteenth example
import re

txt = "My password is 12345"
x = re.sub("\d", "*", txt)
print(x)


# Fourteenth example
import re

txt = "Apple,Orange;Banana.Cherry"
x = re.sub("[,;.]", " ", txt)
print(x)

# Fifteenth example
import re

txt = "The rain in Spain stays mainly in the plain"
x = re.sub("\s", "_", txt, 2)
print(x)
# Output: The_rain_in Spain stays mainly in the plain

# Sixteenth example
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

# Seventeenth example
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

# Eighteenth example
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())

# Nineteenth example
import re

txt = "The cost is 50 dollars, and the tax is 5 dollars."
x = re.findall("\d+", txt)

print(x)
# Output: ['50', '5']

# Twentieth example
import re

txt = "John: 25, Marie: 30, Luke: 21"
# Capture the name (letters) and the age (digits) separately
x = re.findall("([a-zA-Z]+): (\d+)", txt)

print(x)
# Output: [('John', '25'), ('Marie', '30'), ('Luke', '21')]

# Twenty-first example
import re

txt = "The rain in Spain"
x = re.match("The", txt)

if x:
  print("Match found!")
else:
  print("No match")
# Output: Match found!

# Twenty-second example
import re

txt = "The rain in Spain"
# Looking for "Spain"
x = re.match("Spain", txt)

print(x)
# Output: None