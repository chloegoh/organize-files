import os

initial_dir = os.getcwd()

path = input("Enter the path: ")
print()

# check whether the path is an existing directoyr
isdir = os.path.isdir(path)

while not isdir:
    path = input("Invalid path. Please try again: ")

# change directory
os.chdir(path)
print("Successfully changed directory.")

print("Current directory: ", path)

count = 1

for file in os.listdir(path):
    src = path + '/' + file
    dst = path + '/' + 'image' + str(count)

    if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
        if file.endswith(".png"):
            # rename source path to destination path
            os.rename(src, dst + '.png')
        elif file.endswith(".jpg"):
            # rename source path to destination path
            os.rename(src, dst + '.jpg')
        else:
            # rename source path to destination path
            os.rename(src, dst + '.jpeg')

        # increment count
        count += 1

print(count - 1, "filenames changed.")

# if more than 10 image files
if count > 10:
    # reset count
    count = 0

    # create new directory
    new_dir = path + '/Images'
    os.mkdir(new_dir)

    # move all image files to new directory    
    for file in os.listdir(path):
        src = path + '/' + file
        dst = new_dir + '/' + file

        if file.startswith("image"):
            os.rename(src, dst)
            # increment count
            count += 1

    print(count, "files moved to new directory.")

else:
    print("No new directory created.")

# change back to previous directory
os.chdir(initial_dir)
print("Returned to previous directory.")