import threading
lock = threading.Lock()
x = 0

def add():
    global x
    lock.acquire()
    for i in range(100000):
        x += 1
    lock.release()

def subtract():
    global x
    lock.acquire()
    for i in range(100000):
        x -= 1
    lock.release()

if __name__ == "__main__":
    t1 = threading.Thread(target=add, name="Thread1")
    t2 = threading.Thread(target=subtract, name="Thread2")
    t3 = threading.Thread(target=add, name="Thread3")
    t4 = threading.Thread(target=subtract, name="Thread4")
    # We are expecting that x's value will be 0.
    # Because one thread add 100000 times and the other subtract the same amount
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    # But actually result sometimes isn't 0 because of race condition
    # for example t1 adds x to 1 but before it reflect to x t2 can take
    # x's old value and subtract it. So normally it shoul be x+1-1 = x
    # but in race condition it can be x-1 because t2 subtract before +1 reflected
    t1.join()
    t2.join()
    t3.join()
    t4.join()

    # But if we use lock than every thread will look if the lock is open or not
    # Only one thread can change x's value. When one thread want to change the value
    # it will close the lock so no other thread can change value
    # after changing the value thread will open the lock and another thread can change the value

    print(x)
