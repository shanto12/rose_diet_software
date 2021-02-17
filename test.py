import os


for root, dirs, files in os.walk("Main"):
    path = root.split(os.sep)
    for file in files:
        file_name = file.split(".txt")[0]
        file_path = path + [file]
        print("-->".join(file_path[1:]))

text = "asdf=asdf"
k, v = text.split("=")
# tuple(text.split("="))
for k, v in (1, 2):
    print(k, v)