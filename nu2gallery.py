from pathlib import Path
from classes import Image, Thumbnail, Video, ExternalLink, ImageFrontMatter

def main():
    """ Creates a new MD file with front matter that
        helps display a new image from Google Photos in the site's gallery. """
    
    print("Welcome to Nu2Gallery.")
    
    # Create ImageFrontMatter object
    front_matter = ImageFrontMatter()
    
    # Prompt user for new image's category
    category = prompt_category()
    front_matter.set_category(category)

    # Prompt user for new image's short name
    short_name = prompt_short_name()
    front_matter.set_short_name(short_name)

    # Prompt user for new image's title
    title = prompt_title(short_name)
    front_matter.set_title(title)

    # Prompt user for new image's alt text
    alt_text = prompt_alt(short_name)
    front_matter.set_alt(alt_text)

    # Prompt user for new image's preview image
    preview = prompt_preview(short_name)
    front_matter.set_preview(preview)

    # Prompt user for external links
    external_links = prompt_external_links(short_name)
    front_matter.set_external_links(external_links)

    # Prompt user for videos
    videos = prompt_videos(short_name)
    front_matter.set_videos(videos)

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

    # Date and filename
    date_args = ["YEAR", "MONTH", "DAY"]
    date_values = []
    for arg in date_args:
        date_value = input(f"What {arg} was '{short_name}' posted?\n")
        date_values.append(date_value)
    filename = date_values[0] + "-" + date_values[1] + "-" + date_values[2] + "-" + short_name + ".md" 

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


def prompt_category():
    ''' Prompt the user for the image's category and returns it in a string. '''

    # All categories
    categories = {"A": "pixel_art", "B": "watercolor_art",
                  "C": "digital_art", "D": "sketches",
                  "E": "blog_pictures"}

    # Keep prompting user for valid input
    while True:
        prompt = "What is the new image's CATEGORY? [A (Pixel Art)/ B (Watercolor Art)/ C (Digital Art)/ D (Sketches)/ E (Blog Pictures)]\n"
        category = input(prompt).upper()

        # Check input is valid
        if category in categories:
            return categories[category]
        else:
            print("Invalid input.")
            continue


def prompt_short_name():
    ''' Prompt the user for the image's short name and returns it in a string.'''

    # Keep prompting user for valid input
    while True:
        prompt = "What is the new image's SHORT NAME?\n"
        short_name = input(prompt)

        # Check input is valid
        if len(short_name) > 0:
            return short_name
        else:
            print("Invalid input.")
            continue


def prompt_title(short_name):
    ''' Prompt the user for the image's title and returns it in a string.
        It takes a short_name argument for its prompt.                    '''

    # Keep prompting user for valid input
    while True:
        prompt = f"What is the TITLE of '{short_name}'?\n"
        title = input(prompt)

        # Check input is valid
        if len(title) > 0:
            return title
        else:
            print("Invalid input.")
            continue


def prompt_alt(short_name):
    ''' Prompt the user for the image's alt text and returns it in a string.
        It takes a short_name argument for its prompt.                       '''

    # Keep prompting user for valid input
    while True:
        prompt = f"What is the ALTERNATE TEXT of '{short_name}'?\n"
        alt_text = input(prompt)

        # Check input is valid
        if len(alt_text) > 0:
            return alt_text
        else:
            print("Invalid input.")
            continue


def prompt_preview(short_name):
    ''' Prompt the user for the image's preview image link and returns it in a string.
        It takes a short_name argument for its prompt.                                 '''

    # Keep prompting user for valid input
    while True:
        prompt = f"What is the PREVIEW IMAGE of '{short_name}'?\n"
        preview = input(prompt)

        # Check input is valid
        if len(preview) > 0:
            return preview
        else:
            print("Invalid input.")
            continue


