abc = {2, 6, 8, 3}  # tuple is immutable

# abc.update([1, 4, 5])
c = tuple(abc)
print(type(c))


# print(dir(abc))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update'