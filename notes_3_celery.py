from queue import Queue
from celerytasks import multiply_line

N = 10

print(">>> sync")
results = Queue()
for i in range(1, N + 1):
    results.put(multiply_line.delay(i, N))

while not results.empty():
    res = results.get()
    print(res.get())
    results.task_done()

print(">>> async/Queue")

results = Queue()
for i in range(1, N + 1):
    results.put(multiply_line.delay(i, N))

while not results.empty():
    res = results.get()
    if res.ready():
        print(res.get())
        results.task_done()
    else:
        results.put(res)

print(">>> async")

results = [multiply_line.delay(i, N) for i in range(1, N + 1)]
while len(results):
    for i, res in enumerate(results):
        if res.ready():
            print(res.get())
            results.pop(i)
