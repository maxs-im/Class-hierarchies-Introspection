from ._instances import *    
from .logic import *
from collections import defaultdict

def _categorize_members(converter, typegetter, arr):
    """Categorize class members"""
    def categorize(func, seq):
        """Returns mapping from categories to lists of categorized items."""
        d = defaultdict(list)
        for item in seq:
            d[func(item)].append(item)
        return d

    tp = lambda x: Member.get_val_type(typegetter(x))
    dd = categorize(tp, arr)
    return (converter(dd[k]) for k in sorted(dd.keys()))

def _members2str(cls):  
    members = generate_first_node(cls).items()
    convert_col = lambda arr: el.join(map(lambda x: x[0], arr))
    typegetter = lambda x: x[1].attribute_value
    cols = _categorize_members(convert_col, typegetter, members)

    return el.join(filter(bool, cols))

# task 1
def dec_chain(cls):
    # list of MemberChain
    res = generate_chain(cls)
    return el.join(map(str, res))

# task 2
def dec_overriding(cls):
    template = "The hierarchy does not contain any overrided attributes or methods."
    res = get_class_overridings(cls)
    if not res: return template 
    
    def convert_col(arr):
        topiccol = (f'{i+1}. {x}' for i, x in enumerate(arr))
        return el.join(topiccol)
    
    typegetter = lambda om: om.value
    cols = _categorize_members(convert_col, typegetter, res)

    return (el + separator + el).join(filter(bool, cols))

# task 3
def dec_relation(a, b):
    res = relation_classes(a, b)
    return str(res)

# task 4
def dec_subclasses(arrcls, greatest = True):    
    def parse_class(cls):
        class_name = f'{cls.__name__}:'
        return [class_name, _members2str(cls)]
    
    lines = list()   
    # input
    for cls in arrcls:
        lines.extend(parse_class(cls))

    intersect = common_subclasses(arrcls, greatest)
    if not intersect:
        # middle
        class_names = ' & '.join(map(lambda x: x.__name__, arrcls))
        lines.append(f"There is no {'biggest' if greatest else 'common'} common superclass for {class_names}.")
    else: 
        # middle
        res = [x for x in iter(intersect)]
        lines.append(f"Biggest common subclass{'es' if len(res) else ''}:")
        # result
        for cls in res:
            lines.extend(parse_class(cls))
    
    return (el + smallseparator + el).join(lines)

# task 5
def dec_superclass(a, b, greatest):
    no_answer = f"There is no {'biggest' if greatest else 'least'} common superclass for {a.__name__} and {b.__name__}."
    
    common_gen = common_superclasses(a, b, greatest)
    if not common_gen:
        return no_answer

    res = [x for x in iter(common_gen)]

    if not res: 
        return no_answer

    blocks = list()
    for x in res:
        mkpth = lambda cls: Relation.make_class_path(get_relation_mro(cls, x))
        newblock = el.join(map(mkpth, (a, b)))
        blocks.append(newblock)

    return (el + smallseparator + el).join(blocks)

# task 6
def dec_root_member(cls):
    res = get_root_members(cls)

    if not res: return 'That is already root class'
    convert_col = lambda arr: el.join(map(lambda x: x[0], arr))
    typegetter = lambda x: x[1].attribute_value 
    cols = _categorize_members(convert_col, typegetter, res.items())

    return el.join(filter(bool, cols))
