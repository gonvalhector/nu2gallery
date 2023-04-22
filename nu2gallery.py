from pathlib import Path
from classes import Image, Thumbnail, Video, ExternalLink, ImageFrontMatter

def main():
    """ Creates a new MD file with front matter that
        helps display a new image from Google Photos in the site's gallery. """
    
    print("Welcome to Nu2Gallery.")
    
    # Create ImageFrontMatter object
    front_matter = ImageFrontMatter()
    
    # Prompt user for new image category
    category = promt_category()
    front_matter.set_category(category)

    # Short name
    short_name = input("What is the short_name of the new image?\n")
    front_matter += "short_name: " + short_name + "\n"

    # Date and filename
    date_args = ["YEAR", "MONTH", "DAY"]
    date_values = []
    for arg in date_args:
        date_value = input(f"What {arg} was '{short_name}' posted?\n")
        date_values.append(date_value)
    filename = date_values[0] + "-" + date_values[1] + "-" + date_values[2] + "-" + short_name + ".md"

    # Title
    title = input(f"What is the title of '{short_name}'?\n")
    front_matter += "title: " + title + "\n"

    # Alt text
    alt = input(f"What is the alternate text of '{short_name}'?\n")
    front_matter += "alt: " + alt + "\n"

    # Prompt user for yotube video link
    while True:
        is_video = input(f"Is there a Youtube video for '{short_name}'? [Y/N]\n")
        if is_video == "Y" or is_video == "y":
            front_matter += "video:\n"
            video_n = int(input(f"How many videos are there for '{short_name}'?\n"))
            for i in range(video_n):
                video_type = input(f"What is the type of video for video #{i + 1}?\n")
                print(f"Let's add a link for video #{i + 1}'s Youtube video.")
                # Promp the user for the original link
                og_link = input(f"Enter the shareable link you copied:\n")
                separated_link = og_link.split("https://youtu.be/")
                video = "https://www.youtube.com/embed/" + separated_link[1] + "?rel=0"
                front_matter += "   - type: " + video_type + "\n"
                front_matter += "     url: " + video + "\n"
                break
            break
        elif is_video == "N" or is_video == "n":
            print(f"Let's continue with other values for the front matter of '{short_name}'.")
            break
        else:
            print("Invalid input.")
            continue

    # Prompt user for palette
    while True:
        is_palette = input(f"Is there a Palette to share for '{short_name}'? [Y/N]\n")
        if is_palette == "Y" or is_palette == "y":
            palette_name = input("What is the palette's name?")
            front_matter += "palette: " + palette_name + "\n"
            mirror_n = input(f"How many mirrors for the download link are there for '{palette_name}'?\n")
            for i in range(mirror_n):
                caption = input(f"What is the caption for mirror #{i + 1}?\n")
                print(f"Let's add a link for mirror #{i + 1}.")
                # Promp the user for the original link
                url = input(f"Enter the full link:\n")
                front_matter += "   - caption: " + caption + "\n"
                front_matter += "     url: " + url + "\n"
                break
        elif is_palette == "N" or is_palette == "n":
            print(f"Let's continue with other values for the front matter of '{short_name}'.")
            break
        else:
            print("Invalid input.")
            continue

    # Add thumbnail links
    print("Let's add the thumbnails.")
    front_matter += "thumbs:\n"
    extensions = []
    thumb_bases = []

    # If there is an animated image and thumbnail
    while True:
        isanimated = input(f"Is there an animated image? [Y/N]\n")
        if isanimated == "Y" or isanimated == "y":
            animated = True
            break
        elif isanimated == "N" or isanimated == "n":
            animated = False
            break
        else:
            print("Invalid input.")
            continue
    if animated:
        full_thumb_GIF = input(f"What is the link for the GIF thumbnail of '{short_name}'?\n")
        thumb_GIF = full_thumb_GIF.split("=")
        thumb_bases.append(thumb_GIF[0])
        extensions.append("GIF")
    full_thumb_PNG = input(f"What is the link for the PNG thumbnail of '{short_name}'?\n")
    thumb_PNG = full_thumb_PNG.split("=")
    thumb_bases.append(thumb_PNG[0])
    extensions.append("PNG")
    full_thumb_JPG = input(f"What is the link for the JPG thumbnail of '{short_name}'?\n")
    thumb_JPG = full_thumb_JPG.split("=")
    thumb_bases.append(thumb_JPG[0])
    extensions.append("JPG")

    # Image widths in relation to screen widths
    thumb_scr_w = {"w1920": "=w355", "w1024": "=w284", "w768": "=w213", "w600": "=w166", "w411": "=w114", "w360": "=w100", "w240": "=w66"}
    for k, v in thumb_scr_w.items():
        for i in range(len(thumb_bases)):
            front_matter += f"    {k}_{extensions[i]}: " + thumb_bases[i] + v + "\n"

    print("Let's add the images.")

    # Prompt the user for a number of images
    while True:
        # Convert input string to integer
        try:
            n = int(input(f"How many images does '{short_name}' have?\n"))
        except ValueError:
            print("Invalid input.")
            continue
        else:
            break

    # List of images and their values
    if n > 0:
        front_matter += "images:\n"
        for j in range(n):
            extensions = []
            image_bases = []
            label = input(f"Image #{j + 1} LABEL:\n")
            front_matter += "    - label: " + label + "\n"
            caption = input(f"Image #{j + 1} CAPTION:\n")
            front_matter += "      caption: " + caption + "\n"
            full = input(f"Image #{j + 1} FULL size image link:\n")
            full_lst = full.split("=")
            front_matter += "      full: " + full_lst[0] + "=w1080" + "\n"
            if animated:
                while True:
                    isGIF = input(f"Is image #{j + 1} an animated image? [Y/N]\n")
                    if isGIF == "Y" or isGIF == "y":
                        full_image_GIF = input(f"What is the link for the GIF of image #{j + 1}?\n")
                        image_GIF = full_image_GIF.split("=")
                        image_bases.append(image_GIF[0])
                        extensions.append("GIF")
                        break
                    elif isGIF == "N" or isGIF == "n":
                        break
                    else:
                        print("Invalid input.")
                        continue
            full_image_PNG = input(f"What is the link for the PNG of image #{j + 1}?\n")
            image_PNG = full_image_PNG.split("=")
            image_bases.append(image_PNG[0])
            extensions.append("PNG")
            full_image_JPG = input(f"What is the link for the JPG of image #{j + 1}?\n")
            image_JPG = full_image_JPG.split("=")
            image_bases.append(image_JPG[0])
            extensions.append("JPG")
            # Image widths in relation to screen widths
            image_scr_w = {"w1920": "=w850", "w1024": "=w711", "w768": "=w533", "w600": "=w416", "w411": "=w285", "w360": "=w250", "w240": "=w166"}
            for k, v in image_scr_w.items():
                for l in range(len(image_bases)):
                    front_matter += f"      {k}_{extensions[l]}: " + image_bases[l] + v + "\n"

    front_matter += "---"

    # Prompt user for confirmation to write file
    print(front_matter)
    while True:
        write_file = input(f"Do you want '{filename}' to be written with that front matter? [Y/N]\n")
        if write_file == "Y" or write_file == "y":
            print(f"Writing '{filename}' ...")
            current_dir = Path(__file__).parent
            path = current_dir / filename
            file = open(path, 'w')
            file.write(front_matter)
            print(f"'{filename}' succesfully created.")
            print("Thank you for using Nu2Gallery.")
            exit()
        elif write_file == "N" or write_file == "n":
            print("Thank you for using Nu2Gallery.")
            exit()
        else:
            print("Invalid input.")
            continue


def promt_category():
    ''' Prompt the user for the image category and returns it in a string. '''

    # All categories
    categories = {"A": "pixel_art", "B": "watercolor_art",
                  "C": "digital_art", "D": "sketches",
                  "E": "blog_pictures"}

    # Keep prompting user for valid input
    while True:
        prompt = "What is the image CATEGORY? [A (Pixel Art)/ B (Watercolor Art)/ C (Digital Art)/ D (Sketches)/ E (Blog Pictures)]\n"
        category = input(prompt).upper()

        # Check input is valid
        if category in categories:
            return categories[category]
        else:
            print("Invalid input.")
            continue


def prompt_short_name():
    pass


def prompt_title():
    pass


def prompt_alt():
    pass


def prompt_external_link():
    pass


def prompt_thumbnail():
    pass


def prompt_video():
    pass


def prompt_image():
    pass


def write_file():
    pass


if __name__ == "__main__":
    main()
