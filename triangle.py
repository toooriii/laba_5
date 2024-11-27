def area_T(a,h):
    return a * h / 2

def perimeter_T(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Sides must be positive numbers")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Invalid sides for a triangle")
    return a + b + c