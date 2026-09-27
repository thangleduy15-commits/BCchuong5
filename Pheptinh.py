def cong(a, b):
    return a + b


def tru(a, b):
    return a - b


def nhan(a, b):
    return a * b


def chia(a, b):
    if b == 0:
        raise ValueError("Không thể chia cho 0")
    return a / b