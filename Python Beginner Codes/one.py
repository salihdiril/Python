def func_one():
    print("Executed func_one() function in one.py")

print("One.py is executing...")

if __name__ == "__main__":
    print("one.py is running directly")
else:
    print("one.py is imported to current file")