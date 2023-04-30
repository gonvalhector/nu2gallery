from pathlib import Path
from classes import Image, Thumbnail, Video, Mirror, ExternalLink, ImageFrontMatter

def main():
    """ Creates a new MD file with front matter that
        helps display a new image from Google Photos in the site's gallery. """
    
    print("Welcome to Nu2Gallery.")
    
    # Create ImageFrontMatter object
    front_matter = ImageFrontMatter()
    
    # Prompt user for new image's category
    category = prompt_category()
    front_matter.set_category(category)

    print()

    # Prompt user for new image's palette
    palette = prompt_palette(category)
    front_matter.set_palette(palette)

    print()

    # Prompt user for palette's mirrors
    mirrors = prompt_mirrors(palette)
    front_matter.set_mirrors(mirrors)

    print()

    # Prompt user for new image's short name
    short_name = prompt_short_name()
    front_matter.set_short_name(short_name)

    print()

    # Prompt user for new image's title
    title = prompt_title(short_name)
    front_matter.set_title(title)

    print()

    # Prompt user for new image's alt text
    alt_text = prompt_alt(short_name)
    front_matter.set_alt(alt_text)

    print()

    # Prompt user for new image's preview image
    preview = prompt_preview(short_name)
    front_matter.set_preview(preview)

    print()

    # Prompt user for external links
    external_links = prompt_external_links(short_name)
    front_matter.set_external_links(external_links)

    print()

    # Prompt user for videos
    videos = prompt_videos(short_name)
    front_matter.set_videos(videos)

    print()

    # Prompt user for thumbnail
    thumbnail = prompt_thumbnail(short_name)
    front_matter.set_thumbnail(thumbnail)

    print()

    # Prompt user for images
    images = prompt_images(short_name)
    front_matter.set_images(images)

    print()

    # Define new image's filename 
    filename = get_filename(short_name)

    print()

    # Write file and exit
    write_file(front_matter.get_data(), filename)


def prompt_category():
    ''' Prompts the user for the image's category and returns it in a string. '''

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


def prompt_short_name():
    ''' Prompts the user for the image's short name and returns it in a string. '''

    # Keep prompting user for valid input
    while True:
        prompt = "What is the new image's SHORT NAME?\n"
        short_name = input(prompt)

        # Check input is valid
        if len(short_name) > 0:
            return short_name
        else:
            print("Invalid input.")


def prompt_title(short_name):
    ''' Prompts the user for the image's title and returns it in a string.
        It takes a short_name argument for its prompt.                     '''

    # Keep prompting user for valid input
    while True:
        prompt = f"What is the TITLE of '{short_name}'?\n"
        title = input(prompt)

        # Check input is valid
        if len(title) > 0:
            return title
        else:
            print("Invalid input.")


def prompt_alt(short_name):
    ''' Prompts the user for the image's alt text and returns it in a string.
        It takes a short_name argument for its prompt.                        '''

    # Keep prompting user for valid input
    while True:
        prompt = f"What is the ALTERNATE TEXT of '{short_name}'?\n"
        alt_text = input(prompt)

        # Check input is valid
        if len(alt_text) > 0:
            return alt_text
        else:
            print("Invalid input.")


def prompt_preview(short_name):
    ''' Prompts the user for the image's preview image link and returns it in a string.
        It takes a short_name argument for its prompt.                                  '''

    # Keep prompting user for valid input
    while True:
        prompt = f"What is the PREVIEW IMAGE of '{short_name}'?\n"
        preview = input(prompt)

        # Check input is valid
        if len(preview) > 0:
            return preview
        else:
            print("Invalid input.")


def prompt_external_link(i):
    ''' Prompts the user for a single external link's data and returns it as an ExternalLink object.
        It takes an iterator as an argument to keep track of the current external link.              '''
    
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
            break
        elif has_embed == "N":
            return external_link
        else:
            print("Invalid input.")

    return external_link


def prompt_external_links(short_name):
    ''' Prompts the user for the image's number of external links and returns
        them as a list of ExternalLink objects.
        It takes a short_name argument for its prompt.                        '''
    
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
                except:
                    print("Invalid input.")
            break
        elif has_external_links == "N":
            print(f"Let's continue with other values for the front matter of '{short_name}'.")
            break
        else:
            print("Invalid input.")
    
    # Return ExternalLink objects list
    return external_links


def prompt_video(i):
    ''' Prompts the user for a single video's data and returns it as a Video object.
        It takes an iterator as an argument to keep track of the current video.      '''
    
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

    # Keep prompting user for valid URL
    while True:
        url_prompt = "Enter the shareable link you copied:\n"
        url = input(url_prompt)

        # Check input is valid
        if len(url) > 0:
            video.set_url(url)
            break
        else:
            print("Invalid input.")

    return video


