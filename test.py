
dict = {1: 1,
        2: 2,
        3: 3,
        4: 4}


def simp_func(*args ,**kwargs):
    print(kwargs)

simp_func(d=dict)