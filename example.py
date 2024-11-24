def modify_content(content):
    # Modify the content; this example changes text to uppercase
    return content.upper()

def read_and_write_file():
    try:
        # Prompt the user for the filename to read from
        input_filename = input("Enter the filename to read from: ")
        
        # Attempt to open and read the file
        with open(input_filename, 'r') as file:
            content = file.read()
        
        # Modify the file content
        modified_content = modify_content(content)
        
        # Define the output filename and write modified content
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content has been saved to {output_filename}")
    
    # Handle the case where the file doesn't exist
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    
    # Handle other potential IO errors
    except IOError:
        print("Error: An issue occurred while reading the file.")

# Run the function
read_and_write_file()
