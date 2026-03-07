import re
pattern = "(\d\d)-(\d\d\d)-(\d\d\d\d)" 
new_pattern = r"\2\1\3"
user = input()
new_user = re.sub(pattern, new_pattern, user)
print(new_user)

# First example

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
