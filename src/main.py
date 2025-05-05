import os
import sys
from typing import Optional


def list_items(dir: str) -> Optional[list[tuple[str, str]]]:
    items = []
            
    if os.path.exists(dir):

        try:
            # if os.path.isdir(path):
                # ...
            for item in os.listdir(dir):
                item_path = os.path.join(dir, item)
                
                if os.path.isfile(item_path):
                    items.append((item, 'file'))
                else:
                    items.append((item, 'dir'))
            return items
        except PermissionError:
            raise
        except NotADirectoryError:
            raise
    return None
                         
def main():
    print("File Management CLI")
    while True:
        try:
            print('=' * 100)
            print("1. List Files")
            print("2. Exit")
            choice = input("Enter choice (1-2): ").strip()
            
            if choice == '1':
                dir = input("Enter directory (leave blank for current): ").strip()
                if not dir:
                    dir = os.getcwd()
                files_name = list_items(dir)  
                
                if files_name is None:
                    print(f"Directory not found: {dir}")
                    continue
                
                if len(files_name) == 0:
                    print("(no output)")
                    continue
                
                for file_name, type in files_name:
                    print(file_name, f"({type})")
            elif choice == '2':
                sys.exit("Exiting...")
            else:
                print("Invalid choice!")
        except KeyboardInterrupt:
            sys.exit("Exiting...")
        except PermissionError:
            print(f"not allowed to access directory: {dir}")
        except NotADirectoryError:
            print(f"invalid directory path: {dir}")
            

if __name__ == "__main__":
    main()