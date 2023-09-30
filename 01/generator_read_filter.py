import io

def generator(filename, words_to_seek):

    if not isinstance(words_to_seek, list):
        raise TypeError("Ошибка. words_to_seek должен быть списком")

    if not all(isinstance(elem, str) for elem in words_to_seek):
        raise TypeError("Ошибка. words_to_seek должен содержать строки")

    words_to_seek = {word.lower() for word in words_to_seek}

    if isinstance(filename, str):
        with open(filename, "r", encoding="utf-8") as current_file:
            for line in current_file:
                line_unique = {w.lower() for w in line.split()}
                if line_unique.intersection(words_to_seek):
                    yield line.strip()

    elif isinstance(filename, io.StringIO):
        filename.seek(0)
        line = filename.readline()
        while line:
            line_unique = {w.lower() for w in line.split()}
            if line_unique.intersection(words_to_seek):
                yield line.strip()
            line = filename.readline()
    else:
        raise TypeError("Ошибка. filename должен быть типа str или StringIO")
