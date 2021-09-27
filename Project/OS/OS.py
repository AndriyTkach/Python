import os
import time
import argparse
import hashlib
import sys


def is_image(f):
    if f.endswith(".jpg"):
        return True
    if f.endswith(".png"):
        return True
    if f.endswith(".jpg"):
        return True
    if f.endswith(".tiff"):
        return True
    if f.endswith(".bmp"):
        return True
    if f.endswith(".gif"):
        return True
    if f.endswith(".ico"):
        return True
    return False

def show_images(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if is_image(file):
                path_file = os.path.join(root,file)
                if args.output == None:
                    print(path_file)
                else:
                    results.append(path_file)
        
def show_old_files(path):
    now = time.time()
    for filename in os.listdir(path):
        if os.path.getmtime(os.path.join(path, filename)) < now - 356*86400:
            if os.path.isfile(os.path.join(path, filename)):
                if args.output == None:
                    print(filename)
                else:
                    results.append(filename)

def chunk_reader(fobj, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = fobj.read(chunk_size)
        if not chunk:
            return
        yield chunk

def check_for_duplicates(paths, hash=hashlib.sha1):
    hashes = {}
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                hashobj = hash()
                for chunk in chunk_reader(open(full_path, 'rb')):
                    hashobj.update(chunk)
                file_id = (hashobj.digest(), os.path.getsize(full_path))
                duplicate = hashes.get(file_id, None)
                if duplicate:
                    if args.output == None:
                        print(f"Dublicates found: \"{full_path}\" и \"{duplicate}\"")
                    else:
                        results.append(f"Dublicates found: \"{full_path}\" и \"{duplicate}\"")
                else:
                    hashes[file_id] = full_path

def show_large(dir, target_size):
    for dirpath, dirs, files in os.walk(dir):
        for file in files: 
            path = os.path.join(dirpath, file)
            if os.stat(path).st_size > target_size:
                if args.output == None:
                    print(path)
                else:
                    results.append(path)

def get_bytes():
    if args.size == None:
        return -1
    lastS = str(args.size[-1])
    if lastS.isdigit():
        bytes = int(args.size)
    elif (lastS == 'B') or (lastS == 'b'):
        bytes = int(args.size[:-1]) 
    elif (lastS == 'K') or (lastS == 'k'):
        bytes = int(args.size[:-1]) * 1024
    elif (lastS == 'M') or (lastS == 'm'):
        bytes = int(args.size[:-1]) * 1048576
    elif (lastS == 'G') or (lastS == 'g'):
        bytes = int(args.size[:-1]) * 1073741824
    elif (lastS == 'T') or (lastS == 't'):
        bytes = int(args.size[:-1]) * 1099511627776
    else:
        return -1
    return bytes

def write_to_file(resuts):
    with open(args.output + '.txt', "a") as file:
        for result in results[:-1]:
            file.write(f"{result}\n")
        if len(results) > 1:
            file.write(results[-1])

def parse_command():
    help = '''-------------------------------------------------------
commands:
dublicates               - show dublicates of file
large -size SIZE_OF_FILE - show files larger than SIZE_OF_FILES
images                   - show images
old                      - show files older than 1 year

optional arguments:
-o, --output FILE_NAME   - save results to FILE_NAME.txt file
-h, --help               - show documentation

examples:
duplicates D:\\var\\files\\test_folder -o results
large -size 2G D:\\var\\files\\large_folder
images D:\\var\\files\\images 
old D:\\var\\files\\large_folder
-------------------------------------------------------'''

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("command")
    parser.add_argument("-size", "--size", type=str)
    parser.add_argument("path")
    parser.add_argument("-o", "--output", type=str)
    parser.add_argument('-h', '--help', action="store_true")
    
    try:
        args = parser.parse_args()
        if args.help:
            print(help)
        return args
    except:
        print(help)
    
    return None


args = parse_command()

if args != None:
    if os.path.isdir(args.path):
        path = args.path
        global results
        results = []
        if args.output != None:
            resf = (os.path.abspath(os.curdir) 
                    + '\\' + args.output + '.txt')
            if os.path.isfile(resf):
                os.remove(resf)

        if args.command == "images":
            show_images(path)
        elif args.command == "old":
            show_old_files(path)
        elif args.command == "dublicates":
            check_for_duplicates(sys.argv[1:])
        elif args.command == "large":
            bytes = get_bytes()
            if bytes == -1:
                print("File size not specified or format is incorrect")
            else:
                show_large(path, bytes)
        else:
            print("The command does not exist")

        if args.output != None:
            write_to_file(results)

    else:
        print (f"\nDirectory \"{args.path}\" not found")

