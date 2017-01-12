import os
from time import sleep
from random import random
from multiprocessing import Queue, Process

data_storage = {}

def count_row(mul_data, s, r):
    while True:
        number = s.get()
        if number is None:
            break
        time_to_wait = random()*5
        print("pid {}: waiting {}".format(os.getpid(), time_to_wait))
        sleep(time_to_wait)
        ret_list = []
        for mul in mul_data:
            result = mul * number
            ret_list.append(result)
        data_storage[number] = ret_list
        r.put(ret_list)


def print_results(r):
    data_storage = []
    while not r.empty():
        data_storage.append(r.get())

    print("Not Sorted")
    for row in data_storage:
        print("\t" + " ".join(["{:3}".format(elem) for elem in row]))

    print("Sorted")
    for row in sorted(data_storage):
        print("\t" + " ".join(["{:3}".format(elem) for elem in row]))


if __name__ == '__main__':
    import timeit
    start = timeit.default_timer()

    Send = Queue()
    Recieve = Queue()
    size = 20
    no_processs_available = int(size / 2)
    input_data = range(1, size + 1)
    processs = []
    for i in range(no_processs_available):
        processs.append(Process(target=count_row, args=(input_data, Send, Recieve)))
        processs[-1].start()

    for num in input_data:
        Send.put(num)

    for i in range(no_processs_available):
        Send.put(None)

    for process in processs:
        process.join()

    print_results(Recieve)

    stop = timeit.default_timer()
    print("Execution Time: {}".format(stop-start))
