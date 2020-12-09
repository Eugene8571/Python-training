



def f_plus(a,b):
    """ сложение
    >>> f_plus(1,1) + 1
    2

    """
    return a+b

def multiply(a,b):
    """
    >>> multiply('a',4)
    'aaaaa'
    """
    return a*b


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    # print(f"{f_plus(1,1)=}")
    # help('doctest')

