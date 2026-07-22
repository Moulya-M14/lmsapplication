import threading
import time

def square(num):
    print(f"square: {num*num}")
    time.sleep(1)

def cube(num):
    print(f"Cube: {num*num*num}")
    time.sleep(1)

t1 = threading.Thread(target=square, args=(4,))
t2 = threading.Thread(target=cube, args=(4,)) 

t1.start()
print(t1)
t2.start()
print(t2)
t1.join()
t2.join()

print("Done!")