'''try:
    a = 10 / 1
except ZeroDivisionError as e:
    print(f"you can't divide by zero____{e}", e.args)
else:
    print('done')
finally:
    print('all code is done')'''


def f1(x):
    return total / x


def f2():
    summ = 0
    for i in range(-2, 2):
        try:
            summ += f1(i)
            print(summ)
        except ZeroDivisionError as err:
            print(err)
    return summ / 0


try:
    total = f2()
    print(f"result {total}")
except ZeroDivisionError as exc:
    print(f"this is what went wrong {exc}")
except NameError as exc:
    print(f"this is what went wrong {exc}")
