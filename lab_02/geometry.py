import math
from typing import List

FLOAT_ERROR_RATE: float = 1e-6


def floatCompare(a: float, b: float):
    if abs(a - b) < FLOAT_ERROR_RATE:
        return 1
    else:
        return 0


# For tuple/list dotTypes
def dotDistance2(dot1, dot2) -> float:
    return math.sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)


# Из a/b найти p/q, где p и q взаимно простые числа
def find_two_coprime_ints(a: float, b: float) -> (int, int):
    # Найти большее количество цифр после точки
    a_after_dot: int = len(str(a)) - len(str(int(a))) - 1 if len(str(a)) != len(str(math.ceil(a))) else 0
    b_after_dot: int = len(str(b)) - len(str(int(b))) - 1 if len(str(b)) != len(str(math.ceil(b))) else 0
    max_after_dot = a_after_dot if a_after_dot >= b_after_dot else b_after_dot
    print(a_after_dot, b_after_dot, max_after_dot)

    a_new: int = int(a * 10 ** max_after_dot)
    b_new: int = int(b * 10 ** max_after_dot)
    print(f"a_new - {a_new}, b_new - {b_new}")

    # Пусть а >= b
    swap_flag = 0
    if a_new < b_new:
        swap_flag = 1
        a_new, b_new = b_new, a_new

    # Уменьшаем числа пока можем
    i: int = 2
    while i <= b_new / 2:
        while a_new % i == 0 and b_new % i == 0:
            a_new = (a_new // i)
            b_new = (b_new // i)
        i += 1

    if swap_flag:
        a_new, b_new = b_new, a_new

    return a_new, b_new


class Epicycloid:
    DRAW_STEP_ANGLE = 2

    # a ~ r
    # b ~ R
    def __init__(self, a: float = 1, b: float = 1, x0: float = 0, y0: float = 0):
        self.a = a
        self.b = b
        self.x0 = x0
        self.y0 = y0

    def get_coordinates(self, angle) -> (float, float):
        x: float = (self.a + self.b) * math.cos(angle) - self.a * math.cos((self.a + self.b) * angle / self.a) + self.x0
        y: float = (self.a + self.b) * math.sin(angle) - self.a * math.sin((self.a + self.b) * angle / self.a) + self.y0
        return x, y

    def create_figure(self) -> (List[float], List[float]):
        x_list: List[float] = []
        y_list: List[float] = []

        p, q = find_two_coprime_ints(self.a, self.b)

        for i in range(0, 2 * p * 180, self.DRAW_STEP_ANGLE):
            current_angle: float = i / 180 * math.pi
            current_x, current_y = self.get_coordinates(current_angle)
            x_list.append(current_x)
            y_list.append(current_y)

        print(x_list, y_list)
        return x_list, y_list
