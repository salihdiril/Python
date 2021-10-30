import one

def func_two():
    print("Executed func_two() function in one.py")

print("Two.py is executing...")
one.func_one()

if __name__ == "__main__":
    print("two.py is running directly")
else:
    print("two.py is imported to current file")