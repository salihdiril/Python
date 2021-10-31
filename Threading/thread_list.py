import threading
import time

def sleeper(n, name):
    print("Hello, I am {}. Goint to sleep now.\n".format(name))
    time.sleep(n)
    print("Good morning. {} has woken up".format(name))

# we can see how much it takes to run sleeper function 5 times with threads
def main():
    # set a thread list
    thread_list = []

    # create start variable for calculating how much the program last
    start = time.time()
    # create threads
    for i in range(5):
        t = threading.Thread(target=sleeper, name="Thread{}".format(i+1), args=(3, "Thread{}".format(i+1)))
        thread_list.append(t)
        t.start()

    # we need to wait for each thread
    for i in range(5):
        thread_list[i].join()

    end = time.time()
    print("The program finish run {} seconds with threads".format(end-start))

# Let's look at how much it takes to run sleeper function 5 times without threads
def main2():
    start = time.time()
    for i in range(5):
        sleeper(3, "Thread{}".format(i+1))
    end = time.time()
    print("The program finish run {} seconds without threads".format(end - start))

if __name__ == "__main__":
    main()
    main2()