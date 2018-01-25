with open("text.txt", "w") as my_file:
  my_file.write("My Data!")
  
if not file.closed:
  file.close()

print my_file.closed
