def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(make_pair)[0]

def cdr(pair):
    return pair(make_pair)[-1]

def make_pair(a, b):
    return [a, b]

def main():
    print(car(cons(3, 4)))
    print(cdr(cons(3, 4)))

main()