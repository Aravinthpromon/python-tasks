import os
import unittest
from files_in_given_directory import list_files

class TestListFiles(unittest.TestCase):
    
    def test_valid_directory_with_files(self):
        test_dir = r"C:\Users\Aravind\demo1"  
        list_files(test_dir)

        output_file = os.path.join(os.getcwd(), "file_list.txt")
        with open(output_file, "r") as f:
            content = f.read()

        self.assertIn("1.txt", content)
        self.assertIn("2.txt", content)
        self.assertNotIn("4", content)  

    def test_empty_directory(self):
        test_dir = r"C:\Users\Aravind\demo"  
        list_files(test_dir)

    
        output_file = os.path.join(os.getcwd(), "file_list.txt")
        with open(output_file, "r") as f:
           content = f.read()

        expected_output = f"Files in '{test_dir}':\nNo files found.\n" 
        self.assertEqual(content, expected_output)

    def test_invalid_directory(self):
        test_dir = r"C:\Users\Aravind\memo"  
        with self.assertRaises(FileNotFoundError):
            list_files(test_dir)

if __name__ == "__main__":
    unittest.main()