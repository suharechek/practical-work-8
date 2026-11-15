def check_order(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

arrays = [["apple", "banana"], ["zebra", "apple"]]
for i in range(len(arrays)):
    if check_order(arrays[i]):
        print(i+1)
    else:
        print("Отрицательный ответ")
