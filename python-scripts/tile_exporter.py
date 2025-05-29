#!/usr/bin/env python

from gimpfu import *
import os


def slice_and_export(image, drawable, tile_size, output_folder):
    pdb.gimp_image_undo_group_start(image)

    img_width = image.width
    img_height = image.height

    x_tiles = img_width // tile_size
    y_tiles = img_height // tile_size

    for y in range(y_tiles):
        for x in range(x_tiles):
            left = x * tile_size
            top = y * tile_size

            # Create a new image with same mode and one layer
            tile_img = pdb.gimp_image_new(tile_size, tile_size, RGB)
            tile_layer = pdb.gimp_layer_new(
                tile_img, tile_size, tile_size, RGB_IMAGE, "Tile", 100, NORMAL_MODE
            )
            pdb.gimp_image_add_layer(tile_img, tile_layer, 0)

            # Copy from original and paste
            pdb.gimp_edit_copy(drawable)
            floating_sel = pdb.gimp_edit_paste(tile_layer, False)
            pdb.gimp_layer_set_offsets(floating_sel, -left, -top)
            pdb.gimp_floating_sel_anchor(floating_sel)

            # File name and export
            filename = os.path.join(output_folder, "tile_{}_{}.png".format(x, y))
            pdb.file_png_save(
                tile_img, tile_layer, filename, filename, 0, 9, 0, 0, 0, 0, 0
            )

            # Clean up
            pdb.gimp_image_delete(tile_img)

    pdb.gimp_image_undo_group_end(image)
    pdb.gimp_displays_flush()


register(
    "python_fu_slice_and_export",
    "Slice and export image tiles",
    "Cuts an image into 512x512 tiles and exports them as .png files",
    "You",
    "You",
    "2025",
    "<Image>/Filters/Tiling/Slice and Export Tiles",
    "*",
    [
        (PF_INT, "tile_size", "Tile Size (px)", 512),
        (PF_DIRNAME, "output_folder", "Output Folder", os.getcwd()),
    ],
    [],
    slice_and_export,
)

main()
