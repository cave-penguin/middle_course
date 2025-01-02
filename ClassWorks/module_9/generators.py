# import datetime

# numbers = [2, 6, 5, 3, 4, 7, 8, 1]

# result = (x ** 100 for x in numbers)
# print(result)
#
# for elem in result:
#     print(elem)
#
# print('----------')
#
# for elem in result:
#     print(elem)

# start = datetime.datetime.now()
#
# numbers = [2, 6, 5, 3, 4, 7, 8, 9]
# result = (x ** 3000 for x in numbers)
# # print(result)
#
# for i in result:
#     print(i)
#
# end = datetime.datetime.now()
#
# print(f"time {end - start}")


l1 = [2, 5, 4, 3, 6, 7]
l2 = [8, 9, 10, 11, 1, 24]

ran = range(10, 30)
zp = zip(l1, l2)
mp = map(str, l1)

print(ran, zp, mp)

print(list(ran))
print(list(zp))
print(list(mp))
print(list(ran))
print(list(zp))
print(list(mp))
