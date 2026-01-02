def sum(a, b):
    return a + b


def multiply(a, b):
    return a * b


# TODO: example with args and kwargs

def main(a, b):
    print(f'multiplication: {a} * {b} = {multiply(a, b)}')
    print(f'Sum: {a} + {b} = {sum(a, b)}')

if __name__ == '__main__':
    try:
        a, b = '3', 3
        main(a, b)
    except TypeError as err:
        print(err)
        a, b = 3, 3
        main(a, b)