
f1 = open("sanidhya.txt")

try:
    f = open("does2.txt")

except EOFError as e:
    print("Print eof error aa gaya hai", e)

except IOError as e:
    print("Print IO error aa gaya hai", e)

else:
    print("This will run only if except is not running")

finally:
    print("Run this anyway...")
    """ye wala try block f ko try karne k liye wo file close ho rahi h ya nhi qki exsist karri h ya nhi pata karna h
"""
    try:
        f.close()
        f1.close()
    except Exception as e:
        print("file not found",e)
print("Important stuff")
