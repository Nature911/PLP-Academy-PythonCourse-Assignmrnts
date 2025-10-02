

# Reading the content of a file input.txt

try:
        with open("input.txt", "r") as file:
                content = file.read()
                print(content)

        # Writing to a new file
        with open("newfile.txt", "w") as file:
                file.write(content)
                file.write("\nThe End")

        # Reading back the modified file
        with open("newfile.txt", "r") as file:
                content_modified = file.read()
                print(content_modified)

except FileNotFoundError:
        print(f"files nit found. Please check the filename")



