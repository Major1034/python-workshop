#myset1={1,2,3,4,5}
# my_set.add(7)#add the element in the set
# my_set.remove(3)
# my_set.discard(98)
# print(my_set)


#myset2={"g","f",12,3,4,21}
#a=myset1.union(myset2)
#print(a)
# def find_intersection(set8,set9):
#     intersection=set8.intersection(set9)
#     return intersection
# set8={"a","b","c"}
# set9={"a","d"}
# intersection=find_intersection(set8,set9)
# print(intersection)
def find_difference(set8,set9):
    difference=set8.difference(set9)
    return difference
set8={"a","b","c"}
set9={"a","d"}
difference=find_difference(set8,set9)
print(difference)