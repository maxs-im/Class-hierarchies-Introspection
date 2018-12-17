"""The main module where we can start our console application"""

__author__ = ('Maxim Galchenko <maxim1998g@gmail.com>')

import argparse
from os import path
from inspect import getmembers, isclass
import importlib.util
from hierarchy_introspecting.interface import *

class _ModuleData:
    """Class that store data from module that we will introspect
    
        classes - dictionary {name : object} of all classes in module
        root_name - root folder name to save our data
        user_list - classes that user want to analisys 
    
    """

    def __execute_module(self, path):
        """Import user module to enable introspecting"""
        spec = importlib.util.spec_from_file_location("", path)
        m = importlib.util.module_from_spec(spec)
        print("Module importing...")
        spec.loader.exec_module(m)
        print("Module imported.")
        return m

    def __init__(self, module_path, user_list):
        self.__class_set(module_path)
        if not self.classes:
            raise ValueError('There is no any hierarchy in your module')

        self.__user_list = []
        if user_list:
            for x in user_list:
                if x not in self.classes:
                    raise ValueError(f"Class {x} doesn't exist")
                self.__user_list.append(self.classes[x])
        else:
            self.__user_list = self.classes.values()
    
    def __class_get(self):
        return self.__classes
    def __class_set(self, path):
        module = self.__execute_module(path)
        self.__classes = {n: v for n, v in getmembers(module, isclass)}
        self.__set_root_name()

    def __get_root_name(self):
        return self.__root_name
    def __set_root_name(self):
        names = [cls.__name__ for cls in self.__classes.values() if len(cls.__mro__) == 2]
        self.__root_name =  '.'.join(names)
    def __get_user_list(self):
        return self.__user_list

    classes = property(__class_get, __class_set)
    root_name = property(fset=__set_root_name,fget=__get_root_name)
    user_list = property(fget=__get_user_list)

def _parse_args():
    # console UI
    parser = argparse.ArgumentParser()
    
    def check_file(value):
        if not path.isfile(value):
            raise argparse.ArgumentTypeError(f'check_file:"{value}" is not a valid path')
        return value
    # module name
    parser.add_argument("-m", "--module", help="<Required> Set your module path", required=True, type=check_file)
    # list of classes
    parser.add_argument("-c", "--classes", help="Set of class names", nargs='+')

    group = parser.add_mutually_exclusive_group(required=True)
    # complex analisys
    group.add_argument("-a", "--all", help="Complex analysis (all tasks)", action='store_true')

    def create_help_task():
        head = "Choose any from available tasks: "
        tasks = [f'{k} - {v.description}' for k, v in task_dict.items()]
        return head + '; '.join(tasks)
    # tasks
    group.add_argument("-t", choices=task_dict.keys(), help=create_help_task(), nargs='+')
    
    #return parser.parse_args("-m test_module.py -a".split(' '))
    return parser.parse_args("-m test_folder/test_module.py -t root".split(' '))

def _complex_analysis_gen(allcls, allowed):
    if transitive_inheritance_chains in allowed:
        yield transitive_inheritance_chains(allcls)
    if overrided_members in allowed:
        yield overrided_members(allcls)

    if relation_between in allowed:
        for a in allcls:
            for b in allcls: 
                yield relation_between(a, b)

    if common_subclass in allowed:
        for a in allcls:
            for b in allcls:
                yield common_subclass([a, b], True)
                yield common_subclass([a, b], False)

    if common_superclass in allowed:
        for a in allcls:
            for b in allcls:
                yield common_superclass(a, b, True)
                yield common_superclass(a, b, False)

    if members_inherited_root in allowed:
        for cls in allcls:
            yield members_inherited_root(cls)

def _logging(gen, file):
    for x in gen:
        file.write(x)
        print(x)
    
def start():
    """Entrance Console function"""
    args = _parse_args()
    try:
        meta_data = _ModuleData(args.module, args.classes)
        def get_file_path(name):
            sub_folder = path.dirname(args.module)
            extention = 'txt'
            return path.join(sub_folder, name + '.' + extention)

        if args.all:
            gener = _complex_analysis_gen(meta_data.user_list, 
                map(lambda x: x.fn, task_dict.values()))

            with open(get_file_path(meta_data.root_name + "_FULL"), "w") as file:
                _logging(gener, file)
        else:
            allowed = [task_dict[k].fn for k in args.t if k in task_dict]
            gener = _complex_analysis_gen(meta_data.user_list, allowed)

            with open(get_file_path(meta_data.root_name), "a") as file: 
                _logging(gener, file)
    except ValueError as e:
        print(e)
    except e:
        print(f"Unhandled exception: {e}")

    print("\nFinished.")

if __name__ == "__main__":
    start()