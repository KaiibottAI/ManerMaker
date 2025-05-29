#!/usr/bin/env python
from gimpfu import *

def generate_numbered_tiles():
    width, height = 500, 500
    font = "Sans Bold"
    font_size = 64

    for i in range(66):
        label = "TILE{:02d}".format(i)

        # Create image and background
        image = pdb.gimp_image_new(width, height, RGB)
        bg_layer = pdb.gimp_layer_new(image, width, height, RGB_IMAGE, "White BG", 100, NORMAL_MODE)
        pdb.gimp_image_add_layer(image, bg_layer, 0)
        pdb.gimp_context_set_foreground((255, 255, 255))
        pdb.gimp_drawable_fill(bg_layer, FOREGROUND_FILL)

        # Add centered text
        pdb.gimp_context_set_foreground((0, 0, 0))
        text_layer = pdb.gimp_text_fontname(image, None, 0, 0, label, 10, True,
                                            font_size, PIXELS, font)

        text_width = pdb.gimp_drawable_width(text_layer)
        text_height = pdb.gimp_drawable_height(text_layer)
        pdb.gimp_layer_set_offsets(text_layer,
                                   (width - text_width) // 2,
                                   (height - text_height) // 2)

        # Flatten and save the image
        final = pdb.gimp_image_merge_visible_layers(image, CLIP_TO_IMAGE)
        filename = "D:/house-on-the-hill/house-tiles/{}.png".format(label)  # Update path for Windows or desired folder
        pdb.file_png_save(image, final, filename, filename, 0, 9, 0, 0, 0, 0, 0)

        # Cleanup
        pdb.gimp_image_delete(image)

register(
    "python_fu_generate_numbered_tiles",
    "Generate TILE00 to TILE65 images",
    "Creates 500x500 white tiles labeled TILE00 to TILE65 and saves them as PNGs",
    "You",
    "You",
    "2025",
    "Generate Numbered Tiles...",
    "",  # No image required
    [],
    [],
    generate_numbered_tiles,
    menu="<Image>/Filters/Custom"
)

main()
