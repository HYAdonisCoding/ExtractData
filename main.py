import os
import extract
# 提取1,2,4,5,11,12,18，23，26列数据
path = "202110"  # 数据来源
dirs = os.listdir(path)

# for file in dirs:
#     print(file)
dirsList = []
for root, dirs, files in os.walk(path):
    for name in files:
        if name.endswith("_H"):
        # if name.endswith(".txt") == False:
            print(os.path.join(root, name))
            # 调用方法
            # extract.extract(os.path.join(root, name))

    for name in dirs:
        if name.endswith("_H"):
            d = os.path.join(root, name)
            dirsList.append(d)
            print(d)

print("----------------------")
dirsList = sorted(dirsList)
fileCount = 0

for file in dirsList:
    # 文件数组
    fileList = []
    for subfile in os.listdir(file):
        fileCount += 1
        d = os.path.join(file, subfile)
        # print(d)
        fileList.append(d)
    
    fileList = sorted(fileList)
    print(file, "----------------------")
    print(fileList)
    for t in fileList:
        # 调用方法
        extract.extract(t)



