#Несколько исключений, наша ошибка перебирается из возможных, обозначенных в except
try:
    1 / 0
    print("Zero")
    "42" + 10
    print('Type')
except ZeroDivisionError:
    print("Error div 0")
except TypeError:
    print('TypeError')

# Исключение через базовый класс ошибок, который ловит все типы ошибок
try:
    [1, 2][2]
except Exception as e: # Базовый класс исключений, ловит все
    print("Got Exeption", type(e)) #Определяем тип исключения /// Got Exeption <class 'IndexError'>

# Вызов исключения, при помощи raise
try:
    exc = Exception('spam', 'eggs') # объект исключения
    print(exc)
    raise exc  # вызываем исключение, даже если нет ошибки
except Exception as e:
    print("Got Exceprion", type(e), e.args, type(e.args)) # аргументы, тип попавший в исключение
    #Got Exceprion <class 'Exception'> ('spam', 'eggs') <class 'tuple'>

def fails():
    1 / 0
try:
    fails()
except Exception as e:
    print("Got Exception", type(e), e.args, type(e.args))
    #Got Exception <class 'ZeroDivisionError'> ('division by zero',) <class 'tuple'>