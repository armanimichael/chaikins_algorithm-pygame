"Chaikin's Algorithm for curves"

from typing import List
from pygame.math import Vector2

Points = List[Vector2]


def generate_q_point(p_1: Vector2, p_2: Vector2) -> Vector2:
    "Generate Q point from Chaikin's algoritm"
    parsed_p1 = Vector2(p_1.x * 3/4, p_1.y * 3/4)
    parsed_p2 = Vector2(p_2.x * 1/4, p_2.y * 1/4)

    return Vector2(parsed_p1.x + parsed_p2.x, parsed_p1.y + parsed_p2.y)


def generate_r_point(p_1: Vector2, p_2: Vector2) -> Vector2:
    "Generate Q point from Chaikin's algoritm"
    parsed_p1 = Vector2(p_1.x * 1/4, p_1.y * 1/4)
    parsed_p2 = Vector2(p_2.x * 3/4, p_2.y * 3/4)

    return Vector2(parsed_p1.x + parsed_p2.x, parsed_p1.y + parsed_p2.y)


def chaikin_algorithm(points: Points, iterations=1):
    "Curve creation algoritm"
    new_points = [points[0]]

    for i, _ in enumerate(points):
        if i + 1 < len(points):
            p_1 = points[i]
            p_2 = points[i + 1]

            q_point = generate_q_point(p_1, p_2)
            r_point = generate_r_point(p_1, p_2)

            new_points.append(q_point)
            new_points.append(r_point)
        else:
            new_points.append(points[i])

    if iterations == 1:
        return new_points
    return chaikin_algorithm(new_points, iterations - 1)
