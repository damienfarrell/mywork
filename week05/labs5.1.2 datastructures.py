import random

queue = []

for x in range(0,10):
    number = random.randint(0,100)
    queue.append(number)

print(f"queue is {queue}")
for y in queue:
    print(f"Current number is {queue[0]} and the queue is {queue[1:]}")
    queue.pop(0)
    print ("the queue is now empty")
