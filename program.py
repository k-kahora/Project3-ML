import sys

def copy_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            data = file.read()
        
        # Open the output file in write mode
        with open(output_file, 'w') as file:
            file.write(data)
            
        print("File has been copied successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        copy_file(input_file, output_file)
