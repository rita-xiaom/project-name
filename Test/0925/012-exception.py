# try:
#     filename=input('please input filename: ')
#     open('%s.txt'%filename)
# except FileNotFoundError:
#     print('%s.txt file not found'%filename)


# try:
#     print(stu)
# except BaseException as msg:
#     print(msg)

def division(x,y):
    if y==0:
        raise ZeroDivisionError('zero is not allow!')

try:
    division(7,0)
except BaseException as msg:
    print(msg)
