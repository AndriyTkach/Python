import os
import time
import argparse
import hashlib
import sys
import mimetypes



def is_image(f):
    try: 
        ext = mimetypes.MimeTypes().guess_type(f)[0]
        return "image" in ext
    except TypeError:
        return False


def output(s:str):
    if args.output is None:
        print(s)
    else:
        results.append(s)


def show_images(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if is_image(file):
                path_file = os.path.join(root, file)
                output(path_file)


def show_old_files(path):
    now = time.time()
    for filename in os.listdir(path):
        if os.path.getmtime(os.path.join(path, filename)) < now - 356 * 86400:
            if os.path.isfile(os.path.join(path, filename)):
                output(filename)


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
                    output(f"Duplicates found: \"{full_path}\" and \"{duplicate}\"")
                else:
                    hashes[file_id] = full_path


def show_large(dir, target_size):
    for dirpath, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(dirpath, file)
            if os.stat(path).st_size > target_size:
                output(path)


def get_bytes(b):
    lastS = str(b[-1])
    if lastS.isdigit():
        bytes = int(b)
    elif (lastS == 'B') or (lastS == 'b'):
        bytes = int(b[:-1])
    elif (lastS == 'K') or (lastS == 'k'):
        bytes = int(b[:-1]) * 1024
    elif (lastS == 'M') or (lastS == 'm'):
        bytes = int(b[:-1]) * 1048576
    elif (lastS == 'G') or (lastS == 'g'):
        bytes = int(b[:-1]) * 1073741824
    elif (lastS == 'T') or (lastS == 't'):
        bytes = int(b[:-1]) * 1099511627776
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
    help = "------------------------------------------------------- \
            \n commands: \
            \n duplicates               - show dublicates of file \
            \n large -size SIZE_OF_FILE - show files larger than SIZE_OF_FILES \
            \n images                   - show images \
            \n old                      - show files older than 1 year \
            \n\n optional arguments: \
            \n -o, --output FILE_NAME   - save results to FILE_NAME.txt file \
            \n -h, --help               - show documentation \
            \n\n examples: \
            \n duplicates D:\\var\\files\\test_folder -o results \
            \n large -size 2G D:\\var\\files\\large_folder \
            \n images D:\\var\\files\\images \
            \n old D:\\var\\files\\large_folder \
            \n-------------------------------------------------------"

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

def main():
    global args
    args = parse_command()

    if args is not None:
        if os.path.isdir(args.path):
            path = args.path
            global results
            results = []
            if args.output is not None:
                resf = (os.path.abspath(os.curdir)
                        + '\\' + args.output + '.txt')
                if os.path.isfile(resf):
                    os.remove(resf)

            if args.command == "images":
                show_images(path)
            elif args.command == "old":
                show_old_files(path)
            elif args.command == "duplicates":
                check_for_duplicates([args.command, path])
            elif args.command == "large":
                if args.size is None:
                    print("File size not specified or format is incorrect")
                bytes = get_bytes(args.size)
                if bytes == -1:
                    print("File size not specified or format is incorrect")
                else:
                    show_large(path, bytes)
            else:
                print("The command does not exist")

            if args.output is not None:
                write_to_file(results)

        else:
            print(f"\nDirectory \"{args.path}\" not found")


main()
