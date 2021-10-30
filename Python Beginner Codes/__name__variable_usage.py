'''
__name__ variable is created first when we run a file by python interpreter.
"__main__" string assigned to __name__ variable if our scripted file executed.
file's name assigned to __name__ variable if our scripted file imported as a module
to another file.

Python interpreter first runs the imported file, then it run the current file.
'''
import one #Interpreter first run one.py but __name__ variable of one.py will be "one"
import two

if __name__ == "__main__":
    one.func_one()
    two.func_two()
else:
    print("__name__variable_usage.py file is imported")