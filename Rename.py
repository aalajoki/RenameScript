import os


def main():
    i = 1;

    while True:

        dir = input("Enter the target directory: ")

        #dir = dir_input()

        basename = input("Enter the new name: ")

        # Input: file extensions?
        # Everything except folders
        # Just folders
        # Specific filetypes
            # Input specific filetypes separated by a space

        for filename in os.listdir(dir):
            if filename == os.path.basename(__file__):
                continue

            ext = os.path.splitext(dir + "/" + filename)[1]
            os.rename(dir + "/" + filename, dir + "/" + basename + str(i) + ext)

            i += 1
        # Catch errors?
        print("Files renamed. Thank you, come again.")
        break

def dir_input():
    dir = input("Enter the target directory: ")
    if os.path.isdir(str(dir)) == False:
        print("Directory not found. Please try again.")
        dir_input()
    else:
        return str(dir)

if __name__ == "__main__":
    main()
