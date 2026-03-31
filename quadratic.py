# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminante = b**2 - 4 * a * c #la raiz en la discriminante RAICES
    if discriminante < 0:
        return "()"
    elif discriminante == 0:
        r = -b / (2*a)
        return f"({r})"
    else:
        r1 = (-b + discriminante**0.5) / (2*a)
        r2 = (-b - discriminante**0.5) / (2*a)
        return f"({r1}, {r2})"

def value_y(a, b, c, x):
    return a * x**2 + b * x + c #aX2 + bX + c = 0


def to_string(a, b, c):
    return f"f(x) = {a} * X^2 + {b} * X + {c}" #"f(x) = A * X^2 + B * X + C"


def derivation(a, b, c):
    return f"f(x) = 2 * {a} * X + {b}"
