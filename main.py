#Karol Stajer

import random, time, os

def insertionSort(myList):
    for i in range(len(myList)):
        min = myList[i]
        for j in range(i, len(myList)):
            if myList[j] <= min:
                min = myList[j]
                index = j
        myList[index] = myList[i]
        myList[i] = min

    return myList

def bubbleSort(myList):
    n = len(myList) - 1
    for j in range(len(myList)):
        for i in range(n-j):
            if myList[i] > myList[i + 1]:
                temp = myList[i]
                myList[i] = myList[i + 1]
                myList[i + 1] = temp
    return myList

def quickSort(myList):
    less = []
    equal = []
    greater = []

    if len(myList) > 1:
        pivot = myList[random.randint(0, len(myList) - 1)]
        for x in myList:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        return quickSort(less) + equal + quickSort(greater)
    else:
        return myList

def heapify(myList, n, i):
    max = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and myList[i] < myList[left]:
        max = left
    if right < n and myList[max] < myList[right]:
        max = right

    if max != i:
        myList[i], myList[max] = myList[max], myList[i]
        heapify(myList, n, max)

def heapSort(myList):
    n = len(myList)

    for i in range(n // 2 - 1, -1, -1):
        heapify(myList, n, i)

    for i in range(n - 1, 0, -1):
        myList[i], myList[0] = myList[0], myList[i]
        heapify(myList, i, 0)

    return myList

def mergeSort(myList):
    if len(myList) > 1:

        middle = len(myList)//2
        leftSide = myList[:middle]
        rightSide = myList[middle:]

        mergeSort(leftSide)
        mergeSort(rightSide)
        i = 0
        j = 0
        k = 0
        while i < len(leftSide) and j < len(rightSide):
            if leftSide[i] < rightSide[j]:
                myList[k] = leftSide[i]
                i += 1
            else:
                myList[k] = rightSide[j]
                j += 1
            k += 1

        while i < len(leftSide):
            myList[k] = leftSide[i]
            i += 1
            k += 1
        while j < len(rightSide):
            myList[k] = rightSide[j]
            j += 1
            k += 1
    return myList

print("Size of a list filled with random numbers: ")
size = int(input())

print("Number of repetitions: ")
n = int(input())

t1 = [0] * n
t2 = [0] * n
t3 = [0] * n
t4 = [0] * n
t5 = [0] * n

insertionTime = bubbleTime = quickTime = heapTime = mergeTime = 0

max1 = max2 = max3 = max4 = max5 = 0
min1 = min2 = min3 = min4 = min5 = 0

os.system('clear')

for i in range(n):
    myList = [0] * size
    myList2 = myList3 = myList4 = myList5 = myList

    for j in range(size):
        myList[j] = random.randint(1, size)

    startTime = time.time()
    insertionSort(myList)
    t1[i] = round(time.time() - startTime, 4)
    insertionTime += t1[i]
    print("Insertion sort done [{}/{}]".format(i+1, n))

    startTime = time.time()
    bubbleSort(myList2)
    t2[i] = round(time.time() - startTime, 4)
    bubbleTime += t2[i]
    print("Bubble sort done [{}/{}]".format(i+1, n))

    startTime = time.time()
    quickSort(myList3)
    t3[i] = round(time.time() - startTime, 4)
    quickTime += t3[i]
    print("Quick sort done [{}/{}]".format(i+1, n))

    startTime = time.time()
    heapSort(myList4)
    t4[i] = round(time.time() - startTime, 4)
    heapTime += t4[i]
    print("Heap sort done [{}/{}]".format(i+1, n))

    startTime = time.time()
    mergeSort(myList5)
    t5[i] = round(time.time() - startTime, 4)
    mergeTime += t5[i]
    print("Merge sort done [{}/{}]\n".format(i+1, n))



insertionTime /= n
bubbleTime /= n
quickTime /= n
heapTime /= n
mergeTime /= n

heapSort(t1)
heapSort(t2)
heapSort(t3)
heapSort(t4)
heapSort(t5)

print ("---------- INSERTION SORT ----------")
print ("Average time: {}s".format(round(insertionTime, 8)))
print ("Best sorting time: {}s".format(t1[0]))
print ("Worst sorting time: {}s".format(t1[n-1]))

print ("----------- BUBBLE SORT ------------")
print ("Average time: {}s".format(round(bubbleTime, 8)))
print ("Best sorting time: {}s".format(t2[0]))
print ("Worst sorting time: {}s".format(t2[n-1]))

print ("------------ QUICK SORT ------------")
print ("Average time: {}s".format(round(quickTime, 8)))
print ("Best sorting time: {}s".format(t3[0]))
print ("Worst sorting time: {}s".format(t3[n-1]))

print ("------------ HEAP SORT -------------")
print ("Average time: {}s".format(round(heapTime, 8)))
print ("Best sorting time: {}s".format(t4[0]))
print ("Worst sorting time: {}s".format(t4[n-1]))

print ("------------ MERGE SORT ------------")
print ("Average time: {}s".format(round(mergeTime, 8)))
print ("Best sorting time: {}s".format(t5[0]))
print ("Worst sorting time: {}s".format(t5[n-1]))





