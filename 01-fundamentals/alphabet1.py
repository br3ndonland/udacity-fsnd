import os
import string


def rename_files():
    """Remove lowercase letters from a list of image files."""
    # Save current working directory
    saved_path = os.getcwd()
    print('Current working directory is ' + saved_path)

    # Get file names from a folder
    os.chdir('img/alphabet1')
    alphabet1_list = os.listdir()
    print(alphabet1_list)

    # For each file, rename filename
    for file_name in alphabet1_list:
        # construct translation table for the translate function
        t_table = str.maketrans(string.ascii_lowercase[:],
                                '                          ',
                                string.ascii_lowercase[:])
        # rename file with new name
        os.rename(file_name, file_name.translate(t_table))

    # Add back extension after deleting letters
    alphabet1_list_new = os.listdir()
    print(alphabet1_list_new)
    for file_name in alphabet1_list_new:
        os.rename(file_name, file_name + 'jpg')

    # Display list of renamed files
    renamed_files = os.listdir()
    print(renamed_files)

    # Return to previous working directory
    os.chdir(saved_path)
    print('Directory changed back to ' + os.getcwd())


rename_files()
