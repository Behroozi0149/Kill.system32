import os
directory = "D:\\TestFiles"
if not os.path.exists(directory):
    os.makedirs(directory)
for i in range(1, 101):
    file_name = f"file{i}.txt"
    file_path = os.path.join(directory, file_name)
    with open(file_path, 'w') as file:
        file.write(f"This is file number {i}.")
    print(f"File {file_name} has been successfully created.")
#don't run