while True:

    import random as r

    print("(1)addition (2)subtraction (3)Multiplication (4) division")

    operands = int(input("Enter your operand: "))

    random1 = r.randint(1, 99)
    random2 = r.randint(1, 99)

    if operands == 1:
        operand = '+'
    elif operands == 2:
        operand = '-'
    elif operands == 3:
        operand = '*'
    else:
        operand = '/'

    print("what is", random1, operand, random2)

    answer = int(eval("{} {} {}".format(random1, operand, random2)))
    userAnswer = int(input("Answer: "))

    if userAnswer == answer:
        print("Correct")
    else:
        print("wrong")

    ans = input("again(y/n) ")
    if ans != 'y':
        break
