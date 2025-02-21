from CodingPickleFile.FileUtil import FileUtil

list=FileUtil.loadModel("mydata.dat")
for p in list:
    print(p)