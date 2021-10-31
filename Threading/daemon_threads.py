# Threads won't terminated until they finish their tasks which means functions
# So if the function never ends then thread also won't be terminated
# This is where daemon threads are useful. Daemon threads end when main thread termianted
import threading
import time

total = 5

def task1(name):
    global total
    for i in range(10):
        time.sleep(1)
        total += 1
        print("total augmented by {}".format(name))
    print("Augmentation done")

def task2(name):
    global total
    for i in range(5):
        time.sleep(0.5)
        total += 1
        print("total augmented by {}".format(name))

# This function never ends because of while loop. The condition is always True
def task3():
    global total
    while True:
        if total > 8:
            print("Overload")
            total -= 4
            print("Subtracted 4 from total")
        else:
            time.sleep(1)
            print("Waiting...")

def main():
    t1 = threading.Thread(target=task1, name="Thread1", args=("Thread1",))
    t2 = threading.Thread(target=task2, name="Thread2", args=("Thread2",))
    # By default daemon flag is false. If we want to create daemon thread
    # we should set daemon flag as True
    t3 = threading.Thread(target=task3, name="Limiter", daemon=True)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    # Because of task3 function never ends main thread also never terminated.
    # We should use daemaon thread for limiter thread
    #t3.join() #This join blocks main thread until it finish its task, function.

    print("Total's Value: {}".format(total))

if __name__ == "__main__":
    main()