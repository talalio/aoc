from pyfs import Fs, Dir, File

fs = Fs()


def parse_output(output):
    for (idx, line) in enumerate(output):
        if line.startswith('$'):
            if "cd" in line:
                path = line.split()[-1]
                if not fs.path_exists(path):
                    fs.add_d(Dir(path, fs.current, {}, {}))
                fs.cd(path)

        else:
            rtype, name = line.split()

            if rtype == 'dir':
                if not fs.path_exists(name):
                    fs.add_d(Dir(name, fs.current, {}, {}))
                continue

            if not fs.file_exists(name):
                fs.add_f(File(name, rtype))


with open('input.txt', 'r') as f:
    term_out = f.read().splitlines()
    parse_output(term_out)
    # print(fs.get_dir(100_000))
    print(fs.free_space())
