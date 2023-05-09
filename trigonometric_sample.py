from math import *


def get_number(message):
    while True:
        inp = input(message)
        try:
            return int(inp)
        except ValueError:
            print('Sai định dạng. Vui lòng nhập vào một số!')
            continue


def distance(px1, py1, px2, py2):
    return sqrt((px2 - px1)**2 + (py2 - py1)**2)


def is_triangle(ax, ay, bx, by, cx, cy):
    d1 = distance(ax, ay, bx, by)
    d2 = distance(ax, ay, cx, cy)
    d3 = distance(bx, by, cx, cy)
    return d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1


def compute_degree_from_cosine(cosine):
    rad = acos(cosine)
    deg = degrees(rad)
    return deg


def create_vector(px1, py1, px2, py2):
    return [(px1 - px2), (py1 - py2)]


def compute_angle(px1, py1, px2, py2, px3, py3):
    vector1 = create_vector(px1, py1, px2, py2)
    vector2 = create_vector(px2, py2, px3, py3)
    dividend = abs(vector1[0]*vector2[0] + vector1[1]*vector2[1])
    divisor = sqrt(vector1[0]**2 + vector1[1]**2) * sqrt(vector2[0]**2 + vector2[1]**2)
    if divisor != 0:
        cosine = dividend / divisor
        return compute_degree_from_cosine(cosine)