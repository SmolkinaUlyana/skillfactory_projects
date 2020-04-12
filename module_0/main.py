def game_core_v3(number):
    count=1
    predict = np.random.randint(1,101)
    
    ls=list(range(1,101))
    
    while number != predict:
        count+=1
        if predict < number:
            ls=list(filter(lambda x: x !=predict, ls[ls.index(predict):]))   
            predict=ls[round(ls.index(max(ls))/2)]
        elif predict > number: 
            ls=list(filter(lambda x: x !=predict,ls[:ls.index(predict)]))
            predict=ls[round(ls.index(max(ls))/2)]        
    return(count) # выход из цикла, если угадали  


      
def score_game(game_core):
    '''«апускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"¬аш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


score_game(game_core_v3)