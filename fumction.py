"""
Function to create a text file with the current timestamp
and write the timestamp into the file.
"""
import datetime
def create_file_with_timestamp():

# Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Create a file with the current timestamp
    filename = f"timestamp_{current_timestamp}.txt"

# Write the timestamp into the file
    with open(filename, "w") as file:
        file.write(current_timestamp)

    print(f"File '{filename}' with the current timestamp created successfully.")

# Call the function to create the file
create_file_with_timestamp()


"""
Function to read from a text file and display its content in the console.
"""
def read_text_file(filename):
    try:
# Open the text file in read mode ('r')
        with open(filename, 'r') as file:
# Read all the lines from the file and store them in a list
            lines = file.readlines()
            
# Iterate through each line in the list of lines
            for line in lines:
# Display each line in the console
                print(line, end='')
    except FileNotFoundError:
# If the file is not found, display an error message
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
# If any other error occurs, display a generic error message
        print(f"Error: {e}")
# Call the function and pass the filename 'example.txt' as an argument
read_text_file('example.txt')
