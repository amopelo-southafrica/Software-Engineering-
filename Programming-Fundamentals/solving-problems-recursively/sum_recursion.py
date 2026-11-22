def adding_up_to(list,index_point):
    if index_point == 0:
        return list[0]
    return index_point + adding_up_to(list, index_point - 1)
print(adding_up_to([2,3,4,5],5))