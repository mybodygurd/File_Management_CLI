import os
import sys
from typing import Optional


def list_files(dir: str=None) ->Optional[list]:
    if not dir:
        d_path = os.getcwd()
        
    elif os.path.exists(dir):
        d_path = dir
    else:
        return None
        
    files_name = os.listdir(d_path)
        # file_path = os.path.join(d_path, item)

    return files_name

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
                files_name = list_files(dir)
                
                if not files_name:
                    print(f"Directory not found: {dir}")
                    continue
                for file_name in files_name:
                    print(file_name)
            elif choice == '2':
                sys.exit("Exiting...")
            else:
                print("Invalid choice!")
        except KeyboardInterrupt:
            sys.exit("Exiting...")
            

if __name__ == "__main__":
    main()