from time import sleep
from random import random
from threading import Thread
from queue import Queue

data_storage = {}

def count_row(mul_data, s, r):
    while True:
        number = s.get()
        s.task_done()
        if number is None:
            break
        sleep(random()*5)
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
        r.task_done()

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
    no_threads_available = int(size / 2)
    input_data = range(1, size + 1)
    threads = []
    for i in range(no_threads_available):
        threads.append(Thread(target=count_row, args=(input_data, Send, Recieve)))
        threads[-1].start()

    for num in input_data:
        Send.put(num)
    Send.join()

    for i in range(no_threads_available):
        Send.put(None)
    Send.join()

    for thread in threads:
        thread.join()

    print_results(Recieve)
    Recieve.join()

    stop = timeit.default_timer()
    print("Execution Time: {}".format(stop-start))