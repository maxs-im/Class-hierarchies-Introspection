from .parsing import *
from collections import namedtuple

def _border(fn):
    def decorator(*args, **kwargs):
        content = (el + separator + el).join(fn(*args, **kwargs))
        return separator + el + content + el

    return decorator

@_border
def transitive_inheritance_chains(arrcls):
    # title
    blocks = ['Transitive inheritance chains']
    for i, cls in enumerate(arrcls):
        # header
        blocks.append(f'{i+1}. Start point: {cls.__name__}')
        #content
        blocks.append(dec_overriding(cls))
    
    return blocks

@_border
def overrided_members(allcls):
    # title 
    blocks = ['Overrided attributes and methods']
    for cls in allcls:
        blocks.append(dec_overriding(cls))

    return blocks

@_border
def relation_between(a, b):
    title = f'Relation between {a.__name__} and {b.__name__}'
    return [title, dec_relation(a, b)]

@_border
def common_subclass(arrcls, biggest):
    # title
    names = ', '.join(map(lambda x: x.__name__, arrcls))
    blocks = [f'The {"biggest" if biggest else "least"} common subclass for {names}']
    blocks.append(dec_subclasses(arrcls, biggest))
    return blocks

@_border
def common_superclass(a, b, biggest):
    blocks = [f'The {"biggest" if biggest else "least"} common superclass for {a.__name__} and {b.__name__}']
    blocks.append(dec_superclass(a, b, biggest))
    return blocks

@_border
def members_inherited_root(a):
    title = f'Attributes and methods inherited by {a.__name__} from RootClass'
    content = dec_root_member(a)

    return [title, content]

ValueTask = namedtuple("ValueTask", 'fn description')
# available tasks
task_dict = {
    "inheritance": 
        ValueTask(transitive_inheritance_chains, "Transitive inheritance chains"),
    "override":
        ValueTask(overrided_members, "Overrided attributes and methods"),
    "relation": 
        ValueTask(relation_between, "Relation between two classes"),
    "subclass": 
        ValueTask(common_subclass, "The biggest/least common subclass for two classes"),
    "superclass": 
        ValueTask(common_superclass, "The biggest/least common superclass for two classes"),
    "root": 
        ValueTask(common_superclass, "Attributes and methods inherited by class from RootClass")
}