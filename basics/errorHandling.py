def __devideFunc(num1, num2):
    try:
        result = int(num1) / int(num2)
    except ZeroDivisionError:
        print('division by zero!')
    except ValueError:
        print('Please enter an integer')
    else:
        print(f'result is {result}')
    finally:
        print('finally clause')


__devideFunc(2, 1)

__devideFunc(2, 0)

__devideFunc("2", "kjkjk")
