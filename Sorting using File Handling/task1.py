inputTxt = open("input1.txt", "r")
outputTxt = open("output1.txt", "w")

file = inputTxt.readlines()

A = []
A.append(file[0])
file.pop(0)
C = []
for i in file:
    C = i.split(" ")
    C.append(i)
C.pop()
D = [int(x) for x in C]

def bubble_sort(a):
    for i in range(len(a)):
        swaps = 0
        for j in range(0, len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps = swaps + 1

        if swaps == 0:
            break

bubble_sort(D)

for i in range(len(D)):
    outputTxt.write(str(D[i]) + " ")


# now to optimise the bubble sort code in such a way that the time complexity for the best case scenario is O(n)
# to do that I used a variable called "swaps" to count how many swaps are happening within the inner loop.
# if no swaps happends within the inner loop; the break keyword will terminate the execution beacuse the loop is already sorted