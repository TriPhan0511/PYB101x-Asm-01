import math

from utilities import *

# # Test case
# cosine = 0.5
# print(f'{round(compute_degree_from_cosine(cosine))}')  # 60 (degree)

# # Test case 1: get_number function
# Test function nhập một số từ bàn phím
# num = get_number('Enter a number: ')
# print(f'The entered number: {num}')

# Test case 2: distance function
# Test function tính khoảng cách giữa hai điểm
# ax = 1
# ay = 2
# bx = 5
# by = 3
# print(f'{compute_distance(ax, ay, bx, by)}')  # 4.12

# ax = get_number('Nhập tọa độ x của điểm A: ')
# ay = get_number('Nhập tọa độ y của điểm A: ')
# bx = get_number('Nhập tọa độ x của điểm B: ')
# by = get_number('Nhập tọa độ x của điểm B: ')
# print(f'{distance(ax, ay, bx, by)}')

# # Test case 3: is_triangle function
# Test function xác thực 3 điểm cho trước có tao nên một tam giác
# # A(6, -2) B(4, -6) C(12, -6): True
# ax = 6
# ay = -2
# bx = 4
# by = -6
# cx = 12
# cy = -6
# print(f'Three points A(6, -2) B(4, -6) C(12, -6): {is_triangle(ax, ay, bx, by, cx, cy)}')  # True
# #
# # A(6, -2) B(4, -6) C(4, -6): False
# ax = 6
# ay = -2
# bx = 4
# by = -6
# cx = 4
# cy = -6
# print(f'Three points A(6, 2) B(4, 6) C(4, 6): {is_triangle(ax, ay, bx, by, cx, cy)}')  # False

# # Test case 4: compute_degree_from_cosine function
# Test function tính số đo độ của một góc dựa trên cosine của góc đó
# cosine = 0.5
# print(f'{round(compute_degree_from_cosine(cosine))}')  # 60 (degree)

# # Test case 5: create_vector function
# Test function tạo ra một vector từ các tọa độ (x,y) của hai điểm
# # A(6, -2) B(4, -6)
# ax = 6
# ay = -2
# bx = 4
# by = -6
# print(f'{create_vector(ax, ay, bx, by)}')  # [2, 4]

# # Test case 6: compute_angle function
# Test function tính số đo độ của một góc dựa trên các tọa độ (x,y) của 3 điểm
# # A(16, -2) B(16, -6) C(18, -4)
# ax = 16
# ay = -2
# bx = 16
# by = -6
# cx = 18
# cy = -4
# print(compute_angle(ax, ay, bx, by, cx, cy))

# Test case 7: compute three angles
# Test tính số đo độ của 3 góc dựa trên các tọa độ (x,y) của 3 điểm
# Nhập tọa độ 3 điểm từ bàn phím
# A(16, -2) B(16, -6) C(18, -4)
# ax = 16
# ay = -2
# bx = 16
# by = -6
# cx = 18
# cy = -4

# ax = get_number('Nhập toạ độ x của điểm A: ')
# ay = get_number('Nhập toạ độ y của điểm A: ')
# bx = get_number('Nhập toạ độ x của điểm B: ')
# by = get_number('Nhập toạ độ y của điểm B: ')
# cx = get_number('Nhập toạ độ x của điểm C: ')
# cy = get_number('Nhập toạ độ y của điểm C: ')
# print(f'Debug: ax = {ax} ay = {ay} bx = {bx} by = {by} cx = {cx} cy = {cy} ')

# if is_triangle(ax, ay, bx, by, cx, cy):
#     bac_angle = compute_angle(bx, by, ax, ay, cx, cy)
#     abc_angle = compute_angle(ax, ay, bx, by, cx, cy)
#     bca_angle = compute_angle(bx, by, cx, cy, ax, ay)
#     print(f'Góc BAC = {round(bac_angle)} (độ)')
#     print(f'Góc ABC = {round(abc_angle)} (độ)')
#     print(f'Góc BCA = {round(bca_angle)} (độ)')

# Test case 8: is_right_triangle
# Test function xác thực tam giác vuông
# # A(4, -8) B(4, -12) C(10, -12): vuông tại đỉnh B
# ax = 4
# ay = -8
# bx = 4
# by = -12
# cx = 10
# cy = -12
# test_is_right_triangle = is_right_triangle(ax, ay, bx, by, cx, cy)
# if test_is_right_triangle[0]:
#     print(f'Tam giác vuông tại đỉnh {test_is_right_triangle[1]}')
# else:
#     print('Không phải làm tam giác vuông')

# # A(6, -2) B(4, -6) C(12, -6) : Không phải là tam giác vuông
# ax = 6
# ay = -2
# bx = 4
# by = -6
# cx = 12
# cy = -6
# test_is_right_triangle = is_right_triangle(ax, ay, bx, by, cx, cy)
# if test_is_right_triangle[0]:
#     print(f'Tam giác vuông tại đỉnh {test_is_right_triangle[1]}')
# else:
#     print('Không phải làm tam giác vuông')

# Test case 9 : is_obtuse_triangle function
# Test function xác thực tam giác tù
# # A(14, -8) B(10, -10) C(20, -10) : Tam giác tù tại đỉnh A
# ax = 14
# ay = -8
# bx = 10
# by = -10
# cx = 20
# cy = -10
# test_is_obtuse_triangle = is_obtuse_triangle(ax, ay, bx, by, cx, cy)
# if test_is_obtuse_triangle[0]:
#     print(f'Tam giác tù tại đỉnh {test_is_obtuse_triangle[1]}')
# else:
#     print('Không phải làm tam giác tù')

