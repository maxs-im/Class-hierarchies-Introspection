class A(object):
    pass

class B(A):
    pass

import inspect
print(inspect.getmro(B))

print("----------------------------")

import test_package.A as myA

print(inspect.getmro(myA))
