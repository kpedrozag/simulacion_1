import queue
print("aa")
cola = queue.Queue(1)
print("aa")
cola.put(1, block=False)
try:
    cola.put(2, block=False)
except queue.Full:
    print("Cola llena")
