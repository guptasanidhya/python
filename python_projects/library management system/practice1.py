user = input("name of user who lend the book")
ls.append(lend)
lenddic = {f" {item + 1}.{user} ": i for item, i in enumerate(ls)}
print(lenddic)