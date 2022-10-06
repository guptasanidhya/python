import os
def soilder(path,file,format):
    os.chdir(path)
    i=1
    files=os.listdir(path)
    with open(file) as f:
        filelist=f.read().split("\n")

    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())

        if os.path.splitext(file)[1]==format:
            os.rename(file,f"{i}{format}")
            i+=1

if __name__ == '__main__':
    path=input("Enter the path of the folder you want to edit in")
    print(f"is path exist? {os.path.exists(path)}")
    filename=input("enter the name of the file with extension to be checked")
    print(f"is file exists{os.path.isfile(filename)}")
    format=input("enter the format or extension ")
    soilder(path,filename,format)


