my_list = [1,2,3,4]
add = my_list.append(5)
print("added list:",my_list)
try:
    index = int(input("enter the index: "))
    element = my_list[index]
    print("The element at index", index, "is:", element)
except IndexError:
     print("Error: Index out of range!")



