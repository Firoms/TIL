'''
Yield
Yield는
'''


def gen_num():
    print("first number")
    yield 1
    print("second number")
    yield 2
    print("third number")
    yield 3


if __name__ == "__main__":    
    gen_num()
    print(type(gen_num()))
    gen = gen_num()
    next(gen)
    next(gen)
    next(gen)