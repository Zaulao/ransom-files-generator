import argparse
from pathlib import Path
import random
import string
import randomfiletree
import threading

EXTENSIONS = [".3ds", ".7z", ".accdb", ".ai", ".asp", 
              ".aspx", ".avhd", ".avi", ".back", ".bak", 
              ".c", ".cfg", ".conf", ".cpp", ".cs", 
              ".ctl", ".dbf", ".disk", ".djvu", ".doc", 
              ".docx", ".dwg", ".eml", ".fdb", ".giff", 
              ".gz", ".h", ".hdd", ".jpg", ".jpeg", 
              ".kdbx", ".mail", ".mdb", ".mpg", ".mpeg", 
              ".msg", ".nrg", ".ora", ".ost", ".ova", 
              ".ovf", ".pdf", ".php", ".pmf", ".png", 
              ".ppt", ".pptx", ".pst", ".pvi", ".py", 
              ".pyc", ".rar", ".rtf", ".sln", ".sql", 
              ".tar", ".tiff", ".txt", ".vbox", ".vbs", 
              ".vcb", ".vdi", ".vfd", ".vmc", ".vmdk", 
              ".vmsd", ".vmx", ".vsdx", ".vsv", ".work", 
              ".xls", ".xlsx", ".xvd", ".zip"]

def fname():
    ext = EXTENSIONS[random.randint(0,len(EXTENSIONS)-1)]
    length = random.randint(5, 10)
    return "".join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(length)
    ) + ext

def process_paths(path):
    for path in path.iterdir():
        if path.is_dir():
            thread = threading.Thread(target=process_paths, args=(path,))
            thread.start()
        elif path.is_file():
            thread = threading.Thread(target=fill_file, args=(path,))
            thread.start()


def fill_file(path):
    with path.open('wb') as file:
        # Generate random content (up to 5MB of data)
        file_content = random.randbytes(random.randint(1,5000000))
        file.write(file_content)
        print(f'Filled: {str(path)}')

def main():
    parser = argparse.ArgumentParser(description='Generate random files for Infection Monkey Ransomware', formatter_class=argparse.RawDescriptionHelpFormatter,)
    parser.add_argument('-p', '--path', type=str, default='./ransom_files', help='path/to/basedir')
    parser.add_argument('-n', '--files', type=int, default=10, help='number of files per folder')
    parser.add_argument('-f', '--folders', type=int, default=2, help='number of folders')
    parser.add_argument('-d', '--depth', type=int, default=2, help='max depth of folders')
    parser.add_argument('-r', '--repeat', type=int, default=1, help='times to walk over created files and directories')
    args = parser.parse_args()
    
    randomfiletree.core.iterative_gaussian_tree(
        str(args.path),
        nfiles=args.files,
        nfolders=args.folders,
        repeat=4,
        maxdepth=args.depth,
        filename=fname
    )
    process_paths(Path(args.path))

if __name__ == '__main__':
    main()