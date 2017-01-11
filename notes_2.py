import random


class RandomIterator:
    def __init__(self, iter_list):
        self.__i = -1
        self.iter_list = list(iter_list)
        random.shuffle(self.iter_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i >= len(self.iter_list) - 1:
            raise StopIteration
        else:
            self.__i += 1
            return self.iter_list[self.__i]


class RandomFloatIterator:
    def __init__(self):
        self.__last_value = 2

    def __iter__(self):
        return self

    def __next__(self):
        if self.__last_value < 0.1:
            raise StopIteration
        else:
            while True:
                rand_number = random.random()
                if abs(abs(rand_number) - abs(self.__last_value)) <= 0.4:
                    print("*")
                else:
                    self.__last_value = rand_number
                    return rand_number


def random_float_generator():
    _last_value = 2
    while _last_value > 0.1:
        rand_number = random.random()
        if abs(abs(rand_number) - abs(_last_value)) <= 0.4:
            print("*")
        else:
            _last_value = rand_number
            yield rand_number


def frange(stop, start=None, step=0.1):
    round_no = len(str(step).split(".")[-1])
    if start is None:
        start = 0
    else:
        start, stop = stop, start
    counter = 0
    current_value = start
    while (current_value < stop) if step > 0 else (current_value > stop):
        yield round(current_value, round_no)
        current_value = start + counter * step
        counter += 1

if __name__ == '__main__':
    # l = [i for i in range(4)]
    # z = RandomIterator(l)
    # for i in z:
    #     print(i)
    # print("nowe")
    # q = RandomIterator(l)
    # q.__next__()
    # q.__next__()

    # T = RandomFloatIterator()
    # for i in T:
    #     print(i)



    # for z in random_float_generator():
    #     print(z)
    # q = random_float_generator()
    # q.__next__()
    # q.__next__()
    # q.__next__()
    # q.__next__()

    for i in frange(1, 8, 0.435):
        print(i)