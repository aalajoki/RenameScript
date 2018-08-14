import os


def main():
    i = 1;

    while True:

        #dir = input("Enter the target directory: ")
        print("Welcome. Press CTRL + C to cancel anytime.")
        dir = dir_input()

        print("""
        (1) Rename everything
        (2) Rename all files
        (3) Rename all folders
        (4) Rename specific filetypes
        """)

        option = options()

        basename = input("Enter the new name: ")

        # Input: file extensions?
        # Everything except folders
        # Just folders
        # Specific filetypes
            # Input specific filetypes separated by a space


        # Display the chosen action, ask for confirmation
        if option == 1:
            for filename in os.listdir(dir):
                if filename == os.path.basename(__file__):
                    continue

                ext = os.path.splitext(dir + "/" + filename)[1]
                os.rename(dir + "/" + filename, dir + "/" + basename + str(i) + ext)
                i += 1

        elif option == 2:
            for filename in os.listdir(dir):
                if filename == os.path.basename(__file__) or os.path.isdir(dir + "/" + filename) == True:
                    continue

                ext = os.path.splitext(dir + "/" + filename)[1]
                os.rename(dir + "/" + filename, dir + "/" + basename + str(i) + ext)
                i += 1

        elif option == 3:
            for filename in os.listdir(dir):
                if filename == os.path.basename(__file__) or os.path.isdir(dir + "/" + filename) == False:
                    continue

                ext = os.path.splitext(dir + "/" + filename)[1]
                os.rename(dir + "/" + filename, dir + "/" + basename + str(i) + ext)
                i += 1

        #elif option == 4:
            # Enter extensions separated by a space
            # Do you want each extension to have its own numbering? For example, 1.jpg, 2.jpg, 1.png, 2.png

        else:
            print("asdasd")
            break
        i = 1
        # Catch errors?
        print("Files renamed. Thank you, come again.")
        # Do you want to continue? Y/N
        break

def dir_input():
    dir = input("Enter the target directory: ")
    if os.path.isdir(dir) == False:
        print("Directory not found. Please try again.")
        dir_input()
    else:
        return str(dir)

def options():
    option = int(input("What do you want to rename? (1-4): "))
    if option > 4 or option < 1:
        print("Invalid choice. Please try again.")
        options()
    else:
        return option


if __name__ == "__main__":
    main()
