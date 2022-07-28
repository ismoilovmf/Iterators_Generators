nested_list = [1, 2,
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None], 3
]

def flat_generator(lst):
    i = 0
    while i < len(lst):
        if isinstance(lst[i], list):
            for j in flat_generator(lst[i]):
                yield j
        else:
            yield lst[i]
        i += 1


# for i in flat_generator(nested_list):
#     print(i)

def FlatIterator1(lst):
    i = 0
    it = iter(lst)
    while i < len(lst):
        i += 1
        el = next(it)
        if isinstance(el, list):
            j = 0
            it_el = iter(el)
            while j < len(el):
                j += 1
                el_el = next(it_el)
                # if isinstance(el_el, lst):
                #     yield FlatIterator(el_el)
                yield el_el
            
        else:
            yield el



for j in FlatIterator(nested_list):
    print(j)