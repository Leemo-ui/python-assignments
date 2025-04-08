def read_modify_and_write_file():
    filename = input("Please enter the filename: ")
    
    try:
        # Try to open and read the input file
        with open(filename, 'r') as infile:
            content = infile.read()
        
        # Modify the content (For example, convert to uppercase)
        modified_content = content.upper()
        
        # Ask for the output file name
        output_filename = input("Please enter the output filename: ")
        
        # Write the modified content to the output file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File has been read, modified, and written to {output_filename}")
    
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except IOError:
        print(f"Error: There was an issue reading or writing the file.")
