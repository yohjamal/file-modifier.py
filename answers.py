#question 1 Create a program that reads a file and writes a modified version to a new file.
def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
            modified_content = content.upper()  # Example modification: convert to uppercase
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to '{output_filename}'")
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read/write to file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


#question 2 create a program that asks the user for a filename and handle errors if it doesn’t exist or can’t be read.
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)  
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"Error: The file '{filename}' cannot be read.")  
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
def main():
    filename = input("Enter the filename to read: ").strip()
    read_file(filename) 
if __name__ == "__main__":
    main() 
