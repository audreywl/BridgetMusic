"""This script reads the filenames on a music USB and removes the artist names."""
import os

def find_files(usb_dir):
    files = os.walk(usb_dir)
    print files

find_files()
