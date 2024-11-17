import time

def timed(f, *args, n_iter: int =100) -> float:
    """Считает минимальное время выполнения переданой функции.

    :param f: Переданная функция
    :type f: Функции
    :param *args: Агрументы функции
    :type *args: кортеж
    :param n_iter: кол-во подсчётов
    :type n_iter: int

    :rtype: float
    :return: Минимальное время выполнения переданной функции
    """
    acc: float = float("inf") # бесконечно большое значение
    
    for i in range(n_iter): # подсчёты
        t0: float = time.perf_counter() # время до 
        f(*args)
        t1: float = time.perf_counter() # время после
        acc = min(acc, t1 - t0) # мин время выполнения функции (разность посли и до)
        
    return acc
