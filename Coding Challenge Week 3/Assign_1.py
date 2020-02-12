
import os

#Command to set an an empty directory where all folders will be created.

#G:\ is drive on my computer. May be different on other PC>

Main_Director = "G:\ Empty_Directory"
os.mkdir(Main_Director)

#Adding main folders to the empty directory using os.path.join
os.mkdir(os.path.join(Main_Director, "draft_code"))
os.mkdir(os.path.join(Main_Director, "includes"))
os.mkdir(os.path.join(Main_Director, "layouts"))
os.mkdir(os.path.join(Main_Director, "site"))

#Adding subfolders to "draft code" main folder
os.mkdir(os.path.join(Main_Director, "draft_code", "pending"))
os.mkdir(os.path.join(Main_Director, "draft_code", "complete"))

#Adding subfolders to "layouts" main folder
os.mkdir(os.path.join(Main_Director, "layouts", "default"))
os.mkdir(os.path.join(Main_Director, "layouts", "post"))

#Adds posted as a sub-subfolder to post
os.mkdir(os.path.join(Main_Director, "layouts", "post", "posted"))

#Code to delete the entire directory and all folders and sub-folders using "shutil module" to remove all at once
import shutil
shutil.rmtree(Main_Director)
