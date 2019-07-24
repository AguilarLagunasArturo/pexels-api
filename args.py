import sys
import os
args_boundary = (2,12)
required_args_boundary = (2,3)
usage = "Usage: " + sys.argv[0] + " [options] [query] [photos] [path]"
long_usage = usage + """
    Description:
        Download photos from https://www.pexels.com
    Arguments:
        Required:
            query:  A string with the topic of the search
            photos: The number of photos you wish to download
        Not required:
            path:   The directory in which the photos will be downloaded current path assumed if not given
        Options:
            -v:     Verbose mode will print information about each photo
            -d:     Photos will have a description in their filename
            -i:     Photos will have their pexels id in their filename
            -p:     Photos will have their photographer in their filename
            -o:     Photos will be organized by photographer path/query/photographer/filename with description-pexels-id as filename
            -c:     Reduce the size of the photo by compressing the original, it has the aspect ratio of the original photo
            -l:
            -m:
            -s:
        By default the photos will be downloaded with the original size in path/query/filename and they will be enumerated."""
args = sys.argv[1:]
if len(args) == 0 or (len(args) == 1 and args[0] == "--help"):
    print(long_usage)
    exit()
if len(args) < args_boundary[0] or len(args) > args_boundary[1]:
    print(usage)
    exit()

required_args = []
optional_args = []
query = None
total_photos = None
path = os.getcwd()
options = {
    "-v": False,
    "-i": False,
    "-d": False,
    "-p": False,
    "-o": False,
    "-c": False,
    "-l": False,
    "-m": False,
    "-s": False
}
sizes = ["-c", "-l", "-m", "-s"]

required_args = args
# Get required_args and optional_args
optional_args = [arg for arg in args if arg in options]
optional_args = list(dict.fromkeys(optional_args))
if len([size for size in sizes if size in optional_args]) > 1:
    print(usage)
    print("Too many sizes")
    exit()
required_args = [arg for arg in args if arg not in options]

if len(required_args) < required_args_boundary[0] or len(required_args) > required_args_boundary[1]:
    print(usage)
    exit()
# Get options
for option in optional_args:
    options[option] = True

query = required_args[0]
try:
    total_photos = int(required_args[1])
except:
    print("{}: Not a hole number".format(required_args[1]))
    print(usage)
    exit()
if total_photos < 1:
    print("{}: Minimum value 1".format(total_photos))
    print(usage)
    exit()
if len(required_args) == 3:
    if os.path.isdir(required_args[2]):
        path = required_args[2]
    else:
        print("{}: Not a directory".format(required_args[2]))
        print(usage)
        exit()

print("Options: ", options)
print("Query: ", query)
print("Total photos: ", total_photos)
print("Path:", path)
