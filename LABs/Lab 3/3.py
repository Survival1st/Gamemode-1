def solve():
    to_digit = {
        "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
        "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"
    }
    to_word = {v: k for k, v in to_digit.items()}

    s = input().strip()

    operator = ""
    for op in ["+", "-", "*"]:
        if op in s:
            parts = s.split(op)
            operator = op
            break
    
    def str_to_num(text):
        res = ""
        for i in range(0, len(text), 3):
            res += to_digit[text[i:i+3]]
        return int(res)

    def num_to_str(n):
        if n < 0:
            return "-" + "".join(to_word[d] for d in str(abs(n)))
        return "".join(to_word[d] for d in str(n))

    n1 = str_to_num(parts[0])
    n2 = str_to_num(parts[1])

    if operator == "+":
        ans = n1 + n2
    elif operator == "-":
        ans = n1 - n2
    else:
        ans = n1 * n2

    print(num_to_str(ans))

solve()