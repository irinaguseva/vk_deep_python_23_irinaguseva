import time
import logging


def mean(k):
    if not isinstance(k, int):
        raise TypeError("k должен быть integer")
    if k < 0:
        raise ValueError("k должен быть больше 0")

    def decorator(func):
        times = []

        def wrapper(*args, **kwargs):
            begin_time = time.time()
            res = func(*args, **kwargs)
            end_time = time.time()
            execution_time = end_time - begin_time
            times.append(execution_time)
            if len(times) > k:
                times.pop(0)
            av_time = sum(times) / len(times)
            logging.info(round(execution_time, 1))
            print(f"Среднее время последних {k} вызовов: {av_time} сек")
            return res

        return wrapper

    return decorator
