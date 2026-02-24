# Example 1
def color_palette():
    yield "Red"
    yield "Green"
    yield "Blue"

colors = color_palette()

for color in colors:
    print(color)

# Example 2
def even_numbers(limit):
    n = 0
    while n <= limit:
        yield n
        n += 2

for num in even_numbers(10):
    print(num)

# Example 3
def get_lines(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line

def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line.strip()

def format_logs(error_lines):
    for line in error_lines:
        yield f"LOG_ENTRY: {line}"

log_stream = format_logs(filter_errors(get_lines("server.log")))

for entry in log_stream:
    print(entry)

