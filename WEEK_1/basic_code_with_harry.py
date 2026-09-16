# Decorators in Python | Python Tutorial - Day #59

# def greeet(fx):
#     def mfx(*args, **kwargs):
#         print("GOOD MORNING WILSON")
#         fx()
#         print("GOOD BY WILSON")
#         return mfx

# @greeet
# def hello(self):
#     print('Hello John')

# def add(a,b):
#     print(a+b)

# greeet(add)(1,2)


# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"calling {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper

# @logger
# def greet():
#     print("Hello!")

# greet()
# # calling greet
# # Hello!



# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         print(f"Took {time.time() - start:.4f}s")
#         return result
#     return wrapper

# @timer
# def add(a, b):
#     return a + b

# add(3, 4)

print('---------------------------------------------------------------------')

# def retry(func):
#     def wrapper(*args, **kwargs):
#         for attempt in range(3):
#             try:
#                 return func(*args, **kwargs)  # if works, done
#             except Exception as e:
#                 print(f"attempt {attempt+1} failed: {e}")
#         raise Exception("all 3 attempts failed")
#     return wrapper
# @retry
# def risky():
#     raise ValueError("something broke")

# risky()
# attempt 1 failed: something broke
# attempt 2 failed: something broke
# attempt 3 failed: something broke
# Exception: all 3 attempts failed

print('---------------------------------------------------------------------')


# def logger(func):
#     def wrapper(*args, **kwargs):
#         print(f"calling {func.__name__} | args: {args} | kwargs: {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper

# @logger
# def add(a, b):
#     return a + b

# add(3, 4)
# calling add | args: (3, 4) | kwargs: {}


                                                            # DataLoader


import csv

class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load(self):
        with open(self.filepath, 'r') as f:
            reader = csv.DictReader(f)
            return list(reader)

loader = DataLoader('R:\AI_BOOTCAMP\WEEK_1\data.csv')
data = loader.load()
print(data)

print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')


class Cleaner:
    def __init__(self, data):
        self.data = data

    def clean(self):
        # remove nulls
        no_nulls = [row for row in self.data if all(row.values())]
        # remove duplicates
        seen = []
        for row in no_nulls:
            if row not in seen:
                seen.append(row)
        return seen

cleaner = Cleaner(data)
clean_data = cleaner.clean()
print(clean_data)


print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')
print('---------------------------------------------------------------------')

class Reporter:
    def __init__(self, data):
        self.data = data

    def report(self):
        print(f"Total rows: {len(self.data)}")
        print(f"Columns: {list(self.data[0].keys())}")

reporter = Reporter(clean_data)
reporter.report()