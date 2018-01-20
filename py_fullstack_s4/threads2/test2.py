
def foo():


    yield 1


    yield 2

def bar():

    yield 3

    next(foo())
    yield 4