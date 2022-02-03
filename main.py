import os


def soldier(dir_path, words_file, special_format):
    with open(words_file) as f:
        words = f.read().splitlines()
    os.chdir(dir_path)
    i = 0
    for file in os.listdir():
        if os.path.isfile(file) and (not file.startswith('.')):
            i += 1
            file2 = file.split(".")
            if file2[1] == special_format:
                os.rename(file, f"{i}.{file2[1]}")
            elif file2[0] not in words:
                os.rename(file, file.capitalize())


# soldier("./Test", 'harry.txt', 'jpg')