def prompt_external_link(i):
    ''' Prompt the user for the image's external link and returns it as an ExternalLink object.
        It takes an iterator as an argument to keep track of the current external link.         '''
    
    # Create ExternalLink object
    external_link = ExternalLink()

    # Keep prompting user for valid caption
    while True:
        caption_prompt = f"What is external link #{i + 1}'s  CAPTION?\n"
        caption = input(caption_prompt)

        # Check input is valid
        if len(caption) > 0:
            external_link.set_caption(caption)
            break
        else:
            print("Invalid input.")
            continue

    # Keep prompting user for valid URL
    while True:
        url_prompt = f"What is external link #{i + 1}'s URL?\n"
        url = input(url_prompt)

        # Check input is valid
        if len(url) > 0:
            external_link.set_url(url)
            break
        else:
            print("Invalid input.")
            continue

    # Keep prompting user for valid Yes or No input
    while True:
        has_embed_prompt = "Is there an external object to EMBED [Y (Yes) / N (No)]?\n"
        has_embed = input(has_embed_prompt).upper()

        # Check input is valid
        if has_embed == "Y":
            # Keep prompting user for valid embed object link
            while True:
                embed_prompt = "What is the link to the EMBED object?\n"
                embed = input(embed_prompt)

                # Check input is valid
                if len(embed) > 0:
                    external_link.set_embed(embed)
                    break
                else:
                    print("Invalid input.")
                    continue
            break
        elif has_embed == "N":
            return external_link
        else:
            print("Invalid input.")
            continue
    return external_link


def prompt_external_links(short_name):
    ''' Prompts the user for the image's number of external links and returns
        them as a list of ExternalLink objects.
        It takes a short_name argument for its prompt.                                          '''
    
    # Create empty ExternalLink objects list
    external_links = []

    # Keep prompting user for valid Yes or No input
    while True:
        has_external_links_prompt = "Are there any EXTERNAL LINKS [Y (Yes) / N (No)]?\n"
        has_external_links = input(has_external_links_prompt).upper()

        # Check input is valid
        if has_external_links == "Y":
            # Keep prompting user for valid number of external links
            while True:
                try:
                    n_prompt = f"How many EXTERNAL LINKS are there in '{short_name}'?\n"
                    n = int(input(n_prompt))

                    # Check input is valid
                    if n > 0:
                        # Generate n number of ExternalLink objects
                        for i in range(n):
                            external_link = prompt_external_link(i)
                            external_links.append(external_link) 
                        break    
                    else:
                        print("Invalid input.")
                        continue
                except:
                    print("Invalid input.")
                    continue
            break
        elif has_external_links == "N":
            print(f"Let's continue with other values for the front matter of '{short_name}'.")
            break
        else:
            print("Invalid input.")
            continue
    
    # Return ExternalLink objects list
    return external_links


def prompt_video(i):
    ''' Prompt the user for the image's video and returns it as a Video object.
        It takes an iterator as an argument to keep track of the current video. '''
    
    # Create Video object
    video = Video()

    # Keep prompting user for valid type
    while True:
        type_prompt = f"What TYPE of video is video #{i + 1}?\n"
        type = input(type_prompt)

        # Check input is valid
        if len(type) > 0:
            video.set_type(type)
            print(f"Let's add a URL for video #{i + 1}.")
            break
        else:
            print("Invalid input.")
            continue

    # Keep prompting user for valid URL
    while True:
        url_prompt = "Enter the shareable link you copied:\n"
        shareable_url = input(url_prompt)

        # Check input is valid
        if len(shareable_url) > 0:
            # Transform shareable YT link to embed link
            split_url = shareable_url.split("https://youtu.be/")[1]
            url = "https://www.youtube.com/embed/" + split_url + "?rel=0"
            video.set_url(url)
            break
        else:
            print("Invalid input.")
            continue
    return Video


def prompt_videos(short_name):
    ''' Prompts the user for the image's number of videos and returns
        them as a list of Video objects.
        It takes a short_name argument for its prompt.                                          '''

    # Create empty Video objects list
    videos = []

    # Keep prompting user for valid Yes or No input
    while True:
        has_videos_prompt = f"Are there any Youtube VIDEOS for '{short_name}'? [Y (Yes) / N (No)]\n"
        has_videos = input(has_videos_prompt).upper()
        if has_videos == "Y":
            # Keep prompting user for valid number of videos
            while True:
                try:
                    n_prompt = f"How many VIDEOS are there for '{short_name}'?\n"
                    n = int(input(n_prompt))

                    # Check input is valid
                    if n > 0:
                        # Generate n number of Video objects     
                        for i in range(n):
                            video = prompt_video(i)
                            videos.append(video)
                        break
                    else:
                        print("Invalid input.")
                        continue
                except:
                    print("Invalid input.")
                    continue
            break
        elif has_videos == "N":
            print(f"Let's continue with other values for the front matter of '{short_name}'.")
            break
        else:
            print("Invalid input.")
            continue
    
    # Return Video objects list
    return videos


def prompt_thumbnail():
    pass


def prompt_image():
    pass


def write_file():
    pass


if __name__ == "__main__":
    main()
