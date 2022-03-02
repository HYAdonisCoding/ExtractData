import sys

def extract(path):
    # 提取1,2,4,5,11,12,18，23，26列数据
    # path = "001.txt"  # 数据来源
    f = open(path)
    line = f.readline()
    list = []
    while line:
        a = line.split()
        # 12
        b = a[0:2]
        # 4,5
        c = b + a[3:5]
        # 11,12,
        d = c + a[10:12]
         # # 18，
        e = d + a[17:18]
        # # 23
        h = e + a[22:23]
        # # 26
        g = h + a[25:26]

        list.append(g)

        line = f.readline()
    f.close

    with open('result.txt', 'a') as month_file:  # 提取后的数据文件
        for tag in list:
            for i in tag:
                month_file.write(str(i))
                month_file.write(' ')
            month_file.write('\n')



def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and array[i] < array[l]:
        largest = 1
    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heapSort(array):
    n = len(array)
    for i in range(n//2, -1, -1):
        heapify(array, n, i)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return array
