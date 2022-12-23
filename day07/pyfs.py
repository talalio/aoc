class Dir():
    def __init__(self, name, parent, dirs, files):
        self.name = name
        self.parent = parent
        self.dirs = dirs
        self.files = files
        self.update_size()

    def add_file(self, file):
        self.files.update(file)
        self.update_size()

    def add_dirs(self, dirc):
        self.dirs.update(dirc)
        self.update_size()

    def update_size(self):
        filesize = [int(x.size) for x in self.files.values()]
        dirsize = [int(dirc.size) for dirc in self.dirs.values()]

        self.size = sum(filesize + dirsize)

        if self.parent:
            self.parent.update_size()

    def get_dirs(self, size_limit):
        result = []
        for dirc in self.dirs.values():
            if dirc.size <= size_limit:
                result.append(dirc.size)

            result.extend(dirc.get_dirs(size_limit))

        return result

    def free_space(self, used_space, max_space, min_space):
        to_delete = []

        for dirc in self.dirs.values():
            if max_space - (used_space - dirc.size) >= min_space:
                to_delete.append(dirc.size)

            to_delete.extend(dirc.free_space(used_space, max_space, min_space))

        return to_delete


class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Fs():
    def __init__(self):
        self.MAX_STORAGE_SIZE = 70_000_000
        self.root = Dir('/', None, {}, {})
        self.current = self.root

    def cd(self, path):
        if path == '..':
            self.current = self.current.parent
        elif path == '/':
            self.current = self.root
        else:
            self.current = self.current.dirs[path]

    def add_d(self, dirc):
        self.current.add_dirs({dirc.name: dirc})

    def add_f(self, file):
        self.current.add_file({file.name: file})

    def path_exists(self, path):
        return True if path == '/' else path in self.current.dirs

    def file_exists(self, file_name):
        return file_name in self.current.files

    def get_dir(self, size_limit):
        return sum(self.root.get_dirs(size_limit))

    def free_space(self):
        return min(self.root.free_space(
            self.root.size, self.MAX_STORAGE_SIZE, 30_000_000))
