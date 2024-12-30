import os  

def list_files_and_directories(directory):
    
    if not os.path.exists(directory):  
        raise FileNotFoundError(f"Directory not found: {directory}")  
        

    result = {
        "files": [],
        "directories": []
    }

    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)  

        if os.path.isfile(full_path):  
            result["files"].append(item)
        elif os.path.isdir(full_path):  
            result["directories"].append(item)

    
    output_file = os.path.join(os.getcwd(), "files_and_directories.txt")
    
    with open(output_file, "w") as file_writer:
        file_writer.write("Files and Directories List:\n")
        file_writer.write("\nFiles:\n")
        for file in result["files"]:
            file_writer.write(f"  {file}\n")
        file_writer.write("\nDirectories:\n")
        for directory in result["directories"]:
            file_writer.write(f"  {directory}\n")
    
    print(f"Files and directories list has been written to: {output_file}")


if __name__ == "__main__":
    directory_path = input("Enter the path of the directory to list files and directories: ")
    list_files_and_directories(directory_path)
