import os
import unittest
from dict_files_and_directories import list_files_and_directories

class TestListFilesAndDirectories(unittest.TestCase):

    def test_valid_directory_with_files_and_dirs(self):
        test_dir = r"C:\Users\Aravind\demo1"  
        list_files_and_directories(test_dir)

        
        output_file = os.path.join(os.getcwd(), "files_and_directories.txt")
        with open(output_file, "r") as f:
            content = f.read()

        self.assertIn("Files:", content)
        self.assertIn("Directories:", content)
        self.assertIn("1.txt", content)  
        self.assertIn("2.txt", content)  
        self.assertIn("D", content)  

    
        self.assertNotIn("A", content)
        self.assertNotIn("B", content)

    def test_empty_directory(self):
        test_dir = r"C:\Users\Aravind\demo"  
        list_files_and_directories(test_dir)

        output_file = os.path.join(os.getcwd(), "files_and_directories.txt")
        with open(output_file, "r") as f:
            content = f.read()

        self.assertIn("Files:", content)
        self.assertIn("Directories:", content)
        self.assertNotIn("1.txt", content)  
        self.assertNotIn("subfolder", content)  

    def test_invalid_directory(self):
        test_dir = r"C:\Users\Aravind\memo"  
        with self.assertRaises(FileNotFoundError):  
            list_files_and_directories(test_dir)

if __name__ == "__main__":
    unittest.main()
