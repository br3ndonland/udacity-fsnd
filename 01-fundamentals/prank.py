import os


def rename_files():
    """Remove numbers from a list of image files."""
    # Save current working directory
    saved_path = os.getcwd()
    print('Current working directory is ' + saved_path)

    # Get file names from a folder
    os.chdir('img/prank')
    file_list = os.listdir()
    print(file_list)

    # For each file, rename filename
    for file_name in file_list:
        # construct translation table for the translate function
        t_table = str.maketrans('0123456789', '          ', '0123456789')
        # rename file with new name
        os.rename(file_name, file_name.translate(t_table))

    # Display list of renamed files
    renamed_files = os.listdir()
    print(renamed_files)

    # Return to previous working directory
    os.chdir(saved_path)
    print('Directory changed back to ' + os.getcwd())


rename_files()
