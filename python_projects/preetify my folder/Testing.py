
# Oh soldier Prettify my Folder

# path, dictionary file, format

# def soldier("C://", "harry.txt", "jpg")

import os
def soldier(path, file, format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    # print(files)
    with open(file) as f:
        filelist = f.read().split("\n")
        # print(filelist)
        """The split() method in Python returns a list of the words in the string/line ,
         separated by the delimiter string.
         This method will return one or more new strings. 
         All substrings are returned in the list datatype."""
    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        """os.path.splitext() method in Python is used to split the path name into a pair root and ext.
         Here, ext stands for extension and has the extension portion of the specified path while root is
          everything except ext part.
        ext is empty if specified path does not have any extension. 
        If the specified path has leading period (‘.’), it will be ignored."""
        if os.path.splitext(file)[1] == format:
            """[0] means the before . and [1] means part after ."""
            # print(os.path.splitext(file)[0])
            print(os.path.splitext(file)[1])
            os.rename(file, f"{i}{format}")
            i +=1

if __name__ == '__main__':
    path="E://Study//Extra//Python Projects//Preetify My Folder"
    filepath="sanidhya.txt"
    soldier(path,filepath,".jpg")

