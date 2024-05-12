def count_file(filename):
    
    with open(filename, "r") as file:
        content = file.read()
        words = content.split()
        count = len(words)

    print(f"Total number of words in '{filename}': {count}")

filename = "xyz.txt"
count_file(filename)

