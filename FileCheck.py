
def IsFileExists(filepath):
    try:
        with open(filepath) as f:
            return True
    except IOError:
        return False

def CheckStringInFile(filename,searchstring):
    if IsFileExists(filename):
        print("{} exists".format(filename))
        with open(filename) as f:
            linenum = 1
            for eachline in f.readlines():
                if eachline.__contains__(searchstring):
                    print("String {} found in Line number {}".format(searchstring,linenum))
                linenum += 1
    else:
        print("{} Not Exists".format(filename))

CheckStringInFile("testfile.txt","comment")