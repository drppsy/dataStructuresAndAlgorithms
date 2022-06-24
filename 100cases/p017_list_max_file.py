import os


target_path = "/Users/admin/Downloads"

res = []

for roots, dirnames, files in os.walk(target_path):
    # print(dirnames)
    for file in files:
        if file.endswith(".mp4"):
            file_path_and_file_size = (f"{roots}/{file}",
                                       os.path.getsize(f"{roots}/{file}")/1000)
            res.append(file_path_and_file_size)


print(sorted(res, key=lambda x: x[1], reverse=True)[:10])
