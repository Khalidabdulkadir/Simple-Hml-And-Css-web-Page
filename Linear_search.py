def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    else:
        return None
    
def verify(index):
    if index is not None:
        print("The index was found at:", index)
    else:
        print("Index Was not Found")
numbers = [1, 2,3,4,5,6,7,8,9,10]
result = linear_search(numbers, 9)
verify(result)
