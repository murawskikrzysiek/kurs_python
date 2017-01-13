import gevent
import random
from queue import Queue

from notes_3_threading import print_results

def count_row(pid, mul_data, s, r):
    while True:
        number = s.get()
        s.task_done()

        if number is None:
            break

        time_to_wait = random.random() * 5
        print("pid {}: waiting {}".format(pid, time_to_wait))
        gevent.sleep(time_to_wait)

        ret_list = []
        for mul in mul_data:
            result = mul * number
            ret_list.append(result)
        r.put(ret_list)


if __name__ == '__main__':

    Send = Queue()
    Recieve = Queue()

    size = 20
    no_processs_available = int(size / 2)
    input_data = range(1, size + 1)

    threads = [gevent.spawn(count_row, i, input_data, Send, Recieve)
               for i in range(no_processs_available)]

    for num in input_data:
        Send.put(num)
    for i in range(no_processs_available):
        Send.put(None)

    gevent.joinall(threads)

    Send.join()
    print_results(Recieve)
