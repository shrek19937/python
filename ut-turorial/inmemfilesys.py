import sys

def parse_path(path):
    parsed = path.rsplit("/", 1)
    return parsed[0], parsed[1]

class inmemfilesys:
    def __init__(self):
        self.internal = dict({"/": dict()})  #parent_dir, dict(tuple(name, content))

    def mkdir(self, dirname):
        if dirname in self.internal:
            return

        for i in range(1, len(dirname)):
            if dirname[i] == '/':
                if dirname[:i] not in self.internal:
                    self.internal[dirname[:i]] = dict()

        self.internal[dirname] = dict()

    def write(self, path, content):
        dir, file = parse_path(path)  #appending a trailing "/"
        self.mkdir(dir)
        self.internal[dir][file] = content

    def read(self, path):
        dir, file = parse_path(path)
        
        if file not in self.internal[dir]:
            raise Exception(f"error: {path} not found")
        
        return self.internal[dir][file]

#test
sys.tracebacklimit = 0
fs = inmemfilesys()
fs.write("/etc/crond/f1", "this is the content of crond")
fs.write("/etc/crond/f2", "this is a 2nd file")
print(fs.read("/etc/crond/f2"))
print(fs.read("/etc/typo"))