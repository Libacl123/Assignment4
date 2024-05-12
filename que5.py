def read_file(filename):
    with open(filename,"r") as file:
        for line in file:
             print(line.rstrip())

filename = "poem.txt"
read_file(filename)       