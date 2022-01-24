def binary_search(list, item):
    low = 0
    high = len(list) -1
    num_guess = 0
    while low <= high:
        mid = int((low + high) / 2)
        guess = list[mid]
        if guess == item:
            return f"Number {mid} found, found in {num_guess} guesses."
        if guess > item:
            high = mid - 1
        else: 
            low = mid + 1
        num_guess += 1
    
    
list_of_num = [n for n in range(200000)]
print(binary_search(list_of_num, 2))

