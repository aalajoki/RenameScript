import os
import sys

def main():
    # The numbering for renamed files
    i = 1
    # Used for checking if user wants to change directory
    new_dir = True
    # For the main script loop

    print("Welcome.")

    while True:

        # If user runs the script for the first time
        if new_dir == True:
            dir = dir_query()


        print("""
        -- Select your operation --
    (1) Rename all files
    (2) Rename all folders
    (3) Rename files with specific extensions
    (4) Rename everything
    (5) Exit
                """)
        # 1-5 from user
        option = options_query()

        if (option != "5"):
            newname = input("Enter the new name: ")

        # Rename all files
        if option == "1":
            # Ask for confirmation
            print("""
        You are about to name all files in:

        """ + dir + """

        to  ''""" + newname + "'\n")

            confirm = confirm_query()
            if (confirm == True):

                for filename in os.listdir(dir):
                    if filename == os.path.basename(__file__) or os.path.isdir(dir + "/" + filename) == True:
                        continue

                    # Get extension from the file for renaming
                    ext = os.path.splitext(dir + "/" + filename)[1]
                    # Rename file
                    os.rename(dir + "/" + filename, dir + "/" + newname + str(i) + ext)
                    i += 1
                print("Files renamed.")





        # Rename all folders
        elif option == "2":
            # Ask for confirmation
            print("""
        You are about to name all folders in:

        """ + dir + """

        to  '""" + newname + "'\n")

            confirm = confirm_query()
            if (confirm == True):

                for filename in os.listdir(dir):
                    # Ignore the script and non-folders
                    if filename == os.path.basename(__file__) or os.path.isdir(dir + "/" + filename) == False:
                        continue

                    # Store old extension
                    ext = os.path.splitext(dir + "/" + filename)[1]

                    # Rename file
                    os.rename(dir + "/" + filename, dir + "/" + newname + str(i) + ext)
                    i += 1
                print("Files renamed.")





        # Rename files with specific extensions
        elif option == "3":
            exts = input('Enter all extensions of the files you want to rename. Separate them with spaces (e.g."jpg png"): ')

            # Ask for confirmation
            print("""
        You are about to name all files with the following extensions:

        """ + exts +
        """

        in """ + dir + """

        to '""" + newname + "'\n")

            confirm = confirm_query()
            if (confirm == True):

                # Split given extensions into a list
                exts_list = exts.split()

                # Prepare specified extensions for comparison
                exts_list = ["." + e.lower() for e in exts_list]


                for filename in os.listdir(dir):
                    # Store old extension
                    ext = os.path.splitext(dir + "/" + filename)[1]

                    # Ignore the script, folders and files without a specified extension
                    if filename == os.path.basename(__file__) or os.path.isdir(dir + "/" + filename) == True or ext.lower() not in exts_list:
                        continue

                    # Rename file
                    os.rename(dir + "/" + filename, dir + "/" + newname + str(i) + ext)
                    i += 1
                print("Files renamed.")





        # Rename everything
        elif option == "4":
            # Ask for confirmation
            print("""
        You are about to name everything in:

        """ + dir + """

        to  '""" + newname + "'\n")

            confirm = confirm_query()
            if (confirm == True):

                for filename in os.listdir(dir):
                    # Ignore the script
                    if filename == os.path.basename(__file__):
                        continue

                    # Store old extension
                    ext = os.path.splitext(dir + "/" + filename)[1]
                    # Rename
                    os.rename(dir + "/" + filename, dir + "/" + newname + str(i) + ext)
                    i += 1
                print("Files renamed.")

        # Cancel
        elif option == "5":
            print("Thank you, come again.")
            sys.exit()

        # Reset counter for numbering
        i = 1

        # Do you want to continue? Y/N
        continue_query()

        new_dir = change_dir_query()





def confirm_query():
    confirm = input("Continue? (Y/N): ")
    if confirm.lower() == "y":
        return True
    elif confirm.lower() == "n":
        return False
    else:
        print("Invalid choice. Please try again.")
        confirm_query()


def dir_query():
    dir = input("Enter the target directory: ")
    if os.path.isdir(dir) == False:
        print("Directory not found. Please try again.")
        dir_query()
    else:
        return str(dir)


def options_query():
    option = input("What do you want to rename? (1-5): ")

    if option not in ["1","2","3","4","5"]:
        print("Invalid choice. Please try again.")
        options_query()
    else:
        return option


def continue_query():
    continuation = input("Do you want to continue renaming files? (Y/N): ")
    if continuation.lower() == "y":
        pass
    elif continuation.lower() == "n":
        print("Thank you, come again.")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        continue_query()


def change_dir_query():
    change_dir = input("Do you want to change target directory? (Y/N): ")
    if change_dir.lower() == "y":
        return True
    elif change_dir.lower() == "n":
        return False
    else:
        print("Invalid choice. Please try again.")
        change_dir_query()


if __name__ == "__main__":
    main()
