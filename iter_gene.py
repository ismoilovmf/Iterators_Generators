nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
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

for i in flat_generator(nested_list):
    print(i)

class FlatIterator:
    def __init__(self, lst):
        self.lst = lst
        self.cursor = -1
        self.next_cursor = 0
        self.end = len(self.lst)

    def __iter__(self):
        self.next_cursor = 0
        self.cursor += 1
        return self

    def __next__(self):
        if self.next_cursor == len(self.lst[self.cursor]):
            iter(self)
        self.next_cursor += 1
        if self.cursor == self.end:  # условие выход из цикла
            raise StopIteration  # выход из цикла
        return self.lst[self.cursor][self.next_cursor - 1]
    
for item in FlatIterator(nested_list):
    print(item)


    
