import shutil
import os

currdir = os.path.dirname(os.path.abspath(__file__))
lines = open(os.path.join(currdir, "paths.txt"))
all_lines = lines.readlines()
mdir = all_lines[1]
mdir = mdir.replace("\n", "")
mdir = mdir.replace("mdir:", "")
cdir = all_lines[2]
cdir = cdir.replace("\n", "")
cdir = cdir.replace("cdir:", "")

with open(os.path.join(mdir, cdir, "scripts/windows/copiedconfigpaths.txt")) as lines:
    for line in lines:
        path = line.replace("\n", "")
        shutil.copyfile(os.path.join(mdir, "civ13-git", path),
                        os.path.join(mdir, cdir, path))

with open(os.path.join(mdir, cdir, 'scripts/windows/copiedfolderpaths.txt')) as lines:
    for line in lines:
        path = line.replace("\n", "")
        shutil.rmtree(os.path.join(mdir, cdir, path))
        shutil.copytree(os.path.join(mdir, "civ13-git/", path),
                        os.path.join(mdir, cdir, path))
