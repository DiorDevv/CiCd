def qoshish(a, b):
    return a + b

def ayirish(a, b):
    return a - b

def kopaytirish(a, b):
    return a * b

def bolish(a, b):
    if b == 0:
        raise ValueError("Nolga bo'lib bo'lmaydi!")
    return a / b