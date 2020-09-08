from datetime import datetime
import os, time

class Tool:

    def __init__(self):
        # get current time & directory
        self.now = datetime.now()
        self.initial_dir = os.getcwd()
    
    def get_input(self):
        """
        Effects: Prompts user to enter a path and stores the path as an 
                 instance variable.
        """
        path = input("Enter path: ")
        print()

        # check whether the path is an existing directory
        isdir = os.path.isdir(path)

        while not isdir:
            path = input("Invalid path. Please try again: ")
            isdir = os.path.isdir(path)

            if isdir:
                break

        self.path = path

    def change_directory(self):
        """
        Effects: Changes current path to specified path.
        """
        # ask user to input a path
        self.get_input()

        # change directory
        os.chdir(self.path)
        print("Successfully changed directory.")

        print("Current directory: ", self.path)

    def should_break(self, src):
        """
        Effects: Returns True if src file is created within 30 minutes from self.now,
                 otherwise returns False.
        """
        # convert string to datetime object
        created = datetime.strptime(time.ctime(os.path.getctime(src)), "%a %b %d %H:%M:%S %Y")

        # calculate difference in minutes
        minutes_diff = (self.now - created).total_seconds() / 60.0

        # only files created within 30mins from now should be changed
        if minutes_diff > 30:
            return True
        else:
            return False

    def rename_files(self):
        """
        Effects: Loops through files in self.path to rename each image file
                 that has an extension included in ext_lst.
        """
        count = 1

        # sort the list of files in desc order by creation time
        files = os.listdir(self.path)
        files.sort(key = os.path.getctime, reverse = True)

        for file in files:    
            src = self.path + '/' + file
            dst = self.path + '/' + 'image' + str(count)

            # check conditions to exit loop
            if self.should_break(src):
                break

            # get current file extension
            ext = os.path.splitext(file)[1]
            # extensions to check
            ext_lst = [".png", ".jpg", ".jpeg", ".tiff", ".tif", ".bmp"]

            if ext in ext_lst:
                while True:
                    try:
                        # rename source path to destination path
                        os.rename(src, dst + ext)
                        break

                    except FileExistsError:
                        dst = dst + '-duplicate'

                # increment count
                count += 1

        num_image = count - 1
        print(num_image, "filenames changed.")

        return num_image
    
    def create_directory(self, num_image):
        """
        Effects: Checks if number of images is more than 9. If it is more than 9,
                 a new directory will be created. All image files created
                 within 30 minutes from self.now will be moved to the new directory.
        """
        # if at least 10 image files
        if num_image >= 10:
            count = 0

            # create new directory
            new_dir = self.path + '/Images'
            os.mkdir(new_dir)

            # move all image files to new directory    
            for file in os.listdir(self.path):
                src = self.path + '/' + file
                dst = new_dir + '/' + file

                # check conditions to exit loop
                if self.should_break(src):
                    break

                if file.startswith("image"):
                    os.rename(src, dst)
                    # increment count
                    count += 1

            print(count, "files moved to new directory.")

        else:
            print("No directory created.")

        # change back to previous directory
        os.chdir(self.initial_dir)
        print("Returned to previous directory.")

if __name__ == '__main__':
    tool = Tool()
    tool.change_directory()
    num_image = tool.rename_files()
    tool.create_directory(num_image)