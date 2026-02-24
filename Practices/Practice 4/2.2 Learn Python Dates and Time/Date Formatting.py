# Example 1
from datetime import datetime

now = datetime.now()

print(now.strftime("%Y-%m-%d"))
print(now.strftime("%H:%M:%S"))

# Example 2
from datetime import datetime

dt = datetime(2026, 2, 24, 14, 30)

print(dt.strftime("%A, %B %d, %Y"))
print(dt.strftime("%d/%m/%y"))
print(dt.strftime("%I:%M %p"))

# Example 3
from datetime import datetime
import locale

dt = datetime.now()

print(dt.strftime("%c"))
print(dt.strftime("%x %X"))

try:
    locale.setlocale(locale.LC_TIME, "de_DE")
    print(dt.strftime("%A, %d. %B %Y"))
except locale.Error:
    print("Locale not supported on this system")