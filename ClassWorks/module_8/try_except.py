try:
    a = 10 / 1
except ZeroDivisionError as e:
    print(f"you can't divide by zero____{e}", e.args)
else:
    print('done')
finally:
    print('all code is done')
