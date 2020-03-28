import os
import sys

class Decompress_And_Combine:

    """
    Function to walk through the folder with all BZ2 Files and move them to a central "unzipped" folder.
    """
    def copy_bz2_to_central_folder(self, path_for_bz2):
        for dirpath, dirs, files in os.walk(path_for_bz2):
            for filename in files:
                fname = os.path.join(dirpath,filename)
            if fname.endswith('.bz2'):
                new_name = fname[20:].replace("/", "_")
                os.system("sudo mv " + fname + " " + "/Users/willshin/Development/GreatExpectations_Notes/data/" + new_name)

if __name__ == '__main__':
    Decompress_And_Combine().copy_bz2_to_central_folder(path_for_bz2='/Users/willshin/Development/GreatExpectations_Notes/data/2018')
