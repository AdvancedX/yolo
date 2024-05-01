import os

path = "E:\Python\Here_is_a_Loopy\data\labels"
files = os.listdir(path)
files.sort()
for i, files in enumerate(files):
    os.rename(
        os.path.join(path, files), os.path.join(path, str(i + 1).zfill(3) + ".txt")
    )
    print("done")
