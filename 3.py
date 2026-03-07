import re
text = "Сегодня солнце светило сильно, словно сейчас середина лета."
result = re.findall(r'\b[сС]\w+', text)
print(result)
