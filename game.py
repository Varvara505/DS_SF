"""guess the number"""

import numpy as np

number = np.random.randint(1, 101) #think about your number

#count of attempts
count = 0

while True:
    count += 1
    predict_number = int(input('Your number in 1 to 100'))
    
    if predict_number < number:
        print('higher')
    
    elif predict_number > number:
        print('lower')
        
    else:
         print(f'winner! the number is {number} in {count} attemts ')
         break 