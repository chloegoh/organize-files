from datetime import datetime, timedelta
import os, time

# get current time
now = datetime.now()

initial_dir = os.getcwd()

path = input("Enter the path: ")
print()

# check whether the path is an existing directory
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

    # convert string to datetime object
    created = datetime.strptime(time.ctime(os.path.getctime(src)), "%a %b %d %H:%M:%S %Y")

    # calculate difference in minutes
    minutes_diff = (now - created).total_seconds() / 60.0

    # only files created within 30mins 
    # from now should be changed
    if now - created > timedelta(minutes=30):
        break

    # get current file extension
    ext = os.path.splitext(file)[1]
    # extensions to check
    ext_lst = [".png", ".jpg", ".jpeg", ".tiff", ".tif", ".bmp"]

    if ext in ext_lst:  
        # rename source path to destination path
        os.rename(src, dst + ext)

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
    print("No directory created.")

# change back to previous directory
os.chdir(initial_dir)
print("Returned to previous directory.")