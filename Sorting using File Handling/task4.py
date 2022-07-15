inputTxt = open("input4.txt", "r")
outputTxt = open("output4.txt", "w")

file = inputTxt.readlines()
lst1 = []
lst1.append(file[0])
file.pop(0)
A = [int(x) for x in lst1]

lst2 = []
for i in file:
    lst2 = i.split(" ")
    lst2.append(i)
lst2.pop()
B = [int(x) for x in lst2]

def merge_sort(a):
    if len(a) > 1:
        low = 0
        up = 0
        mid = len(a) // 2
        low = a[:mid]
        up = a[mid:]

        merge_sort(low)
        merge_sort(up)

        i = 0
        j = 0
        k = 0

        while i < len(low) and j < len(up):
            if low[i] < up[j]:
                a[k] = low[i]
                i = i + 1
            else:
                a[k] = up[j]
                j = j + 1
            k = k + 1

        while i < len(low):
            a[k] = low[i]
            i = i + 1
            k = k + 1
        while j < len(up):
            a[k] = up[j]
            j = j + 1
            k = k + 1

merge_sort(B)

for i in range(0, len(B)):
    outputTxt.write(str(B[i]) + " ")