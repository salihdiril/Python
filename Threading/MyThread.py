# Normally when we want threads to work we use start function
# but in background start function calls run function
# we can override this run function according to object oriented concepts
import threading
import time

class MyThread(threading.Thread):
    # run function runs for every thread. So we can add print statements in run function
    # instead of our main program
    def run(self):
        print("{} has started!".format(self.getName()))
        try:
            if self._target:
                self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs
        print("{} has finished!".format(self.getName()))

def sleeper(n, name):
    print("Hello, I am {}. Going to sleep now.\n".format(name))
    time.sleep(n)
    print("Good morning. {} has woken up".format(name))

if __name__ == "__main__":

    for i in range(3):
        t = MyThread(target=sleeper, name="Thread{}".format(i+1), args=(3,"Thread{}".format(i+1),))
        t.start()

