import random
import logging

def input_int(
    msg: str, 
    min: int = None, 
    max: int = None,
) -> int:
    '''
    Берет на ввод у пользователя число с дальнейшей проверкой.
    Параметры:
    msg - Сообщение подающееся на ввод пользователю.
    min - Минимальное значение на ввод.
    max - Максимальное значение на ввод.
    Возврат:
    Корректно введенное число.
    '''
    while True:
        try:
            logging.info(msg)
            num = int(input(msg))
            logging.info('Пользователь ввел: ' + str(num))
            if min != None and num < min or max != None and num > max:
                min_msg = '' if min == None else f' от {min}'
                max_msg = '' if max == None else f' до {max}'
                print(f'Ошибка: нужно ввести число{min_msg}{max_msg}!')
                logging.error(f'Ошибка: нужно ввести число{min_msg}{max_msg}!')
                continue
            logging.info('Корректное значение введенное пользователем: ' + str(num))
            return num
        except:
            logging.error('Ошибка: нужно ввести число!', exc_info=True)
            print('Ошибка: нужно ввести число!')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename="logfile.log", filemode="a",
                            format="%(asctime)s %(levelname)s %(message)s")

    #Берет на ввод у пользователя 2 числа: число для угадывания и кол-во попыток
    right = random.randint(1, input_int("Введите максимальное число для загадывания: ", 1))
    tries = input_int("Введите число попыток для отгадывания числа: ", 1)

    #Пока у пользователя есть попытки, он угадывает
    while tries:

        guess = input_int("Угадайте загаданное число: ")

        #Проверка на угаданное число
        if guess == right: 
            print("Вы угадали! Это число", right)
            logging.info("Вы угадали! Это число" + str(right))
            break
        
        #Вычет попыток
        tries -= 1
        
        if not tries: 
            print("Попытки закончились, вы не угадали число, правильный ответ:", right) 
            logging.info("Попытки закончились, вы не угадали число, правильный ответ:" + str(right))
            break
        
        #Подсказка
        if guess > right: 
            print("Попробуйте число меньше") 
            logging.info("Попробуйте число меньше")
        else: 
            print("Попробуйте число больше")
            logging.info("Попробуйте число больше")