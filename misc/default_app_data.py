from data import db_session
from data.achievements import Achievement
from data.topics import Topic


def create_default_data():
    session = db_session.create_session()

    t1 = Topic(name='Сложение',
               description='Сложение — одна из основных бинарных математических операций двух аргументов, '
                           'результатом которой является новое число, получаемое увеличением значения первого аргумента'
                           ' на значение второго аргумента. То есть каждой паре элементов из множества A ставится в'
                           ' соответствие элемент c=a+b, называемый суммой a и b',
               eng_name='Addition',
               eng_description='Addition is one of the basic binary mathematical operations of two arguments, '
                               'the result of which is a new number obtained by increasing the value of the first argument'
                               ' to the value of the second argument. That is, each pair of elements from set A is placed in '
                               ' matching element c=a+b, called the sum of a and b',
               color='#F44336')
    t2 = Topic(name='Вычитание', description='Вычитание — одна из вспомогательных бинарных математических операций '
                                             'двух аргументов, результатом которой является новое число, получаемое '
                                             'уменьшением значения первого аргумента на значение второго аргумента',
               eng_name='Subtraction',
               eng_description='Subtraction is one of the auxiliary binary mathematical operations '
                               'two arguments, the result of which is the new number obtained'
                               'by decreasing the value of the first argument by the value of the second argument',
               color='#E91E63')
    t3 = Topic(name='Умножение', description='Умножение — одна из основных математических операций над двумя '
                                             'аргументами, которые называются множителями или сомножителями. '
                                             'Результат умножения называется их произведением',
               eng_name='Multiplication',
               eng_description='Multiplication is one of the basic mathematical operations on two'
                               'arguments, which are called factors or factors. '
                               'The result of multiplication is called their product',
               color='#9C27B0')
    t4 = Topic(name='Деление',
               description='Деление — действие, обратное умножению. Деление обозначается двоеточием, обелюсом, '
                           'косой чертой или записывается в виде дроби',
               eng_name='Division',
               eng_description='Division is the inverse of multiplication. Division is indicated by a colon, obelus, '
                               'slashed or written as a fraction',
               color='#673AB7')
    t5 = Topic(name='Корень',
               description='Корень — это значение, которое удовлетворяет '
                           'уравнению или неравенству. Например, корни уравнения x^2 - 4 = 0 - это 2 и -2',
               eng_name='Root',
               eng_description='A root is a value that satisfies an'
                               'inequality or equation. For example, the roots of the equation x^2 - 4 = 0 are 2 and -2',
               color='#3F51B5')
    t6 = Topic(name='Степень',
               description='Степень — это число, возведенное в определенную степень. '
                           'Например, 2 в степени 3 равно 8 (2^3 = 8)',
               eng_name='Power',
               eng_description='A power is a number raised to a certain power. '
                               'For example, 2 to the power of 3 is 8 (2^3 = 8)',
               color='#2196F3')
    t7 = Topic(name='Дробь',
               description='Дробь — это число, которое представляет собой отношение двух целых чисел. '
                           'Например, дробь 1/2 равна 0.5 в десятичном представлении',
               eng_name='Fraction',
               eng_description='A fraction is a number that represents the ratio of two integers. '
                               'For example, the fraction 1/2 is equal to 0.5 in decimal representation',
               color='#03A9F4')
    t8 = Topic(name='Факториал',
               description='Факториал натурального числа — это произведение всех натуральных чисел от 1 до данного числа. '
                           'Например, факториал 5 равен 120 (5! = 1*2*3*4*5 = 120)',
               eng_name='Factorial',
               eng_description='The factorial of a natural number is the product of all natural numbers from 1 to the given number. '
                               'For example, the factorial of 5 is 120 (5! = 1*2*3*4*5 = 120)',
               color='#00BCD4')
    t9 = Topic(name='Логарифм',
               description='Логарифм числа по заданному основанию — это показатель степени, в которую нужно возвести основание, '
                           'чтобы получить данное число. '
                           'Например, логарифм 100 по основанию 10 равен 2 (log10(100) = 2)',
               eng_name='Logarithm',
               eng_description='The logarithm of a number to a given base is the exponent to which the base must be raised '
                               'to obtain the given number. '
                               'For example, the logarithm of 100 to base 10 is 2 (log10(100) = 2)',
               color='#009688')
    t10 = Topic(name='Тригонометрические значения',
                description='Тригонометрические значения — это значения синуса, косинуса, тангенса и '
                            'котангенса для заданного угла. Например, синус 30 градусов равен 0.5',
                eng_name='Trigonometric values',
                eng_description='Trigonometric values are the values of sine, cosine, tangent, and '
                                'cotangent for a given angle. For example, the sine of 30 degrees is 0.5',
                color='#4CAF50')
    t11 = Topic(name='Линейное уравнение',
                description='Линейное уравнение — это уравнение, которое представляет собой прямую линию '
                            'в декартовой системе координат. Например, уравнение y = 2x + 1 — это линейное уравнение',
                eng_name='Linear equation',
                eng_description='A linear equation is an equation that represents a straight line '
                                'in the Cartesian coordinate system. For example, the equation y = 2x + 1 is a linear equation',
                color='#8BC34A')
    t12 = Topic(name='Квадратное уравнение',
                description='Квадратное уравнение — это уравнение, которое представляет собой параболу '
                            'в декартовой системе координат. Например, уравнение y = x^2 + 2x - 3 — это квадратное уравнение',
                eng_name='Quadratic equation',
                eng_description='A quadratic equation is an equation that represents a parabola '
                                'in the Cartesian coordinate system. For example, the equation y = x^2 + 2x - 3 is a quadratic equation',
                color='#CDDC39')
    t13 = Topic(name='Линейное неравенство',
                description='Линейное неравенство — это неравенство, которое представляет собой область '
                            'в декартовой системе координат, ограниченную прямой линией. Например, неравенство y > 2x + 1 — '
                            'это линейное неравенство',
                eng_name='Linear inequality',
                eng_description='A linear inequality is an inequality that represents a region '
                                'in the Cartesian coordinate system, bounded by a straight line. For example, the inequality y > 2x + 1 — '
                                'is a linear inequality',
                color='#FFEB3B')
    t14 = Topic(name='Смешанная задача',
                description='Смешанная задача — это задача, которая включает в себя различные '
                            'математические операции и понятия. Например, задача, которая требует решения линейного уравнения '
                            'и нахождения факториала',
                eng_name='Mixed problem',
                eng_description='A mixed problem is a problem that involves various '
                                'mathematical operations and concepts. For example, a problem that requires solving a linear equation '
                                'and finding a factorial',
                color='#FFC107')
    t15 = Topic(name='Yandex GPT',
                description='Yandex GPT — это алгоритм машинного обучения, который может генерировать '
                            'все, что угодно! Попробуйте победить нейросеть, ответив на ее математические вопросы!',
                eng_name='Yandex GPT',
                eng_description='Yandex GPT is a machine learning algorithm that can generate '
                                'anything! Try to beat the neural network by answering its math questions!',
                color='#FF9800')

    for i in range(1, 16):
        session.add(eval(f't{i}'))

    a1 = Achievement(name='Легенда', eng_name='Legend', description='Станьте ТОП-1 в рейтинге!',
                     eng_description='Be the TOP-1 in the ranking!', type=1.1)
    a2 = Achievement(name='Чемпион', eng_name='Champion', description='Станьте ТОП-2 в рейтинге!',
                     eng_description='Be the TOP-2 in the ranking!', type=1.2)
    a3 = Achievement(name='Красавчик', eng_name='Beauty', description='Станьте ТОП-3 в рейтинге!',
                     eng_description='Be the TOP-3 in the ranking!', type=1.3)
    a4 = Achievement(name='Гуру математики', eng_name='Guru of math', description='Решите 10000 заданий!',
                     eng_description='Solve 10000 tasks!', type=2.1)
    a5 = Achievement(name='Сильный математик', eng_name='Strong mathematician', description='Решите 1000 заданий!',
                     eng_description='Solve 1000 tasks!', type=2.2)
    a6 = Achievement(name='Юный математик', eng_name='Young mathematician', description='Решите 500 заданий!',
                     eng_description='Solve 500 tasks!', type=2.3)
    a7 = Achievement(name='Попстар', eng_name='Popstar', description='Наберите 1000 очков рейтинга!',
                     eng_description='Get 1000 points in the ranking!', type=3.1)
    a8 = Achievement(name='Мидлстар', eng_name='Middlestar', description='Наберите 500 очков рейтинга!',
                     eng_description='Get 500 points in the ranking!', type=3.2)
    a9 = Achievement(name='Юнгстар', eng_name='Youngstar', description='Наберите 100 очков рейтинга!',
                     eng_description='Get 100 points in the ranking!', type=3.3)
    a10 = Achievement(name='Сильнее чем AI', eng_name='Stronger than AI', description='Решите задание от Yandex GPT',
                      eng_description='Solve the task from Yandex GPT', type=0.0)

    for i in range(1, 11):
        session.add(eval(f'a{i}'))

    session.commit()
    session.close()
