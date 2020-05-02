import os

path = input("Enter the path: ")
print()

# check whether the path is an existing directoyr
isdir = os.path.isdir(path)

while not isdir:
    path = input("Invalid path. Please try again: ")

# change directory
os.chdir(path)
print("Successfully changed directory.")

location = os.getcwd()
print("Current directory: ", location)

count = 1

for file in os.listdir(location):
    src = location + '/' + file
    dst = location + '/' + 'image' + str(count)

    if file.endswith(".png") or file.endswith(".jpg"):
        if (file.endswith(".png")):
            # rename source path to destination path
            os.rename(src, dst + '.png')
        else:
            # rename source path to destination path
            os.rename(src, dst + '.jpg')

        # increment count
        count += 1

print(count - 1, " filenames changed.")