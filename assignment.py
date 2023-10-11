import os

# Get the file name from the user
file_name = input("Enter the file name: ")

# Split the file name into the file name and extension
file_name, extension = os.path.splitext(file_name)

# Print the extension of the file
print("The extension of the file is:", extension)