def prompt_videos(short_name):
    ''' Prompts the user for the image's number of videos and returns
        them as a list of Video objects.
        It takes a short_name argument for its prompt.                '''

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
                except:
                    print("Invalid input.")
            break
        elif has_videos == "N":
            print(f"Let's continue with other values for the front matter of '{short_name}'.")
            break
        else:
            print("Invalid input.")
    
    # Return Video objects list
    return videos


def prompt_thumbnail(short_name):
    ''' Prompts the user for a single thumbnail's data and returns it as a Thumbnail object.
        It takes a short_name argument for its prompt.                                       '''

    # Create Thumbnail object
    print(f"Let's add the thumbnail for '{short_name}'.")
    thumbnail = Thumbnail()

    # Keep prompting user for valid Yes or No input
    while True:
        is_animated_prompt = "Is it an animated thumbnail? [Y (Yes) / N (No)]\n"
        is_animated = input(is_animated_prompt).upper()
        if is_animated == "Y":
            # Keep prompting user for valid GIF link
            while True:
                link_gif_prompt = "Paste the GIF's link:\n"
                link_gif = input(link_gif_prompt)

                # Check input is valid
                if len(link_gif) > 0:
                    thumbnail.set_link_gif(link_gif)
                    break
                else:
                    print("Invalid input.")
            break
        elif is_animated == "N":
            break
        else:
            print("Invalid input.")

    # Keep prompting user for valid PNG link
    while True:
        link_png_prompt = "Paste the PNG's link:\n"
        link_png = input(link_png_prompt)

        # Check input is valid
        if len(link_png) > 0:
            thumbnail.set_link_png(link_png)
            break
        else:
            print("Invalid input.")

    # Keep prompting user for valid JPG link
    while True:
        link_jpg_prompt = "Paste the JPG's link:\n"
        link_jpg = input(link_jpg_prompt)

        # Check input is valid
        if len(link_jpg) > 0:
            thumbnail.set_link_jpg(link_jpg)
            break
        else:
            print("Invalid input.")

    return thumbnail


def prompt_image(i):
    ''' Prompts the user for a single image's data and returns it as an Image object.
        It takes an iterator as an argument to keep track of the current video.       '''
    
    # Create Image object
    image = Image()

    # Keep prompting user for valid label
    while True:
        label_prompt = f"What is image #{i + 1}'s LABEL?\n"
        label = input(label_prompt)

        # Check input is valid
        if len(label) > 0:
            image.set_label(label)
            break
        else:
            print("Invalid input.")

    # Keep prompting user for valid caption
    while True:
        caption_prompt = f"What is image #{i + 1}'s  CAPTION?\n"
        caption = input(caption_prompt)

        # Check input is valid
        if len(caption) > 0:
            image.set_caption(caption)
            break
        else:
            print("Invalid input.")

    # Keep prompting user for valid FULL resolution link
    while True:
        link_full_prompt = "Paste the FULL resolution's link:\n"
        link_full = input(link_full_prompt)

        # Check input is valid
        if len(link_full) > 0:
            image.set_link_full(link_full)
            break
        else:
            print("Invalid input.")

    # Keep prompting user for valid Yes or No input
    while True:
        is_animated_prompt = f"Is image #{i + 1} animated? [Y (Yes) / N (No)]\n"
        is_animated = input(is_animated_prompt).upper()
        if is_animated == "Y":
            # Keep prompting user for valid GIF link
            while True:
                link_gif_prompt = "Paste the GIF's link:\n"
                link_gif = input(link_gif_prompt)

                # Check input is valid
                if len(link_gif) > 0:
                    image.set_link_gif(link_gif)
                    break
                else:
                    print("Invalid input.")
            break
        elif is_animated == "N":
            break
        else:
            print("Invalid input.")

    # Keep prompting user for valid PNG link
    while True:
        link_png_prompt = "Paste the PNG's link:\n"
        link_png = input(link_png_prompt)

        # Check input is valid
        if len(link_png) > 0:
            image.set_link_png(link_png)
            break
        else:
            print("Invalid input.")

    # Keep prompting user for valid JPG link
    while True:
        link_jpg_prompt = "Paste the JPG's link:\n"
        link_jpg = input(link_jpg_prompt)

        # Check input is valid
        if len(link_jpg) > 0:
            image.set_link_jpg(link_jpg)
            break
        else:
            print("Invalid input.")

    return image


