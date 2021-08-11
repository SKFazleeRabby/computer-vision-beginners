# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 19:29:59 2021

@author: SK. Fazlee Rabby
"""

import os
import shutil
import sys
import subprocess


#Update the variable with your virtual environment name
VIRTUAL_ENV = "tensorflow-gpu"


project_dir = os.path.dirname(__file__)
drive_root = f"{os.path.splitdrive(os.path.dirname(__file__))[0]}\\"
darknet_dir = os.path.join(drive_root, 'darknet')


os.makedirs(darknet_dir, exist_ok=True)
os.chdir(darknet_dir)
git_cmd = "git clone https://github.com/AlexeyAB/darknet.git ."

if not len(os.listdir(darknet_dir))>0:
    print(git_cmd)
    subprocess.run("git clone https://github.com/AlexeyAB/darknet.git .", 
                   stderr=sys.stderr, stdout=sys.stdout) 

try:
    import darknet
except:
    install_cmd = ["powershell.exe", ".//build.ps1", "-UseVCPKG",
                    "-EnableOPENCV", "-EnableCUDA", "-EnableCUDNN"]
    if VIRTUAL_ENV:
        install_cmd.insert(1, f"conda activate {VIRTUAL_ENV};")
    
    p = subprocess.Popen(install_cmd, stderr=sys.stderr, stdin=subprocess.PIPE,
                          stdout=sys.stdout, shell=True)
    p.communicate()
    print("FINISHED")

os.chdir(drive_root)

if not os.path.exists(os.path.join(project_dir, 'darknet')):
    print("Please Wait Till We Move the Darknet into the Project Directory. This action might take some times...")
    shutil.move(darknet_dir, os.path.join(project_dir, 'darknet'))
    if os.path.exists(darknet_dir):
        shutil.rmtree(darknet_dir)
    print("Darknet is successfully installed.")
else:
    if os.path.exists(darknet_dir):
        print("Delete the Darknet Folder in the explorer")

    print("Darknet is Already Installed")