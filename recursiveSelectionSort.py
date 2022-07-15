def insertion_sort(a, i, n):
    if len(a) == 0:
        return a

    temp = a[i]
    j = i - 1

    while j >= 0 and a[j] > temp:
        a[j+1] = a[j]
        j = j-1
    a[j+1] = temp

    if i+1 <= n:
        insertion_sort(a, i+1, n)

a = [30,20,15,23,-2,56,-5]
insertion_sort(a, 1, len(a)-1)
print(a)