def prompt_images(short_name):
    ''' Prompts the user for the image's number of images and returns
        them as a list of Image objects.
        It takes a short_name argument for its prompt.                '''
    # Create Image objects list
    images = []

    # Keep prompting user for valid number of images
    while True:
        try:
            n_prompt = f"How many IMAGES are there for '{short_name}'?\n"
            n = int(input(n_prompt))

            # Check input is valid
            if n > 0:
                # Generate n number of Image objects     
                for i in range(n):
                    image = prompt_image(i)
                    images.append(image)
                break
            else:
                print("Invalid input.")
        except:
            print("Invalid input.")

    # Return Image objects list
    return images


def prompt_palette(category):
    ''' Prompts the user for the image's palette and returns it in a string.
        Takes a category as an argument and returns None if there is no palette. '''

    # A palette and its mirrors are exclusive to images with pixel art category
    if category == "pixel_art":
        # Keep prompting user for valid Yes or No input
        while True:
            has_palette_prompt = "Is there a PALETTE? [Y (Yes) / N (No)]\n"
            has_palette = input(has_palette_prompt).upper()
            if has_palette == "Y":
                # Keep prompting user for valid input
                while True:
                    prompt = "What is the new image's PALETTE?\n"
                    palette = input(prompt)

                    # Check input is valid
                    if len(palette) > 0:
                        return palette
                    else:
                        print("Invalid input.")
            elif has_palette == "N":
                return None
            else:
                print("Invalid input.")
    else:
        return None


def prompt_mirror(i):
    ''' Prompts the user for a single mirror's data and returns it as a Mirror object.
        It takes an iterator as an argument to keep track of the current mirror.       '''
    
    # Create Mirror object
    mirror = Mirror()

    # Keep prompting user for valid caption
    while True:
        caption_prompt = f"What is mirror #{i + 1}'s  CAPTION?\n"
        caption = input(caption_prompt)

        # Check input is valid
        if len(caption) > 0:
            mirror.set_caption(caption)
            break
        else:
            print("Invalid input.")

    # Keep prompting user for valid URL
    while True:
        url_prompt = f"What is mirror #{i + 1}'s URL?\n"
        url = input(url_prompt)

        # Check input is valid
        if len(url) > 0:
            mirror.set_url(url)
            break
        else:
            print("Invalid input.")

    return mirror


def prompt_mirrors(palette):
    ''' Prompts the user for the image's number of mirrors and returns them as 
        a list of Mirror objects.                              
        Takes a palette as an argument and returns None if there is no palette. '''
    
    # Mirrors are only created if a palette is given
    if palette:
        # Create empty Mirror objects list
        mirrors = []

        # Keep prompting user for valid number of mirrors
        while True:
            try:
                n_prompt = "How many MIRRORS are there?\n"
                n = int(input(n_prompt))

                # Check input is valid
                if n > 0:
                    # Generate n number of Mirror objects
                    for i in range(n):
                        mirror = prompt_mirror(i)
                        mirrors.append(mirror) 
                    break    
                else:
                    print("Invalid input.")
            except:
                print("Invalid input.")
        
        # Return Mirror objects list
        return mirrors
    else:
        return None


def get_filename(short_name):
    ''' Prompts the user for the image's posting date and returns a filename in a string.
        It takes a short name argument for the prompts and filename.                      '''

    # Define dates for the prompts
    date_prompts = ("YEAR", "MONTH", "DAY")
    date_values = []

    for prompt in date_prompts:
        # Keep prompting the user for valid input
        while True:
            date_value = input(f"What {prompt} was '{short_name}' posted?\n")
            # Check input is a number
            if date_value.isnumeric():
                date_values.append(date_value)
                break
            else:
                print("Invalid input.")       
    filename = date_values[0] + "-" + date_values[1] + "-" + date_values[2] + "-" + short_name + ".md"

    return filename


def write_file(data, filename):
    ''' Prints the front matter of the image and prompts the user for 
        confirmation to write the file.
        Takes data string to print and a filename string to write the final file. '''

    # Print formatted front matter data
    print("Here's the front matter:")
    print(data)

    # Keep prompting the user for a valid Yes or No input
    while True:
        confirm = input(f"Do you want '{filename}' to be written with that front matter? [Y (Yes) / N (No)]\n").upper()
        if confirm == "Y":
            print(f"Writing '{filename}' ...")
            # Get current directory
            current_dir = Path(__file__).parent
            # Define directory to write file to
            images_dir = current_dir / "images"
            # Create directory if it doesn't exist
            if not images_dir.exists():
                images_dir.mkdir()
            # Write the final file
            path = images_dir / filename
            file = open(path, 'w')
            file.write(data)
            print(f"'{filename}' was succesfully created inside /images directory.")
            print("Thank you for using Nu2Gallery.")
            exit()
        elif write_file == "N":
            print("Thank you for using Nu2Gallery.")
            exit()
        else:
            print("Invalid input.")


if __name__ == "__main__":
    main()
