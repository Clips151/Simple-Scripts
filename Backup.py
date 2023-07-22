import os
import shutil

def backup_data(source_dir, backup_dir):
    try:
        # Check if the source directory exists
        if not os.path.exists(source_dir):
            print(f"Source directory '{source_dir}' does not exist.")
            return
        
        # Create the backup directory if it doesn't exist
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
            print(f"Backup directory '{backup_dir}' created.")
        
        # Get the list of files and subdirectories in the source directory
        items = os.listdir(source_dir)
        
        # Copy each item in the source directory to the backup directory
        for item in items:
            source_path = os.path.join(source_dir, item)
            backup_path = os.path.join(backup_dir, item)
            
            if os.path.isdir(source_path):
                # If the item is a directory, recursively copy its contents
                backup_data(source_path, backup_path)
            else:
                # If the item is a file, copy it to the backup directory
                shutil.copy2(source_path, backup_path)
                print(f"File '{item}' backed up.")
        
        print("Backup completed successfully.")
        
    except Exception as e:
        print(f"An error occurred during backup: {str(e)}")

if __name__ == "__main__":
    # Replace 'source_directory' with the path of the directory you want to back up
    source_directory = '/path/to/source_directory'
    
    # Replace 'backup_directory' with the path of the destination directory for the backup
    backup_directory = '/path/to/backup_directory'
    
    backup_data(source_directory, backup_directory)
