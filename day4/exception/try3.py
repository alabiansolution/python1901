try:
    handle = open("textfile.txt", "r")
except FileNotFoundError as a:
    print(a)
