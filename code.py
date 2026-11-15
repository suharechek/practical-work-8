def check_order(arr):
    if not isinstance(arr, list):
        raise TypeError("Входные данные должны быть массивом (списком)")
    if len(arr) > 100:
        raise ValueError("Размер массива не должен превышать 100 элементов")
    if not all(isinstance(x, str) for x in arr):
        raise TypeError("Все элементы массива должны быть строками")
        
    lower_arr = [x.lower() for x in arr]
    
    for i in range(len(lower_arr) - 1):
        if lower_arr[i] > lower_arr[i+1]:
            return False
    return True

def main(arrays):
    if len(arrays) != 5:
        raise ValueError("Ошибка: необходимо передать ровно 5 массивов")

    found_any = False
    for i in range(5):
        if check_order(arrays[i]):
            print(f"Массив №{i+1} в алфавитном порядке.")
            found_any = True
            
    if not found_any:
        print("-1")
