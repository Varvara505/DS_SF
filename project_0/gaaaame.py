import numpy as np   

def game_core_v3(number: int = 1) -> int:
    count = 0
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1 
        if 101 > number > 75:
            if number > predict:
                predict += 1
            elif number < predict:
                predict -= 1
                    
        if 76 > number > 50:
            if number > predict:
                predict += 1
            elif number < predict:
                predict -= 1
                    
        if 51 > number > 25:
            if number > predict:
                predict += 1
            elif number < predict:
                predict -= 1
                    
        else:
            if number > predict:
                predict += 1
            elif number < predict:
                predict -= 1
            

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    #Run benchmarking to score effectiveness of all algorithms

score_game(game_core_v3)