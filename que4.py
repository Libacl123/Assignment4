def create_file(filename, content):
  
  with open(filename, "w") as file:
    file.write(content)
  print(f"File '{filename}' created successfully!")


filename = "xyz.txt"
content = "This is my new file."
create_file(filename,content)
