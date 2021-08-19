#!python3
# https://www.jb51.net/article/215893.htm
import run_python
import run_cython
import time

number = 100

start = time.time()
run_python.test(number)
end = time.time()

py_time = end - start
print('Python time = {}'.format(py_time))

start = time.time()
run_cython.test(number)
end = time.time()

cy_time = end - start
print('Cython time = {}'.format(cy_time))

print('Speedup = {}'.format(py_time/cy_time))