from pprint import pprint
import test_module as tm
from inspect import getmembers, isclass
from logic import *
from parsing import *
from interface import *

def testing_logic(arr=range(1, 7)):    
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
        gen_common = common_subclasses([tm.A, tm.A], True)
        if gen_common:
            pprint([x for x in iter(gen_common)])
        print('-'*50)
        gen_common = common_subclasses([tm.A, tm.A], False)
        if gen_common:
            pprint([x for x in iter(gen_common)])
    if 5 in arr:
        print("TEST 5")
        pprint([x for x in iter(common_superclasses(tm.E, tm.E, True))])
        print('-'*50)
        pprint([x for x in iter(common_superclasses(tm.Root, tm.A, False))])
    if 6 in arr:
        print("TEST 6")
        pprint(get_root_members(tm.F))

def testing_parsing(arr=range(1, 7)):    
    if 1 in arr:
        print("TEST 1")
        print(transitive_inheritance_chains([tm.D]))
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

def testing_interface(allcls, arr=range(1, 7)):    
    if 1 in arr:
        print("TEST 1")
        print(transitive_inheritance_chains(allcls))
    if 2 in arr:
        print("TEST 2")
        print(overrided_members(allcls))
    if 3 in arr:
        print("TEST 3")
        print(relation_between(tm.D, tm.F))
        print(relation_between(tm.Root, tm.Root))
    if 4 in arr:
        print("TEST 4")
        print(common_subclass([tm.D, tm.F], True))
        print('-'*50)
        print(common_subclass([tm.Root, tm.A], False))
    if 5 in arr:
        print("TEST 5")
        print(common_superclass(tm.E, tm.F, True))
        print('-'*50)
        print(common_superclass(tm.E, tm.F, False))
    if 6 in arr:
        print("TEST 6")
        print(members_inherited_root(tm.F))

def complex_analysis(allcls):
    yield transitive_inheritance_chains(allcls)
    yield overrided_members(allcls)

    for a in allcls:
        for b in allcls: 
            yield relation_between(a, b)
            yield common_subclass([a, b], True)
            yield common_subclass([a, b], False)
            yield common_superclass(a, b, True)
            yield common_superclass(a, b, False)

    for cls in allcls:
       yield members_inherited_root(cls)

if __name__ == "__main__":
    allcls = [v for n, v in getmembers(tm, isclass)]
    #testing_logic()
    #testing_parsing()
    if allcls:
        #testing_interface(allcls)
        for x in complex_analysis(allcls):
            print(x)
    