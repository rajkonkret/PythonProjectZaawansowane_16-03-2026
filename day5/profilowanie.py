import cProfile

def slow_function():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

cProfile.run("slow_function()")
#          4 function calls in 0.046 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.046    0.046 <string>:1(<module>)
#         1    0.046    0.046    0.046    0.046 profilowanie.py:3(slow_function)
#         1    0.000    0.000    0.046    0.046 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

#          4 function calls in 0.502 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.502    0.502 <string>:1(<module>)
#         1    0.502    0.502    0.502    0.502 profilowanie.py:3(slow_function)
#         1    0.000    0.000    0.502    0.502 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}