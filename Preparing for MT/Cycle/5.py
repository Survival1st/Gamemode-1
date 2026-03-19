amount = int(input("Введите сумму: "))
banknotes = [5000, 2000, 1000, 500, 100]
total_count = 0

for note in banknotes:
    count = amount // note      
    if count > 0:           
        print(f"{note} x {count}")
        total_count += count    
    amount %= note              

print(f"Итого купюр: {total_count}")