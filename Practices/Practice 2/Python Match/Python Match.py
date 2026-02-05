#1 example
status = 404
match status:
    case 200:
        print("Success")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Unknown Status")

#2 example
day = "Saturday"

match day:
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("It's a workday.")
    case _:
        print("Invalid day.")