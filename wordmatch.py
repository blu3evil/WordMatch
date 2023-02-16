import os
import platform
import sys

def search(folder = "../python", word="ogg", extension="py"):
    filelist = os.listdir(folder)
    os.chdir(os.path.join(os.getcwd(), folder))
    path = pathip(path = os.getcwd())
    for file in filelist:
        if os.path.isdir(os.path.join(os.getcwd(), file)):
            search(os.path.join(os.getcwd(), file), word, extension)
            os.chdir(os.path.join("../"))
        if file.endswith(extension):
            f = open(file,"r", encoding='utf-8')
            i = 0
            for line in f.readlines():
                i += 1
                line = line.strip().replace('\n','')
                if word in line:
                    print('\033[1;36m[+]\033[0m  ' + \
                          'Match \033[1;33m%s\033[0m at \033[1;34m%s\033[0m line %d: \033[1;32m%s\033[1;0m' \
                            % (word, path + file, i, line))

def pathip(root = sys.argv[1], path = __file__):
    root = root.replace('.', '').replace('/', '').replace('\\', '')
    return root + path.split(root, 1)[1] + '\\' if platform.system().lower() == 'windows' else '/' 
    

if __name__ == '__main__':    
    search(sys.argv[1], sys.argv[2], sys.argv[3])
    #search("./sounds/","ogg","py")

