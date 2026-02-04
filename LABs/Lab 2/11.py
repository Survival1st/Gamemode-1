def reverse_segment():
    n, l, r = map(int, input().split())
    arr = list(map(int, input().split()))
    left = l - 1
    right = r - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    print(*(arr))
reverse_segment()