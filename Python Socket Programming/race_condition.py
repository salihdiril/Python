import threading

# global variable
x = 0

def increment():
    global x
    x += 1

def task():
    #increment 100000 times
    for i in range(100000):
        increment()

def main_task():
    global x
    x = 0
    # create threads
    t1 = threading.Thread(target=task)
    t2 = threading.Thread(target=task)

    # start threads
    t1.start()
    t2.start()

    # wait for threads
    t1.join()
    t2.join()

# We calculate the value of x 10 times to see the race condition.
# Normally we should get 200000 as a result of x because 2 threads use task function
# But because of race condition between thread sometimes we can't get 200000
for i in range(10):
    main_task()
    print("Iteration {0}: Incremented x = {1}".format(i,x))