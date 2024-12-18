import queue
import random
Q=queue.Queue(maxsize=10)
for v in range(0,5):
    Q.put((random.random()*100))
print("Queue size:",Q.qsize())
for v in range(0,5):
    print(v,"Value remove from Queue:",Q.get())
print("Queue size:",Q.qsize())
print("Queue is empty",Q.empty())
print("Queue is full:",Q.full())
for v in range(0,10):
    Q.put((random.random()*100))
print("Queue is full:",Q.full())
print("Queue is empty",Q.empty())
for v in range(0,10):
    print(v,"Value remove from Queue:",Q.get())


    
