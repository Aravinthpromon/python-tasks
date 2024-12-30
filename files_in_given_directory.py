import os

def list_files(directory):
    try:
        if not os.path.exists(directory):
            raise FileNotFoundError(f"Directory not found: {directory}")

        items = os.listdir(directory)
        files = []

        for item in items:
            full_path = os.path.join(directory, item)
            if os.path.isfile(full_path):
                files.append(item)

        write_to_file(directory, files)

    except FileNotFoundError as e:
        print(e)
        raise

def write_to_file(directory, files):
    output_file = os.path.join(os.getcwd(), "file_list.txt")  
    with open(output_file, "w") as file_writer:
        content = f"Files in '{directory}':\n"
        if not files:
            content += "No files found.\n"
        else:
            content += "\n".join(f"{file}" for file in files) + "\n"
        file_writer.write(content)

    print(f"File list has been written to: {output_file}")


if __name__ == "__main__":
    directory_path = input("Enter the path of the directory to list files: ")
    list_files(directory_path)
