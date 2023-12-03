# Open the file and save it into a variable
file = open("my_file.txt")
# Read the file, return it as a string and save it into another variable
contents = file.read()
print(contents)
# Close the file to save resources/spaces/rams
file.close()

"""
Using this method, we don't have to worry about forgotten to close the file
as it will do it automatically

mode:
"r" = read the content inside the text file
"w" = write into the text file but will replace the whole content inside 
"a" = append the content into the text file 

with open("my_file_2.txt", mode = "w") as file:
file.write("I don't like durian")

<if the text file doesn't exist, it will create the text file> 
"""
with open("my_file_2.txt", mode="a") as file:
    file.write("\nI don't like durian")

with open("my_file_2.txt",) as file:
    contents = file.read()
    print(contents)


