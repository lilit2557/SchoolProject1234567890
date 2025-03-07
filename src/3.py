def calculate_area(shape):
    if shape == "circle":
        return 3.14 * radius ** 2
    elif shape == "square":
        return length ** 2
    elif shape == "rectangle":
        return length * width
    else:
        raise ValueError("Invalid shape")
