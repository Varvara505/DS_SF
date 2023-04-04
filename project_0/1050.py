import numpy as np   

def game_core_v3(number: int = 1) -> int:
    count = 0

    a = list(range(1,101))
    low = 0
    high = len(a) - 1
    mid = (low + high) // 2
    
    while a[mid] != number:
        count += 1 
        if number > a[mid]:
            low = mid + 1
        elif number < a[mid]:
            high = mid - 1
        mid = (low + high) // 2
    return(count)

print(game_core_v3())
        
