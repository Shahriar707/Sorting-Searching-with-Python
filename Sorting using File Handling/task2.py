inputTxt = open("input2.txt", "r")
outputTxt = open("output2.txt", "w")

file = inputTxt.readlines()
lst1 = []
lst2 = []
lst1.append(file[0])
file.pop(0)
lst2 = file

lst1N = []
for i in lst1:
    lst1N = i.split(" ")
    lst1N.append(i)
lst1N.pop()
A = [int(x) for x in lst1N]

lst2N = []
for i in lst2:
    lst2N = i.split(" ")
    lst2N.append(i)
lst2N.pop()
B = [int(x) for x in lst2N]

M = min(A)
N = max(A)

def selection_sort(a):
    for i in range(len(a)-1):
        minIndex = i
        for j in range(i+1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        if i != minIndex:
            a[i], a[minIndex] = a[minIndex], a[i]

selection_sort(B)

for i in range(0, M):
    outputTxt.write(str(B[i]) + " ")