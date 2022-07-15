inputTxt = open("input3.txt", "r")
outputTxt = open("output3.txt", "w")

file = inputTxt.readlines()
lst1 = []
lst2 = []
lst3 = []
lst1.append(file[0])
lst2.append(file[1])
lst3.append(file[2])

for i in lst1:
    lst1N = i.split(" ")
    lst1N.append(i)
lst1N.pop()
A = [int(x) for x in lst1N]
for i in lst2:
    lst2N = i.split(" ")
    lst2N.append(i)
lst2N.pop()
B = [int(x) for x in lst2N]
for i in lst3:
    lst3N = i.split(" ")
    lst3N.append(i)
lst3N.pop()
C = [int(x) for x in lst3N]

sheet = {}
for key in B:
    for value in C:
        sheet[key] = value
        C.remove(value)
        break

def insertion_sort(my_dict):
    arr = list(my_dict.values())
    new_dict={}
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    for j in reversed(arr):
        new_dict[list(my_dict.keys())[list(my_dict.values()).index(j)]] = j
    return new_dict

sheet1 = insertion_sort(sheet)

for keys in sheet1:
    outputTxt.write(str(keys) + " ")