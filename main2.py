# import math
from math import *


def main():
    print('PYB101x - Assignment 01 (main2.py)')

    # 2. Nhập tọa độ 3 điểm từ bàn phím
    # Sample: # A(16, -2) B(16, -6) C(18, -4)
    ax = get_number('Nhập toạ độ x của điểm A: ')
    ay = get_number('Nhập toạ độ y của điểm A: ')
    bx = get_number('Nhập toạ độ x của điểm B: ')
    by = get_number('Nhập toạ độ y của điểm B: ')
    cx = get_number('Nhập toạ độ x của điểm C: ')
    cy = get_number('Nhập toạ độ y của điểm C: ')
    print(f'Debug: ax = {ax} ay = {ay} bx = {bx} by = {by} cx = {cx} cy = {cy} ')

    # # 3. Tính độ dài các cạnh của tam giác
    # d1 = distance(ax, ay, bx, by)
    # d2 = distance(ax, ay, cx, cy)
    # d3 = distance(bx, by, cx, cy)
    # print(f'Độ dài cạnh AB = {d1} cm.')
    # print(f'Độ dài cạnh AC = {d2} cm.')
    # print(f'Độ dài cạnh BC = {d3} cm.')

    # # 4. Kiểm tra xem ba điểm có tạo được một tam giác không
    # if is_triangle(ax, ay, bx, by, cx, cy):
    #     print('A,B, C là một tam giác')
    # else:
    #     print('A,B, C không phải là một tam giác')
    #     exit()

    # 5. Tính các góc của tam giác
    if is_triangle(ax, ay, bx, by, cx, cy):
        bac_angle = compute_angle(bx, by, ax, ay, cx, cy)
        abc_angle = compute_angle(ax, ay, bx, by, cx, cy)
        bca_angle = compute_angle(bx, by, cx, cy, ax, ay)
        print(f'Góc BAC = {round(bac_angle)} (độ)')
        print(f'Góc ABC = {round(abc_angle)} (độ)')
        print(f'Góc BCA = {round(bca_angle)} (độ)')


def create_vector(px1, py1, px2, py2):
    return [(px1 - px2), (py1 - py2)]


def compute_angle(px1, py1, px2, py2, px3, py3):
    vector1 = create_vector(px1, py1, px2, py2)
    vector2 = create_vector(px2, py2, px3, py3)
    dividend = abs(vector1[0]*vector2[0] + vector1[1]*vector2[1])
    divisor = sqrt(vector1[0]**2 + vector1[1]**2) * sqrt(vector2[0]**2 + vector2[1]**2)
    if divisor != 0:
        cosine = dividend / divisor
        # return compute_degree_from_cosine(cosine)
        return round(compute_degree_from_cosine(cosine))


def compute_angle_2(vector1, vector2):
    dividend = vector1[0]*vector2[0] + vector1[1]*vector2[1]
    divisor = sqrt(vector1[0]**2 + vector1[1]**2) * sqrt(vector2[0]**2 + vector2[1]**2)
    if divisor != 0:
        cosine = dividend / divisor
        return compute_degree_from_cosine(cosine)


def compute_degree_from_cosine(cosine):
    rad = acos(cosine)
    deg = degrees(rad)
    return deg


def is_triangle(ax, ay, bx, by, cx, cy):
    d1 = distance(ax, ay, bx, by)
    d2 = distance(ax, ay, cx, cy)
    d3 = distance(bx, by, cx, cy)
    return d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1


def distance(px1, py1, px2, py2):
    return sqrt((px2 - px1)**2 + (py2 - py1)**2)


def get_number(message):
    while True:
        inp = input(message)
        try:
            return int(inp)
        except ValueError:
            print('Sai định dạng. Vui lòng nhập vào một số!')
            continue


if __name__ == '__main__':
    main()


