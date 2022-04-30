input=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flatten(lst, out=[]):
    for item in lst:
        if type(item)==list:
            flatten(item)
        else:
            out.append(item)
    return out            
print(flatten(input))

input = [[1, 2], [3, 4], [5, 6, 7]]

def reverse(lst, out=[]):
    reversed_list=[elem[::-1] for elem in input]
    return reversed_list.reverse()
print(reverse(input))
