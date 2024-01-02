from pathlib import Path
fileData = Path("C:\\Users\\Administrator\\Desktop\\xingQingUI")
#for i in fileData.iterdir():
    # print(i)

#递归遍历说有png(包含子目录)
#for i in fileData.rglob("*.png"):
#    print(i)

#遍历所有png (不包括子目录)
#for i in fileData.glob("*.png"):
#    print(i)

#遍历所有文件(包括子目录)
for i in fileData.glob("**/*"):
    print(i)
