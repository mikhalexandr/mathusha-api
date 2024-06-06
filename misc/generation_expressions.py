import mathgenerator
import unicodedata
import random
import re


def arithmetic_generation(complexity):
    id_ = random.randint(0, 3)
    problem, solution = None, None
    if complexity == 0:
        problem, solution = mathgenerator.genById(id_, 19, 19) if id_ != 2 else mathgenerator.genById(id_, 19)
    if complexity == 1:
        problem, solution = mathgenerator.genById(id_, 49, 49) if id_ != 2 else mathgenerator.genById(id_, 49)
    if complexity == 2:
        problem, solution = mathgenerator.genById(id_, 99, 99) if id_ != 2 else mathgenerator.genById(id_, 99)
    problem = re.sub(r'\\div|\\cdot', lambda match: {'\\div': ':', '\\cdot': '*'}[match.group(0)], problem)
    return problem[1:-2] if id_ != 2 else problem[1:-1], solution[1:-1]


def root_generation(complexity):
    id_square, id_cube = 6, 47
    problem, solution = None, None
    if complexity == 0:
        problem, solution = mathgenerator.genById(id_square, 1, 12)
        problem = re.sub(r'{|}|\$|=|\\sqrt',
                         lambda match: {'{': '', '}': '', '$': '', '=': '', r'\sqrt': '√'}[match.group(0)], problem)
    if complexity == 1:
        for_three = random.randint(1, 5)
        problem, solution = f'∛{for_three ** 3}', f'{for_three}'
    if complexity == 2:
        for_four = random.randint(1, 5)
        problem, solution = f'∜{for_four ** 4}', f'{for_four}'
    return problem, solution


def power_generation(complexity):
    problem, solution = None, None
    if complexity == 0:
        id_ = 8
        problem, solution = mathgenerator.genById(id_, 20)
    if complexity == 1:
        n, power = random.randint(1, 6), random.randint(0, 6)
        problem, solution = str(f'${n}^{power}=$'), str(f'${n ** power}$')
    if complexity == 2:
        n = random.randint(1, 5)
        power1, power2 = random.randint(1, 5), random.randint(1, 5)
        possible = [
            (f'${n}^{power1}*{n}^{power2}=$', f'${n ** (power1 + power2)}$'),
            (f'${n}^{power1}:{n}^{power2}=$', f'${n ** (power1 - power2)}$'),
            (f'$({n}^{power1})^{power2}=$', f'${n ** (power1 * power2)}$')
        ]
        id_ = random.randint(0, 2)
        problem, solution = possible[id_][0], possible[id_][1]
    return problem[1:-2], solution[1:-1]


def fractional_to_decimal_generation(complexity):
    id_ = 13
    problem, solution = None, None
    if complexity == 0:
        problem, solution = mathgenerator.genById(id_, 39, 39)
    if complexity == 1:
        problem, solution = mathgenerator.genById(id_, 69, 69)
    if complexity == 2:
        problem, solution = mathgenerator.genById(id_, 99, 99)
    problem = re.sub(r'\\div', '/', problem)
    return problem[1:-2], solution[1:-1]


def factorial_generation(complexity):
    id_ = 31
    problem, solution = None, None
    if complexity == 0:
        problem, solution = mathgenerator.genById(id_, 6)
    if complexity == 1:
        problem, solution = mathgenerator.genById(id_, 10)
    if complexity == 2:
        problem, solution = mathgenerator.genById(id_, 14)
    return problem[1:-2], solution[1:-1]


def logarithm_generation(complexity):
    id_ = 12
    problem, solution = None, None
    if complexity == 0:
        problem, solution = mathgenerator.genById(id_, 3, 6)
    if complexity == 1:
        problem, solution = mathgenerator.genById(id_, 5, 8)
    if complexity == 2:
        problem, solution = mathgenerator.genById(id_, 7, 10)
    problem = re.sub(r'_{(\d+)}',
                     lambda match: f'{chr(0x2080 + int(unicodedata.numeric(match.group(1))))}', problem)
    return problem[1:-2], solution[1:-1]


def linear_equation_generation(complexity):
    id_simple, id_hard = 11, 26
    problem, solution = None, None
    if complexity == 0:
        problem, solution = mathgenerator.genById(id_simple, 10)
    if complexity == 1:
        problem, solution = mathgenerator.genById(id_simple, 20)
    if complexity == 2:
        problem, solution = mathgenerator.genById(id_simple, 30)
    return problem[1:-1], solution[1:-1]


def quadratic_equation_generation(complexity):
    x1, x2 = None, None
    if complexity == 0:
        x1, x2 = random.randint(-10, 10), random.randint(-10, 10)
    if complexity == 1:
        x1, x2 = random.randint(-20, 20), random.randint(-20, 20)
    if complexity == 2:
        x1, x2 = random.randint(-30, 30), random.randint(-30, 30)
    p, q = (x1 + x2) * -1, x1 * x2
    p_to_pr, q_to_pr = f'+{abs(p)}' if p >= 0 else f'-{abs(p)}', f'+{abs(q)}' if q >= 0 else f'-{abs(q)}'
    problem, solution = f'$x^2{p_to_pr}x{q_to_pr}=0$', f'$x1={x1}, x2={x2}$'
    return problem[1:-1], solution[1:-1]


def linear_inequality_generation(complexity):
    pass


def quadratic_inequality_generation(complexity):
    pass


def mixed_generation(complexity, *selected_ids):
    selected_ids = list(selected_ids)
    if len(selected_ids) == 0:
        return "No topic id selected :("
    list_of_expressions = [arithmetic_generation, root_generation, power_generation, fractional_to_decimal_generation,
                           factorial_generation, logarithm_generation, linear_equation_generation,
                           quadratic_equation_generation, linear_inequality_generation, quadratic_inequality_generation]
    chosen_list = [i for i in list_of_expressions if list_of_expressions.index(i) in selected_ids]
    random_expression = random.choice(chosen_list)
    return random_expression(complexity)