# # A(6, -2) B(4, -6) C(12, -6) : Không phải là tam giác tù
# ax = 6
# ay = -2
# bx = 4
# by = -6
# cx = 12
# cy = -6
# test_is_obtuse_triangle = is_obtuse_triangle(ax, ay, bx, by, cx, cy)
# if test_is_obtuse_triangle[0]:
#     print(f'Tam giác tù tại đỉnh {test_is_obtuse_triangle[1]}')
# else:
#     print('Không phải làm tam giác tù')

# Test case 10 : is_isosceles_triangle function
# Test function xác thực tam giác cân
# # A(8,3) B(7,0) C(9,0) : Tam giác cân tại đỉnh A
# ax = 8
# ay = 3
# bx = 7
# by = 0
# cx = 9
# cy = 0

# # A(6, -2) B(4, -6) C(12, -6) : Không phải là tam giác cân
# ax = 6
# ay = -2
# bx = 4
# by = -6
# cx = 12
# cy = -6

# test_is_isosceles_triangle = is_isosceles_triangle(ax, ay, bx, by, cx, cy)
# if test_is_isosceles_triangle[0]:
#     print(f'Tam giác cân tại đỉnh {test_is_isosceles_triangle[1]}')
# else:
#     print('Không phải làm tam giác cân')


# Test case 11 : is_equilateral_triangle function
# Test function xác thực tam giác đều
# # A(math.sqrt(3), 2) B(0, 1) C(0, 3) : Tam giác đều
# ax = math.sqrt(3)
# ay = 2
# bx = 0
# by = 1
# cx = 0
# cy = 3

# # A(6, -2) B(4, -6) C(12, -6) : Không phải là tam giác đều
# ax = 6
# ay = -2
# bx = 4
# by = -6
# cx = 12
# cy = -6
#
# test_is_equilateral_triangle = is_equilateral_triangle(ax, ay, bx, by, cx, cy)
# if test_is_equilateral_triangle[0]:
#     print('Tam giác đều')
# else:
#     print('Không phải là tam giác đều')

# Test case 12 : is_right_and_isosceles_triangle function
# Test function xác thực tam giác vuông cân
# # A(1, 3) B(1, 1) C(3, 1) : Tam giác vuông cân tại đỉnh B
# ax = 1
# ay = 3
# bx = 1
# by = 1
# cx = 3
# cy = 1

# # A(1, 4) B(1, 1) C(3, 1): Không phải là tam giác vuông cân (chỉ là tam giác vuông tại B)
# ax = 1
# ay = 4
# bx = 1
# by = 1
# cx = 3
# cy = 1

# # A(8,3) B(7,0) C(9,0) : Không phải là tam giác vuông cân (chỉ là tam giác cân tại A)
# ax = 8
# ay = 3
# bx = 7
# by = 0
# cx = 9
# cy = 0

# # A(5,4) B(4,2) C(5,1) : Không phải là tam giác vuông cân (chỉ là tam giác thường)
# ax = 5
# ay = 4
# bx = 4
# by = 2
# cx = 5
# cy = 1

# test_is_right_and_isosceles_triangle = is_right_and_isosceles_triangle(ax, ay, bx, by, cx, cy)
# if test_is_right_and_isosceles_triangle[0]:
#     print(f'Tam giác vuông cân tại đỉnh {test_is_right_and_isosceles_triangle[1]}')
# else:
#     print('Không phải là tam giác vuông cân')

# Test case 13 : is_obtuse_and_isosceles_triangle function
# Test function xác thực tam giác tù cân
# # A(6,2) B(3,1) C(9, 1) : Tam giác tù cân tại đỉnh A
# ax = 6
# ay = 2
# bx = 3
# by = 1
# cx = 9
# cy = 1

# # A(6,2) B(3,1) C(9, 1) : Không phải là tam giác tù cân (chỉ là tam giác tù tại A)
# ax = 6
# ay = 2
# bx = 3
# by = 1
# cx = 10
# cy = 1

# # A(2,4) B(1,1) C(3, 1) : Không phải là tam giác tù cân (chỉ là tam giác cân tại A)
# ax = 2
# ay = 4
# bx = 1
# by = 1
# cx = 3
# cy = 1

# # A(4,4) B(2,2) C(3, 1) : Không phải là tam giác tù cân (chỉ là tam giác thường)
# ax = 4
# ay = 4
# bx = 2
# by = 2
# cx = 3
# cy = 1

# test_is_obtuse_and_isosceles_triangle = is_obtuse_and_isosceles_triangle(ax, ay, bx, by, cx, cy)
# if test_is_obtuse_and_isosceles_triangle[0]:
#     print(f'Tam giác tù tại đỉnh A và cân tại đỉnh {test_is_obtuse_and_isosceles_triangle[1]}')
# else:
#     print('Không phải là tam giác tù cân')

# Test case 14 : is_normal_triangle function
# Test function xác thực tam giác thường
# A(4,4) B(2,2) C(3, 1) : Tam giác thường
# ax = 4
# ay = 4
# bx = 2
# by = 2
# cx = 3
# cy = 1

ax = 4
ay = 3
bx = 3
by = 1
cx = 6
cy = 1

if is_normal_triangle(ax, ay, bx, by, cx, cy)[0]:
    print('Tam giác thường')
else:
    print('Không phải tam giác thường')





































