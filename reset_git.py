import os
import shutil

def reset_git(git_dir_path='.git'):
    """
    Deletes the specified .git directory if it exists and reinitializes it.
    
    Parameters:
        git_dir_path (str): Path to the .git directory. Default is '.git' in the current directory.
    
    Returns:
        None
    """
    try:
        # Step 1: Check if the .git directory exists and delete it
        if os.path.exists(git_dir_path):
            if os.path.isdir(git_dir_path):  # Ensure it's a directory, not a file
                shutil.rmtree(git_dir_path)  # Remove the directory and its contents
                print(f"Deleted {git_dir_path} directory.")
            else:
                print(f"{git_dir_path} exists but is not a directory. Skipping deletion.")
                return
        else:
            print(f"{git_dir_path} does not exist. Proceeding to recreate it.")

        # Step 2: Reinitialize the .git directory as an empty Git repository
        os.system('git init')  # Use Git to reinitialize the repository
        print(f"Reinitialized Git repository in {os.getcwd()}")

    except Exception as e:
        print(f"An error occurred while resetting {git_dir_path}: {e}")

if __name__ == "__main__":
    reset_git()