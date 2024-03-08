import os
import argparse
import glob

import sys

def do_system(arg):
    print(f"==== running: {arg}")
    err = os.system(arg)
    if err:
        print("FATAL: command failed")
        sys.exit(err)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("path", default="", help = "input path to the output folder")
    args = parser.parse_args()
    test_png_path = os.path.join(args.path, "test/ours_None/")
    for png in pngs:
        do_system(f"ffmpeg -framerate 15 -i %05d.png test_render.gif")
        do_system(f"ffmpeg -i {video} -start_number 0 -r 10 {test_png_path}/{cam_name}_%04d.png")