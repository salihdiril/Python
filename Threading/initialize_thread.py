# we need to import threading module and time module
import threading
import time

# if we want to work with threads we need to create a function
# because threads work with functions
def sleeper(n, name):
    print("Hello, I am {}. Goint to sleep now.\n".format(name))
    time.sleep(n)
    print("Good morning. {} has woken up".format(name))

def main():
    # create a thread. This thread run sleeper function. We set its name and give
    # parameters to sleeper function with args list
    t = threading.Thread(target= sleeper, name="Thread1", args=(5, "Thread1", ))

    # run the thread
    t.start()

    # right now there is 2 thread working in this program.
    # Main thread and Thread1. This two threads can work concurrently.
    # Python can switch the threads when one of them wait for I/O bound work
    print("Hello. I am main thread.")
    # There is no need to wait 5 sec for printing this statement because python
    # switch Thread1 to main thread.

    # if we don't want interpreter switch thread1 to main thread we can use
    # join function. join function ensure that main thread don't run until Thread1 finish.
    t.join()
    print("Hello again. This is main thread")

if __name__ == "__main__":
    main()