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


# Hàm xác định ba điểm có thể tạo nên một tam giác được không dựa trên các tọa độ (x,y) của ba điểm đó
def is_triangle(ax, ay, bx, by, cx, cy):
    d1 = compute_distance(ax, ay, bx, by)
    d2 = compute_distance(ax, ay, cx, cy)
    d3 = compute_distance(bx, by, cx, cy)
    return d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1


# # Hàm tính độ của góc dựa trên cosine của góc đó
# def compute_degree_from_cosine(cosine):
#     rad = acos(cosine)
#     deg = degrees(rad)
#     return deg


# # Hàm tạo nên một vector dựa trên các tọa độ (x,y) của hai điểm
# def create_vector(ax, ay, bx, by):
#     return [(ax - bx), (ay - by)]


# # Hàm tính độ của góc được tạo nên bởi hai vector
# # Đầu vào là các tọa độ (x,y) của ba điểm.
# def compute_angle(ax, ay, bx, by, cx, cy):
#     vector1 = create_vector(ax, ay, bx, by)
#     vector2 = create_vector(bx, by, cx, cy)
#     # dividend = abs(vector1[0]*vector2[0] + vector1[1]*vector2[1])
#     dividend = vector1[0]*vector2[0] + vector1[1]*vector2[1]
#     divisor = sqrt(vector1[0]**2 + vector1[1]**2) * sqrt(vector2[0]**2 + vector2[1]**2)
#     if divisor != 0:
#         cosine = dividend / divisor
#         return round(compute_degree_from_cosine(cosine))


# Hàm tính độ của một góc trong tam giác
# Đầu vào là các tọa độ (x,y) của ba điểm.
def compute_angle_in_a_triangle(ax, ay, bx, by, cx, cy):
    ang = degrees(atan2(cy - by, cx - bx) - atan2(ay - by, ax - bx))
    ang = ang + 360 if ang < 0 else ang
    return round(360 - ang if ang > 180 else ang, 2)


# Hàm xác định tam giác vuông
# Trong tam giác có 1 góc = 90 độ.
def is_right_triangle(ax, ay, bx, by, cx, cy):
    if is_triangle(ax, ay, bx, by, cx, cy):
        angle_a = compute_angle_in_a_triangle(bx, by, ax, ay, cx, cy)
        angle_b = compute_angle_in_a_triangle(ax, ay, bx, by, cx, cy)
        angle_c = compute_angle_in_a_triangle(ax, ay, cx, cy, bx, by)
        print(f'DEBUG: angle_a: {angle_a}')
        print(f'DEBUG: angle_b: {angle_b}')
        print(f'DEBUG: angle_c: {angle_c}')
        if angle_a == 90:
            return [True, 'A']
        if angle_b == 90:
            return [True, 'B']
        if angle_c == 90:
            return [True, 'B']
    return [False]


# Hàm xác định tam giác tù
# Trong tam giác có 1 góc > 90 độ.
def is_obtuse_triangle(ax, ay, bx, by, cx, cy):
    if is_triangle(ax, ay, bx, by, cx, cy):
        angle_a = compute_angle_in_a_triangle(bx, by, ax, ay, cx, cy)
        angle_b = compute_angle_in_a_triangle(ax, ay, bx, by, cx, cy)
        angle_c = compute_angle_in_a_triangle(ax, ay, cx, cy, bx, by)
        if angle_a > 90:
            return [True, 'A']
        if angle_b > 90:
            return [True, 'B']
        if angle_c > 90:
            return [True, 'B']
    return [False]


# Hàm xác định tam giác cân
# Trong tam giác có 2 cạnh bằng nhau
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
# Tam giác có 3 cạnh bằng nhau hoặc 3 góc bằng 60 độ.
def is_equilateral_triangle(ax, ay, bx, by, cx, cy):
    if is_triangle(ax, ay, bx, by, cx, cy):
        ab = compute_distance(ax, ay, bx, by)
        ac = compute_distance(ax, ay, cx, cy)
        bc = compute_distance(bx, by, cx, cy)
        if ab == ac == bc:
            return [True]
    return [False]


# Hàm xác định tam giác vuông cân
# Đảm bảo cả tiêu chí của tam giác vuông và tam giác cân.
def is_right_and_isosceles_triangle(ax, ay, bx, by, cx, cy):
    right_triangle = is_right_triangle(ax, ay, bx, by, cx, cy)
    isosceles_triangle = is_isosceles_triangle(ax, ay, bx, by, cx, cy)
    print(f'DEBUG: right_triangle[0]: {right_triangle[0]}')
    print(f'DEBUG: isosceles_triangle[0]: {isosceles_triangle[0]}')
    if right_triangle[0] and isosceles_triangle[0]:
        print(f'DEBUG: HERE')
        return [True, right_triangle[1]]
    return [False]


def is_obtuse_and_isosceles_triangle(ax, ay, bx, by, cx, cy):
    obtuse_triangle = is_obtuse_triangle(ax, ay, bx, by, cx, cy)
    isosceles_triangle = is_isosceles_triangle(ax, ay, bx, by, cx, cy)
    if obtuse_triangle[0]:
        print(f'DEBUG: obtuse_triangle[0]: {obtuse_triangle[0]} obtuse_triangle[1]: {obtuse_triangle[1]}')
    else:
        print(f'DEBUG: obtuse_triangle[0]: {obtuse_triangle[0]}')
    if isosceles_triangle[0]:
        print(f'DEBUG: isosceles_triangle[0]: {isosceles_triangle[0]} isosceles_triangle[1]: {isosceles_triangle[1]}')
    else:
        print(f'DEBUG: isosceles_triangle[0]: {isosceles_triangle[0]}')
    if obtuse_triangle[0] and isosceles_triangle[0]:
        return [True, obtuse_triangle[1]]
    return [False]


def is_normal_triangle(ax, ay, bx, by, cx, cy):
    if not is_triangle(ax, ay, bx, by, cx, cy):
        return None
    right_triangle = is_right_triangle(ax, ay, bx, by, cx, cy)
    obtuse_triangle = is_obtuse_triangle(ax, ay, bx, by, cx, cy)
    isosceles_triangle = is_isosceles_triangle(ax, ay, bx, by, cx, cy)
    equilateral_triangle = is_equilateral_triangle(ax, ay, bx, by, cx, cy)
    if right_triangle[0] or obtuse_triangle[0] or isosceles_triangle[0] or equilateral_triangle[0]:
        print(f'DEBUG: right_triangle[0]: {right_triangle[0]}')
        print(f'DEBUG: obtuse_triangle[0]: {obtuse_triangle[0]}')
        print(f'DEBUG: isosceles_triangle[0]: {isosceles_triangle[0]}')
        print(f'DEBUG: equilateral_triangle[0]: {equilateral_triangle[0]}')
        return False
    return True




































