import os
import re
'''
    os.path.exists(path) - Returns true if the path is a file, directory, or a valid symlink.
    os.path.isfile(path) - Returns true if the path is a regular file or a symlink to a file.
    os.path.isdir(path) - Returns true if the path is a directory or a symlink to a directory.
'''
def CheckStringInFile(filename,searchstring):
    if os.path.exists(filename) and os.path.isfile(filename):
        print("{} exists".format(filename))
        with open(filename) as f:
            linenum = 1
            for eachline in f.readlines():
                if eachline.__contains__(searchstring):
                    print("String {} found in Line number {}".format(searchstring,linenum))
                linenum += 1
    else:
        print("{} Not Exists or It may not be a regular file".format(filename))

CheckStringInFile("testfile.txt","cool")