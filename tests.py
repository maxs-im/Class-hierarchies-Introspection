from pprint import pprint
import test_module as tm
from logic import *
from parsing import *

def testing_logic(arr=[0, 1, 2, 3, 4, 5, 6]):    
    if 0 in arr:
        print("TEST 0")
        pass
    if 1 in arr:
        print("TEST 1")
        print(generate_chain(tm.D))
    if 2 in arr:
        print("TEST 2")
        pprint(get_class_overridings(tm.A))
    if 3 in arr:
        print("TEST 3")
        pprint(relation_classes(tm.A, tm.A))
    if 4 in arr:
        print("TEST 4")
        pprint([x for x in iter(common_subclasses([tm.Root, tm.A], True))])
        print('-'*50)
        pprint([x for x in iter(common_subclasses([tm.Root, tm.A], False))])
    if 5 in arr:
        print("TEST 5")
        pprint([x for x in iter(common_superclasses(tm.E, tm.F, True))])
        print('-'*50)
        pprint([x for x in iter(common_superclasses(tm.Root, tm.A, False))])
    if 6 in arr:
        print("TEST 6")
        pprint(get_root_members(tm.F))

def testing_parsing(arr=[0, 1, 2, 3, 4, 5, 6]):    
    if 0 in arr:
        print("TEST 0")
        pass
    if 1 in arr:
        print("TEST 1")
        print(dec_chain(tm.D))
    if 2 in arr:
        print("TEST 2")
        print(dec_overriding(tm.A))
    if 3 in arr:
        print("TEST 3")
        print(dec_relation(tm.A, tm.A))
    if 4 in arr:
        print("TEST 4")
        print(dec_subclasses([tm.Root, tm.A], True))
        print('-'*50)
        print(dec_subclasses([tm.Root, tm.A], False))
    if 5 in arr:
        print("TEST 5")
        print(dec_superclass(tm.E, tm.F, True))
        print('-'*50)
        print(dec_superclass(tm.E, tm.F, False))
    if 6 in arr:
        print("TEST 6")
        print(dec_root_member(tm.F))