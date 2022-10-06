import os
def soilder(path,filename):
    os.chdir(path)
    print(f"we are in {os.getcwd()}")
    f=open(filename,"r")
    filelist=f.read().split("\n")
    print(filelist)
    for item in filelist:
        output=item.title()
        outputlist.append(output)
        print(output)
    f.close()
    o=open(filename,"w")
    for item in outputlist:
         o.writelines(item)
         o.writelines("\n")
    o.close()



if __name__ == '__main__':
    # path=input("Enter the path of the folder you wanna edit in")
    # print(os.path.exists(path))
    # filename=input("Enter the filename you wanna edit in")
    # print(os.path.exists(filename))
    outputlist=[]
    path="E://Study//Extra//Python Projects//Preetify My Folder"
    filename="sanidhya.txt"
    soilder(path,filename)
    print(outputlist)
