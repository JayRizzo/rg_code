#!/usr/bin/env python3
# =============================================================================
"""Module To Locate X,Y of images in a folder for the game 'Realm Grinder'."""
# =============================================================================
# Created By: Jeromie Kirchoff
# Created On: 2018-05-13
# https://stackoverflow.com/a/5137509/1896134
# https://stackoverflow.com/a/5337759/1896134
# https://stackoverflow.com/a/1120736/1896134
# =============================================================================
from os import listdir
from os.path import dirname
from os.path import realpath

from sys import path

from pyautogui import locateCenterOnScreen

# =============================================================================
# Declarations
# =============================================================================
script_dir = path[0]
dir_path = dirname(realpath(__file__))


def find_image(item):
    """Module To Locate X,Y of images in a folder."""
    xy_none_loc = locateCenterOnScreen(item)
    print("X,Y Location: {} --- Path: {}".format(xy_none_loc, item))
    # print(str(xy_none_loc))
    return xy_none_loc


def check_all_images():
    """Locate X,Y for all images in current project image folder."""
    for filename in listdir(dir_path + "/image"):
        if filename.endswith(".png"):
            # print(os.path.join(dir_path + '/image/' + filename))
            # print('Filename: ' + filename)
            xy = find_image(dir_path + '/image/' + filename)
    return xy


if __name__ == '__main__':
    check_all_images()
