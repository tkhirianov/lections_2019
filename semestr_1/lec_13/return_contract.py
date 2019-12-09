from contracts import contract

@contract(returns='int,>=0')
def f(x):
    return x
