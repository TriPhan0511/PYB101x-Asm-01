from math import *


# Hàm nhập một số từ bàn phím
def get_number(message):
    while True:
        inp = input(message)
        try:
            return int(inp)
        except ValueError:
            print('Sai định dạng. Vui lòng nhập vào một số!')
            continue


# Hàm tính khoảng cách giữa hai điểm dựa trên các tọa độ (x,y) của hai điểm đó
def compute_distance(ax, ay, bx, by):
    return round(sqrt((bx - ax) ** 2 + (by - ay) ** 2), 2)


# def compute_distance(ax, ay, bx, by):
#     return sqrt((bx - ax) ** 2 + (by - ay) ** 2)


# Hàm xác định ba điểm có thể tạo nên một tam giác được không dựa trên các tọa độ (x,y) của ba điểm đó
def is_triangle(ax, ay, bx, by, cx, cy):
    d1 = compute_distance(ax, ay, bx, by)
    d2 = compute_distance(ax, ay, cx, cy)
    d3 = compute_distance(bx, by, cx, cy)
    return d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1


# Hàm tính độ của góc dựa trên cosin của góc đó
def compute_degree_from_cosine(cosine):
    rad = acos(cosine)
    deg = degrees(rad)
    return deg


# Hàm tạo nên một vector dựa trên các tọa độ (x,y) của hai điểm
def create_vector(ax, ay, bx, by):
    return [(ax - bx), (ay - by)]


# Hàm tính độ của góc được tạo nên bởi hai vector
# Đầu vào là các tọa độ (x,y) của ba điểm.
def compute_angle(ax, ay, bx, by, cx, cy):
    ang = degrees(atan2(cy - by, cx - bx) - atan2(ay - by, ax - bx))
    ang = ang + 360 if ang < 0 else ang
    return round(360 - ang if ang > 180 else ang, 2)


# def compute_angle(ax, ay, bx, by, cx, cy):
#     vector1 = create_vector(ax, ay, bx, by)
#     vector2 = create_vector(bx, by, cx, cy)
#     # dividend = abs(vector1[0]*vector2[0] + vector1[1]*vector2[1])
#     dividend = vector1[0]*vector2[0] + vector1[1]*vector2[1]
#     divisor = sqrt(vector1[0]**2 + vector1[1]**2) * sqrt(vector2[0]**2 + vector2[1]**2)
#     if divisor != 0:
#         cosine = dividend / divisor
#         return round(compute_degree_from_cosine(cosine))


# Hàm xác định tam giác vuông
def is_right_triangle(ax, ay, bx, by, cx, cy):
    if is_triangle(ax, ay, bx, by, cx, cy):
        angle_a = compute_angle(bx, by, ax, ay, cx, cy)
        angle_b = compute_angle(ax, ay, bx, by, cx, cy)
        angle_c = compute_angle(ax, ay, cx, cy, bx, by)
        if angle_a == 90:
            return [True, 'A']
        if angle_b == 90:
            return [True, 'B']
        if angle_c == 90:
            return [True, 'B']
    return [False]


# Hàm xác định tam giác tù
def is_obtuse_triangle(ax, ay, bx, by, cx, cy):
    if is_triangle(ax, ay, bx, by, cx, cy):
        angle_a = compute_angle(bx, by, ax, ay, cx, cy)
        angle_b = compute_angle(ax, ay, bx, by, cx, cy)
        angle_c = compute_angle(ax, ay, cx, cy, bx, by)
        # print(f'DEBUG: angle A = {angle_a} (degree)')
        # print(f'DEBUG: angle B = {angle_b} (degree)')
        # print(f'DEBUG: angle C = {angle_c} (degree)')
        if angle_a > 90:
            return [True, 'A']
        if angle_b > 90:
            return [True, 'B']
        if angle_c > 90:
            return [True, 'B']
    return [False]


# Hàm xác định tam giác cân
def is_isosceles_triangle(ax, ay, bx, by, cx, cy):
    if is_triangle(ax, ay, bx, by, cx, cy):
        ab = compute_distance(ax, ay, bx, by)
        ac = compute_distance(ax, ay, cx, cy)
        bc = compute_distance(bx, by, cx, cy)
        if ab == ac:
            return [True, 'A']
        if ab == bc:
            return [True, 'B']
        if ac == bc:
            return [True, 'C']
    return [False]


# Hàm xác định tam giác đều
def is_equilateral_triangle(ax, ay, bx, by, cx, cy):
    if is_triangle(ax, ay, bx, by, cx, cy):
        ab = compute_distance(ax, ay, bx, by)
        ac = compute_distance(ax, ay, cx, cy)
        bc = compute_distance(bx, by, cx, cy)
        if ab == ac == bc:
            return True
    return False































