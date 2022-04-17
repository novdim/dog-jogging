# Задача программы: посчитать сколько раз пробежит собака от одного друга к другому прежде чем они встретятся.

def digit_check(Namber): #функция проверки ввода числа
    while True:
        try:
            namber = int(input(Namber + '\n'))
            return namber
        except ValueError: # Проверка на ошибку неверного формата (введены буквы)
            print('Введенное вам значение не является числом! Введите пожалуйста число!\n')
            continue

friend = 1 # от какого друга побежит собака

firstFriendSpeed = digit_check("Введите скорость первого друга (м/c):")
secondFriendSpeed = digit_check("Введите скорость второго друга (м/c): ")
dogSpeed = digit_check("Введите скорость собаки: ")
distance = digit_check("Введите расстояние между 1 и 2 другом. (м): ")
distanceMeeting = digit_check("Введите расстояние на котором друзья встретятся (м): ")

count = 0 # счетчик кол-ва раз сколько собака пробежит от одного друга до другого

while distance > distanceMeeting: # выполняем цикл пока друзья не встрется
    if friend == 1:
        time = distance / (dogSpeed + secondFriendSpeed) # расчитываем время за которое собака пробежит от одного друга к другому
        friend = 2 # меняем направление собаки
    else:
        time = distance / (dogSpeed + firstFriendSpeed) # расчитываем время за которое собака пробежит от одного друга к другому
        friend = 1 # меняем направление собаки
    distance = distance - time * (firstFriendSpeed + secondFriendSpeed) # расчитываем оставшуюся дистанцию между друзьями
    count = count + 1 # увеличиваем счетчик пробежек на 1
print('Собака ' + str(count) + ' раз(а) пробежит от 1 до 2 друга') 
