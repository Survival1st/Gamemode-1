def check_list_size(nums, threshold=3):
    if (count := len(nums)) > threshold:
        print(f"List has {count} elements")

numbers = [1, 2, 3, 4, 5]
check_list_size(numbers)

