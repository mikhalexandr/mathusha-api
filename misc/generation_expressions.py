import mathgenerator
import random


def arithmetic_generation(complexity):
    id_ = random.randint(0, 3)
    problem, solution = None, None
    if complexity == 0:
        problem, solution = mathgenerator.genById(id_, 99, 99) if id_ != 2 else mathgenerator.genById(id_, 9)
    if complexity == 1:
        problem, solution = mathgenerator.genById(id_, 99, 9) if id_ != 2 else mathgenerator.genById(id_, 9)
    if complexity == 2:
        problem, solution = mathgenerator.genById(id_, 9, 9) if id_ != 2 else mathgenerator.genById(id_, 9)
    return problem, solution


def root_generation(complexity):
    id_square, id_cube = 6, 47
    problem, solution = None, None
    if complexity == 0:
        problem, solution = mathgenerator.genById(id_square, 1, 12)
    if complexity == 1:
        problem, solution = mathgenerator.genById(id_square, 12, 24)
    if complexity == 2:
        problem, solution = mathgenerator.genById(id_cube, 1, 100)
    return problem, solution


def power_generation(complexity):
    problem, solution = None, None
    if complexity == 0:
        id_ = 8
        problem, solution = mathgenerator.genById(id_, 20)
    if complexity == 1:
        n, power = random.randint(1, 20), random.randint(0, 20)
        problem, solution = str(f'${n}^{power}=$'), str(f'${n ** power}$')
    if complexity == 2:
        n = random.randint(1, 20)
        power1, power2 = random.randint(1, 20), random.randint(1, 20)
        possible = [
            (f'${n}^{power1}*{n}^{power2}$', f'${n ** (power1 + power2)}$'),
            (f'${n}^{power1}:{n}^{power2}$', f'${n ** (power1 - power2)}$'),
            (f'$({n}^{power1})^{power2}$', f'${n ** (power1 * power2)}$')
        ]
        id_ = random.randint(0, 2)
        problem, solution = possible[id_][0], possible[id_][1]
    return problem, solution


def logarithm_generation(complexity):
    id_ = 12
    problem, solution = None, None
    if complexity == 0:
        problem, solution = mathgenerator.genById(id_, 3, 8)
    if complexity == 1:
        problem, solution = mathgenerator.genById(id_, 6, 16)
    if complexity == 2:
        problem, solution = mathgenerator.genById(id_, 9, 24)
    return problem, solution


def linear_equation_generation(complexity):
    id_simple, id_hard = 11, 26
    problem, solution = None, None
    if complexity == 0:
        problem, solution = mathgenerator.genById(id_simple, 10)
    if complexity == 1:
        problem, solution = mathgenerator.genById(id_simple, 20)
    if complexity == 2:
        problem, solution = mathgenerator.genById(id_hard, 2, 20, 20)
    return problem, solution


def quadratic_equation_generation(complexity):
    x1, x2 = None, None
    if complexity == 0:
        x1, x2 = random.randint(-10, 10), random.randint(-10, 10)
    if complexity == 1:
        x1, x2 = random.randint(-20, 20), random.randint(-20, 20)
    if complexity == 2:
        x1, x2 = random.randint(-30, 30), random.randint(-30, 30)
    p, q = (x1 + x2) * -1, x1 * x2
    p_to_pr, q_to_pr = '+p' if p >= 0 else '-p', '+q' if q >= 0 else '-q'
    problem, solution = f'$x^2{p_to_pr}x{q_to_pr}=0$', f'$x1={x1}, x2={x2}$'
    return problem, solution
