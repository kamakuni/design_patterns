from functools import partial

addr = lambda x,y: x + y
incrementer = partial(addr, 1)
print(incrementer(1))