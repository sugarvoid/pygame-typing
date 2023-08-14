# math_func.py 

# TODO: Move to its' own file
def clamp(n, min, max):
    if n < min:
        return min
    elif n > max:
        return max
    else:
        return n