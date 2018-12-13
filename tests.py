from logic import *

def testing(arr=[0, 1, 2, 3, 4, 5, 6]):
    import test_module as tm
    from pprint import pprint
    if 0 in arr:
        print("TEST 0")
        pass
    if 1 in arr:
        print("TEST 1")
        print(generate_chain(tm.A))
    if 2 in arr:
        print("TEST 2")
        from sys import modules
        # module for testing
        module_name = 'test_module'
        #test_module = __import__(module_name)
        module = modules[module_name]
        pprint(list(get_all_overridings(module)))
    if 3 in arr:
        print("TEST 3")
        pprint(relation_classes(tm.A, tm.A))
    if 4 in arr:
        print("TEST 4")
        pprint([x for x in iter(common_subclasses(tm.Root, tm.A))])
    if 5 in arr:
        print("TEST 5")
        pprint([x for x in iter(common_superclasses(tm.E, tm.F, True))])
    if 6 in arr:
        print("TEST 6")
        pprint([g for g in iter(get_root_members(tm.F))])