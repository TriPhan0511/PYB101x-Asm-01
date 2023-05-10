import math


# def get_angle_1(knee, hip, shoulder):
#     ang = math.degrees(
#         math.atan2(shoulder[1] - hip[1], shoulder[0] - hip[0]) - math.atan2(knee[1] - hip[1], knee[0] - hip[0]))
#     return ang + 360 if ang < 0 else ang

# def get_angle_1(a, b, c):
#     ang = math.degrees(
#         math.atan2(c[1] - b[1], c[0] - b[0]) - math.atan2(a[1] - b[1], a[0] - b[0]))
#     return ang + 360 if ang < 0 else ang
#
#
# print(get_angle_1((5, 0), (0, 0), (0, 5)))  # 90.0
# print(get_angle_1((6, 0), (0, 0), (6, 6)))  # 45.0


# def get_angle(a, b, c):
# def compute_angle(ax, ay, bx, by, cx, cy):
#     ang = math.degrees(
#         math.atan2(cy - by, cx - bx) - math.atan2(ay - by, ax - bx))
#     return ang + 360 if ang < 0 else ang


# def compute_angle(ax, ay, bx, by, cx, cy):
#     ang = round(math.degrees(math.atan2(cy - by, cx - bx) - math.atan2(ay - by, ax - bx)), 2)
#     return ang + 360 if ang < 0 else ang

def compute_angle(ax, ay, bx, by, cx, cy):
    ang = round(math.degrees(math.atan2(cy - by, cx - bx) - math.atan2(ay - by, ax - bx)), 2)
    ang = ang + 360 if ang < 0 else ang
    return 360 - ang if ang > 180 else ang

# # A(5, 0) B(0, 0) C(0, 5)
# ax = 5
# ay = 0
# bx = 0
# by = 0
# cx = 0
# cy = 5
# print(compute_angle(ax, ay, bx, by, cx, cy))  # angle B = 90.0 degrees

# # A(6, 0) B(0, 0) C(6, 6)
# ax = 6
# ay = 0
# bx = 0
# by = 0
# cx = 6
# cy = 6
# print(compute_angle(ax, ay, bx, by, cx, cy))  # angle B = 45.0 degrees

# A(14, -8) B(10, -10) C(20, -10)
ax = 14
ay = -8
bx = 10
by = -10
cx = 20
cy = -10
print(compute_angle(bx, by, ax, ay, cx, cy))  # angle A = 135.0 degrees
print(compute_angle(cx, cy, ax, ay, bx, by))  # angle A = 135.0 degrees
# # print(compute_angle(ax, ay, bx, by, cx, cy))  # angle B = 333.43 degrees
# print(compute_angle(cx, cy, bx, by, ax, ay))  # angle B = 333.43 degrees
# print(compute_angle(ax, ay, cx, cy, bx, by))  # angle c = 18.43 degrees
