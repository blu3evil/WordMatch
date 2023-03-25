import os
import platform
import sys
import getopt
#都给我用绝对地址
def search(folder="/", word="porn", extension="*", flag_quiet=True,):
    try:
        os.chdir(folder)
    except PermissionError:
        if not flag_quiet:
            print('\033[1;31m[-]\033[0m  ' + "Permission denied when entering files from  " + '\033[1;34m' + folder +'\033[0m')
        return
    try:
        filelist = os.listdir(folder)
        if len(filelist) == 0:
            os.chdir(os.getcwd() + '/..')
    except PermissionError:
        if not flag_quiet:
            print('\033[1;31m[-]\033[0m  ' + "Permission denied when listing files from  " + '\033[1;34m' + folder +'\033[0m')
        os.chdir(os.getcwd() + '/..')
        return
    for file in filelist:
        if os.path.isdir(os.path.join(folder, file)):
            search(os.path.abspath(file), word, extension)
            if filelist.index(file) == len(filelist) - 1:
                os.chdir(os.getcwd() + '/..')
        elif file.endswith(extension) or extension =='*':
            try:
                f = open(os.path.abspath(file),"r", encoding='utf-8')
                i = 0
                for line in f.readlines():
                    i += 1
                    line = line.strip().replace('\n','')
                    if word in line:
                        print('\033[1;36m[+]\033[0m  ' + \
                            'Match \033[1;33m%s\033[0m at \033[1;34m%s\033[0m line %d: \033[1;32m' \
                            % (word, os.path.abspath(file), i) + printAll(line.split(word), word) + '\033[0m')
            except (FileNotFoundError, OSError, UnicodeDecodeError, PermissionError):
                if not flag_quiet:
                    print('\033[1;31m[-]\033[0m  ' + "Something bad happened when reading file " + '\033[1;34m' + os.path.abspath(file) +'\033[0m')
                continue
            finally:
                if filelist.index(file) == len(filelist) - 1:
                    os.chdir(os.getcwd() + '/..')
                
    
def printAll(words, key):
    ret = ''
    for word in words:
        if not word == words[-1]:
            ret += '\033[1;32m' + word + '\033[1;0m\033[1;35m'
            ret += key + '\033[1;0m'
        else:
            ret += '\033[1;32m' + word + '\033[1;0m\033[1;35m'
    return ret

def print_help():
    print("test")

if __name__ == '__main__': 
    path, word, extension = ["","",""]
    flag_help = False
    flag_quiet = True
    opts, args = getopt.getopt(sys.argv[1:], "hqp:w:o:e:")
    for key, val in opts:
        match key:
            case '-h':
                flag_help = True
            case '-q':
                flag_quiet = True
            case '-p':
                path = val
            case '-w':
                word = val
            case '-o':
                output = val            
            case '-e':
                extension = val
    search(path, word, extension, flag_quiet)
    #search("C:\\Users\\Blu3", "blu3", "*")
