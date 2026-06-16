import os
import glob

GALLERY_DIR = "gallery"
TEMPLATE = "gallery-template.qmd"
OUTPUT = "gallery.qmd"

# read your template header (title, lightbox, etc.)
with open(TEMPLATE, "r") as f:
    header = f.read()

tabs = ["::: {.panel-tabset}\n"]

# each subfolder becomes a tab
for folder in sorted(os.listdir(GALLERY_DIR)):
    folder_path = os.path.join(GALLERY_DIR, folder)
    if not os.path.isdir(folder_path):
        continue

    # tab label: replace hyphens with spaces, title-case it
    label = folder.replace("-", " ").title()
    tabs.append(f"## {label}\n")
    tabs.append('::: {layout="[[1,1,1]]"}\n')

    images = sorted(glob.glob(f"{folder_path}/*.jpg") +
                    glob.glob(f"{folder_path}/*.jpeg") +
                    glob.glob(f"{folder_path}/*.png") +
                    glob.glob(f"{folder_path}/*.webp"))

    for img in images:
        img_path = img.replace("\\", "/")  # windows safety
        tabs.append(f"![]({img_path})\n")

    tabs.append(":::\n")

tabs.append(":::\n")

with open(OUTPUT, "w") as f:
    f.write(header)
    f.write("\n")
    f.write("\n".join(tabs))

print(f"Generated {OUTPUT} with {len(os.listdir(GALLERY_DIR))} tabs.")