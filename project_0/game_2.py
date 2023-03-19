"""guess the number. for machine"""

import numpy as np

def random_predict(number:int=1) -> int:
    """guess the number in random 

    Args:
        number (int, optional): guessing number. Defaults to 1.

    Returns:
        int: count of attempts
    """    ''''''
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return (count) 


def score_game(random_predict) -> int:
    """ average count of attempts

    Args:
        random_predict (_type_): function of prediction

    Returns:
        int: average count of attempts
    """
    count_list = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size = (1000))
    
    for number in random_array:
        count_list.append(random_predict(number))
        
    score = int(np.mean(count_list))
    print(f'Your algoritm predict the number in average {score} counts')
    return(score)

if __name__ == '__main__':  
    score_game(random_predict)
        
 