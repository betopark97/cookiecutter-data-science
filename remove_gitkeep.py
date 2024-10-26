import os


def add_gitkeep_to_empty_dirs(root_dir): 
    # Walk through all directories and subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Check if the directory is empty
        if not dirnames and not filenames:  # No subdirectories and no files
            gitkeep_path = os.path.join(dirpath, '.gitkeep')
            # Create a .gitkeep file
            with open(gitkeep_path, 'w') as f:
                f.write("")  # Create an empty file
            print(f"Added .gitkeep to empty directory: {dirpath}")


def remove_gitkeep_files(root_dir):
    # Walk through all directories and subdirectories
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == '.gitkeep':
                gitkeep_path = os.path.join(dirpath, filename)
                os.remove(gitkeep_path)
                print(f"Removed: {gitkeep_path}")


if __name__ == "__main__":
    # Path to this root directory
    root_dir_path = '../cookiecutter-data-science'
    # add_gitkeep_to_empty_dirs(root_dir_path)
    remove_gitkeep_files(root_dir_path)