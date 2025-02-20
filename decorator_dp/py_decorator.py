import time
import logging
from abc import abstractmethod, ABC

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# manager -- decorator
# 1 code
# 2 func
# 3 code

def dont_run(func):
    def wrapper(): # 1
        # 2
        print('Before ...')

        #func()

        print('After')
    return wrapper # 3

@dont_run
def say_hello():
    print('hello...')

# parameters require extra function
def repeat(n): # 1
    def decorator(func): # 2
        def wrapper(): # 1
            for _ in range(n):
                func()
        return wrapper # 3
    return decorator

@repeat(3)
def print_1_10():
    print("1 2 3 4 5 6 7 8 9 10")

@repeat(2)
def print_1_8():
    print("1 2 3 4 5 6 7 8")

print_1_10()
print_1_8()

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"{func.__name__}  running time is {end_time - start_time:.4f} seconds")
        logging.info(f"{func.__name__}  running time is {end_time - start_time:.4f} seconds")
    return wrapper

@timer
def slow_function():
    time.sleep(0.2)

@timer
def connect_remote_mongo():
    time.sleep(0.3)

slow_function()
connect_remote_mongo()

# create decorator @safe_run
# try-except around the function
#  in the except write error to log file
#  create function div which divides by zero

def safe_run(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"function [{func.__name__}] Error = {e}. args={args}")
            logging.error(f"function [{func.__name__}] Error {e}. args={args}")
    return wrapper

@safe_run
def divide(a, b):
    c = a / b
    return c

print(divide(3, 0))
print(divide(3, 2))

# Aspect Orientation Programming

# a = 5
# b = 1
# expected = 6
# actual = calculator.add(a, b)
# assert actual == expected


