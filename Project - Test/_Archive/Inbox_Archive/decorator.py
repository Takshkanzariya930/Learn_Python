def decorator(f):
    def new_f(*args,**kwargs):
        print("Welcome to my function.")
        f(*args,**kwargs)
        print("Thank you for using.")
    return new_f

@decorator
def hello():
    print("hello world.")

@decorator
def ADD(a,b):
    print(a+b)

hello()
ADD(6,7)

# output:
# Welcome to my function.
# hello world.
# Thank you for using.
# Welcome to my function.
# 13
# Thank you for using.