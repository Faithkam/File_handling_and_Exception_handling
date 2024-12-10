import os

# f = open('MyData.txt', 'r')
#print(f.read())

#print(f.readline())
#print(f.readline())

#for line in f:
    #print(line)

# f.close()

# Append the file
# f = open('MyData.txt', 'a')
# f.write('I love coding!')
# f.close()

# f = open('MyData.txt', 'r')
# print(f.read())
# f.close()

# create a new file and write on it, create one if it doesnt exist
# f = open('content.txt', 'w')
# f.close()

#creates the specified file, but returns an error if the file exists
# if not os.path.exists('faith.txt'):
#     f = open('faith.txt', 'x')
#     f.close()

# delete a file

# avoid an error if it doesnt exist
# if os.path.exists('faith.txt'):
#     os.remove('faith.txt')
# else: print('The file you wish to delete does not exist')





# open the file in read mode
# with open('MyData.txt') as f:
#     #read the content of the file
#     content = f.read()

# modify the content (ie convert to uppercase)
# modified_content = content.upper()


# open another file in write mode
# with open('content.txt', 'w') as f:
#     #write the modifed content to the file
#     f.write(modified_content)




def modify_file():
    input_file = input("Please enter the name of the file to read: ")
    
    try:
        # Open the input file in read mode
        with open('MyData.txt', 'r') as file:
            # Read the content of the file
            content = file.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Open the output file in write mode
        output_file = "modified_" + input_file
        with open('error_handling.txt', 'w') as file:
            # Write the modified content to the file
            file.write(modified_content)
        
        print(f"File 'MyData.txt' has been modified and saved as 'error_handling.txt'.")
    
    except FileNotFoundError:
        print(f"The file 'MyData.txt' does not exist.")
    except IOError:
        print(f"The file 'MyData.txt' cannot be read.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
modify_file()


    