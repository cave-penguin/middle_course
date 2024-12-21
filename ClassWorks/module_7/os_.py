import os

print(os.getcwd())
if os.path.exists('second'):
    os.chdir('second')
else:
    os.mkdir('second')
    os.chdir('second')

print(os.getcwd())
# os.makedirs(r'third\fourth')
print(os.listdir())
# for i in os.walk('.'):
#     print(i)
os.chdir(
    'D:\Dev\Python\PythonProjectsForUniversity\middle_course\ClassWorks\module_7')
print(os.getcwd())
# print(os.listdir())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
# print(file)
# print(dirs)
# os.startfile(file[2]) #open file
# print(os.stat(file[2]).st_size)
os.system('pip install numpy')
