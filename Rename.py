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
            # WIP: Display the chosen action, ask for confirmation
            for filename in os.listdir(dir):
                if filename == os.path.basename(__file__) or os.path.isdir(dir + "/" + filename) == True:
                    continue

                # Get extension from the file for renaming
                ext = os.path.splitext(dir + "/" + filename)[1]
                # Rename file
                os.rename(dir + "/" + filename, dir + "/" + newname + str(i) + ext)
                i += 1

        # Rename all folders
        elif option == "2":
            # WIP: Display the chosen action, ask for confirmation

            for filename in os.listdir(dir):
                if filename == os.path.basename(__file__) or os.path.isdir(dir + "/" + filename) == False:
                    continue

                ext = os.path.splitext(dir + "/" + filename)[1]

                # Rename file and reset counter
                os.rename(dir + "/" + filename, dir + "/" + newname + str(i) + ext)
                i += 1

        # Rename files with specific extensions
        elif option == "3":
            exts = input('Enter all extensions of the files you want to rename. Separate them with spaces (e.g."jpg png"): ')
            # WIP: Display the chosen action, ask for confirmation
            exts_list = exts.split()

            # Prepare specified extensions for comparison
            exts_list = ["." + e.lower() for e in exts_list]


            for filename in os.listdir(dir):
                ext = os.path.splitext(dir + "/" + filename)[1]

                # Ignore the script, folders and files without a specified extension
                if filename == os.path.basename(__file__) or os.path.isdir(dir + "/" + filename) == True or ext.lower() not in exts_list:
                    continue

                # Rename file and reset counter
                os.rename(dir + "/" + filename, dir + "/" + newname + str(i) + ext)
                i += 1

        # Rename everything
        elif option == "4":
            # WIP: Display the chosen action, ask for confirmation
            for filename in os.listdir(dir):
                if filename == os.path.basename(__file__):
                    continue

                ext = os.path.splitext(dir + "/" + filename)[1]
                os.rename(dir + "/" + filename, dir + "/" + newname + str(i) + ext)
                i += 1

        # Cancel
        elif option == "5":
            print("Thank you, come again.")
            sys.exit()

        # Debug
        else:
            print("Whoopsy daisy")



        i = 1
        # Catch errors?
        print("Files renamed.")
        # Do you want to continue? Y/N
        continue_query()

        new_dir = change_dir_query()







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
    continuation = input("Do you want to continue? Y/N: ")
    if continuation.lower() == "y":
        pass
    elif continuation.lower() == "n":
        print("Thank you, come again.")
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        continue_query()

def change_dir_query():
    change_dir = input("Do you want to change target directory? Y/N: ")
    if change_dir.lower() == "y":
        return True
    elif change_dir.lower() == "n":
        return False
    else:
        print("Invalid choice. Please try again.")
        change_dir_query()


if __name__ == "__main__":
    main()
