import os


def main():
    i = 1;

    while True:

        #dir = input("Enter the target directory: ")
        print("Welcome. Press CTRL + C to cancel anytime.")
        dir = dir_input()

        #print("""
        #(1) Rename everything
        #(2) Rename all files
        #(3) Rename all folders
        #(4) Rename files with specific extensions
        #""")

        print("""
    (1) Rename all files
    (2) Rename all folders
    (3) Rename files with specific extensions
    (4) Rename everything
                """)

        option = options()

        basename = input("Enter the new name: ")


        if option == 1:
            # Display the chosen action, ask for confirmation
            for filename in os.listdir(dir):
                if filename == os.path.basename(__file__) or os.path.isdir(dir + "/" + filename) == True:
                    continue

                ext = os.path.splitext(dir + "/" + filename)[1]
                os.rename(dir + "/" + filename, dir + "/" + basename + str(i) + ext)
                i += 1

        elif option == 2:
            # Display the chosen action, ask for confirmation
            for filename in os.listdir(dir):
                if filename == os.path.basename(__file__) or os.path.isdir(dir + "/" + filename) == False:
                    continue

                ext = os.path.splitext(dir + "/" + filename)[1]
                os.rename(dir + "/" + filename, dir + "/" + basename + str(i) + ext)
                i += 1

        elif option == 3:
            exts = input("Enter all extensions of the files you want to rename. Separate them with spaces: ")
            # Do you want each extension to have its own numbering? For example, 1.jpg, 2.jpg, 1.png, 2.png
            # Display the chosen action, ask for confirmation
            exts_list = exts.split()

            exts_list = ["." + e.lower() for e in exts_list]

            print(exts_list)

            for filename in os.listdir(dir):
                ext = os.path.splitext(dir + "/" + filename)[1]

                if filename == os.path.basename(__file__) or os.path.isdir(dir + "/" + filename) == True or ext.lower() not in exts_list:
                    continue

                os.rename(dir + "/" + filename, dir + "/" + basename + str(i) + ext)
                i += 1

        elif option == 4:
            for filename in os.listdir(dir):
                if filename == os.path.basename(__file__):
                    continue

                ext = os.path.splitext(dir + "/" + filename)[1]
                os.rename(dir + "/" + filename, dir + "/" + basename + str(i) + ext)
                i += 1


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
