import os

# Directory path where you want to create the files
directory = "D:\\TestFiles"  # Change to your desired path

# Check if the directory exists and create it if it doesn't
if not os.path.exists(directory):
    os.makedirs(directory)

# Create 100 files with different names
for i in range(1, 101):
    file_name = f"file{i}.txt"
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as file:
        file.write(f"This is file number {i}.")
    print(f"File {file_name} has been successfully created.")
