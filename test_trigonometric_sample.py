from trigonometric_sample import *

# # Test case
# cosine = 0.5
# print(f'{round(compute_degree_from_cosine(cosine))}')  # 60 (degree)

# # Test case 1: get_number function
# num = get_number('Enter a number: ')
# print(f'The entered number: {num}')

# Test case 2: distance function
# ax = 1
# ay = 2
# bx = 5
# by = 3
# print(f'{distance(ax, ay, bx, by)}')  # 4.123105625617661

# ax = get_number('Nhập tọa độ x của điểm A: ')
# ay = get_number('Nhập tọa độ y của điểm A: ')
# bx = get_number('Nhập tọa độ x của điểm B: ')
# by = get_number('Nhập tọa độ x của điểm B: ')
# print(f'{distance(ax, ay, bx, by)}')

# # Test case 3: is_triangle function
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
# cosine = 0.5
# print(f'{round(compute_degree_from_cosine(cosine))}')  # 60 (degree)

# # Test case 5: create_vector function
# # A(6, -2) B(4, -6)
# ax = 6
# ay = -2
# bx = 4
# by = -6
# print(f'{create_vector(ax, ay, bx, by)}')  # [2, 4]

# # Test case 6: compute_angle function
# # A(16, -2) B(16, -6) C(18, -4)
# ax = 16
# ay = -2
# bx = 16
# by = -6
# cx = 18
# cy = -4
# print(compute_angle(ax, ay, bx, by, cx, cy))

# Test case 7: compute three angles
# Nhập tọa độ 3 điểm từ bàn phím
# A(16, -2) B(16, -6) C(18, -4)
ax = 16
ay = -2
bx = 16
by = -6
cx = 18
cy = -4

# ax = get_number('Nhập toạ độ x của điểm A: ')
# ay = get_number('Nhập toạ độ y của điểm A: ')
# bx = get_number('Nhập toạ độ x của điểm B: ')
# by = get_number('Nhập toạ độ y của điểm B: ')
# cx = get_number('Nhập toạ độ x của điểm C: ')
# cy = get_number('Nhập toạ độ y của điểm C: ')
# print(f'Debug: ax = {ax} ay = {ay} bx = {bx} by = {by} cx = {cx} cy = {cy} ')

if is_triangle(ax, ay, bx, by, cx, cy):
    bac_angle = compute_angle(bx, by, ax, ay, cx, cy)
    abc_angle = compute_angle(ax, ay, bx, by, cx, cy)
    bca_angle = compute_angle(bx, by, cx, cy, ax, ay)
    print(f'Góc BAC = {round(bac_angle)} (độ)')
    print(f'Góc ABC = {round(abc_angle)} (độ)')
    print(f'Góc BCA = {round(bca_angle)} (độ)')

# Test case 8: type of triangle




































