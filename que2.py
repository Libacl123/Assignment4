try:
    with open("abx.txt","r") as file:
        do = file.read()
        print("file content:",do)
except FileNotFoundError:
    print("Error:File not found!")