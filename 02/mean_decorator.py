import time
import logging


def mean(k):
    if not isinstance(k, int):
        raise TypeError("k должен быть integer")
    if k < 0:
        raise ValueError("k должен быть больше 0")

    def decorator(our_function):
        if not callable(our_function):
            raise TypeError("func должен быть callable")
        lst = []

        def wrapper(*args, **kwargs):
            begin_time = time.time()
            res = our_function(*args, **kwargs)
            end_time = time.time()
            time_passed = end_time - begin_time
            lst.append(time_passed)
            if len(lst) > k:
                lst.pop(0)
            time_avrg = sum(lst) / len(lst)
            logging.info(round(time_passed, 1))
            print(f"Среднее время последних {k} вызовов: {time_avrg} секунд")
            return res
        return wrapper
    return decorator
