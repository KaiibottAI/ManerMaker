#!/usr/bin/env python

from gimpfu import *
import os

def batch_resize_500x500(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            image = pdb.gimp_file_load(input_path, input_path)
            drawable = image.active_layer

            pdb.gimp_image_scale(image, 500, 500)
            pdb.file_png_save_defaults(image, drawable, output_path, output_path)
            pdb.gimp_image_delete(image)

register(
    "python_fu_batch_resize_500x500",
    "Resize all PNG images in a folder to 500x500",
    "Resize all PNG images in a folder to 500x500",
    "Your Name",
    "Your Name",
    "2025",
    "<Image>/Filters/Custom/Batch Resize to 500x500",
    "",  # No image required to run
    [
        (PF_DIRNAME, "input_folder", "Input folder", ""),
        (PF_DIRNAME, "output_folder", "Output folder", "")
    ],
    [],
    batch_resize_500x500
)

main()
