import threading

def raise_to_pow(base, pow):
    print("Power of given number: {}".format(base**pow))

def find_max(num1, num2):
    if num1 >= num2:
        print("max num: ", num1)
    else:
        print("max num: ", num2)

base = float(input("Enter base number: "))
pow = float(input("Enter exponent: "))
num1 = float(input("Enter num1 for finding max number: "))
num2 = float(input("Enter num2 for finding max number: "))
thread1 = threading.Thread(target=raise_to_pow, args=(base, pow,))
thread2 = threading.Thread(target=find_max, args=(num1, num2))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Done!")