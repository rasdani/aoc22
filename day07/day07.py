# INPUT = "test_input.txt"
INPUT = "input.txt"

with open(INPUT, "r") as f:
    data = f.read().splitlines()

class FileSystem():
    def __init__(self):
        self.root = Directory(name="/", parent=None)
        self.current_dir = self.root

    # def __str__(self):
        # ret = ""
        # for i in self.root:
            # ret += f"{i.name}\n"
        # return ret

    def get_dir(self, _dir):
        for d in self.current_dir.content:
            if d.name==_dir:
                return d

    def cd(self, _dir):
        if _dir=="/":
            self.current_dir = self.root
        elif _dir=="..":
            self.current_dir = self.current_dir.parent
        elif _dir in [d.name for d in self.current_dir.content]:
            self.current_dir = self.get_dir(_dir)
        else:
            raise NameError("No such dir.")

    def parse(self, inp):
        for line in inp:
            line = line.rstrip()
            chunks = line.split(" ")
            if chunks[0]+chunks[1] == "$cd":
                    self.cd(chunks[2])
            elif chunks[0]+chunks[1] == "$ls":
                pass
            elif chunks[0] == "dir":
                _dir = Directory(parent=self.current_dir)
                _dir.name = chunks[1]
                self.current_dir.content.append(_dir)
            else:
                file_size, file_name = chunks[0], chunks[1]
                file = File(file_name, int(file_size))
                self.current_dir.content.append(file)

    def traverse(self, _dir):
        for x in _dir.content:
            if isinstance(x, Directory):
                self.traverse(x)
                _dir.size += x.size
            else:
                assert isinstance(x, File)
                _dir.size += x.size

    def print_sizes(self, _dir, level=0, s=0):
        for x in _dir.content:
            if isinstance(x, Directory):
                if x.size <= 100000:
                    # print(level * "\t", x.name, x.size)
                    s += x.size
                s = self.print_sizes(x, level=level+1, s=s)
        
        return s 

    # broke it accidentally, whoopsie
    # commit first working version!!!
    def del_candidate(self, _dir, candidate_size, candidate):
        # breakpoint()
        # if _dir == candidate:
            # return _dir
        for x in _dir.content:
            if isinstance(x, Directory):
                # if candidate.name=="dqbnbl":
                    # breakpoint()
                if candidate.size > _dir.size >= candidate_size:
                    print(x.name, x.size)
                    candidate = self.del_candidate(x, candidate_size, candidate=x)
                    # candidate = self.del_candidate(x, candidate_size, candidate=x)
                else:
                    return candidate
                    # return candidate

                # self.del_candidate(x, candidate_size, candidate)
        
        # breakpoint()
        return candidate

                    

class File():
    def __init__(self, name="", size=0):
        self.size = size
        self.name = name

class Directory():
    def __init__(self, parent, name="default_dir"):
        # watch out! inheritance causes:
        # isinstance(x, File) and isinstance(x, Directory) == True
        # super().__init__()
        self.size = 0
        self.name = name
        self.parent = parent
        self.content = []

    def ls(self):
        for x in self.content:
            print(x.name, 2*"\t",  x.size)


fs = FileSystem()
fs.parse(data)
fs.traverse(_dir=fs.root)
# s = fs.print_sizes(_dir=fs.root)
# print("Sum of small dir sizes: ", s)
free_space = 70000000 - fs.root.size
candidate_size = 30000000 - free_space
candidate = fs.del_candidate(fs.root, candidate_size, fs.root)
print("To delete: ", candidate.name, candidate.size)
