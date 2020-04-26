import logging
# уровни debug, info, warning, error, critical при выборе уровня, будут выводится только нижележащие уровни

# конфигурируем формат вывода лога и его уровень:
logging.basicConfig(format='%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s',
                     level=logging.DEBUG)

logging.debug("Working!")
#lesson3.py[LINE:39]# DEBUG    [2020-04-26 09:37:06,862] Working!
# файл, строка кода,тип логирования, время, текст предупреждения

def fails():
    logging.info("Entered logging")

#Логирование исключений:
def fails2():
    1 / 0
try:
    fails2()
except Exception as e:
    logging.info("Got Exception %s, %s", type(e), e.args, exc_info=e) # exc_info=e - вывод доп. инф
    # вывод лога через %s мы делаем разметку, через запятую далее описываем что вывести
    # logging.info вывод всего лога
    logging.exception('Got Exceprion %s, %s', type(e), e.args) # логирование ошибки logging.exception

logging.error("Working")


# Сокращенный вариант логирование ошибок
def fails3():
    1 / 0
try:
    fails3()
except Exception: #Сокращенный вариант записи без доп. информации
    logging.exception("Got Exception")
logging.error("Working")