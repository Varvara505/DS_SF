import numpy as np   

def game_core_v3(number: int = 1) -> int:
    count = 0
    predict = np.random.randint(1, 101)
   
    while True:
        count += 1 
        if number != predict:
            
            if number // 10 == 0:
                if number > predict:
                    predict += 10
                elif number < predict:
                    predict -= 10 
  
                   
            if number // 10 != 0 and number // 5 == 0:
                if number > predict:
                    predict += 10
                elif number < predict:
                    predict -= 10  

                
            if number // 5 != 0 and number //2 == 0:
                if number > predict:
                    predict += 2
                elif number < predict:
                    predict -= 2

            
            if number // 5 != 0 and number // 2 == 1:
                if number > predict:
                    predict += 1
                elif number < predict:
                    predict -= 1 
                else:
                    break     
              
    return (count) 
print(game_core_v3())

#def score_game(game_core_v3) -> int:
    #"""За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    #Args:
    #    random_predict ([type]): функция угадывания

    #Returns:
    #    int: среднее количество попыток
    #"""
    #count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    #random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    #for number in random_array:
    #    count_ls.append(game_core_v3(number))

    #score = int(np.mean(count_ls))
    #print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    
    #Run benchmarking to score effectiveness of all algorithms

#score_game(game_core_v3)

