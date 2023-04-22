class ImageFile:
    ''' An image file consists of several links:
        - A link to a GIF version of the image (for animated images only)
        - A link to a PNG version of the image
        - A link to a JPG version of the image                            '''

    # Initializer
    def __init__(self, link_gif=None, link_png="", link_jpg=""):
        self.__link_gif = link_gif
        self.__link_png = link_png
        self.__link_jpg = link_jpg

    # Getters and setters
    def get_link_gif(self):
        return self.__link_gif
    
    def set_link_gif(self, link):
        self.__link_gif = link

    def get_link_png(self):
        return self.__link_png
    
    def set_link_png(self, link):
        self.__link_png = link

    def get_link_jpg(self):
        return self.__link_jpg
    
    def set_link_jpg(self, link):
        self.__link_jpg = link

    # Print data
    def print_details(self):
        print("GIF link: ", self.get_link_gif())
        print("PNG link: ", self.get_link_png())
        print("JPG link: ", self.get_link_jpg())


class Image(ImageFile):
    ''' An image object inherits from ImageFile and consists of a label, 
        a caption and several links:
        - A link to a full resolution version of the image
        - A link to a GIF version of the image (for animated images only)
        - A link to a PNG version of the image
        - A link to a JPG version of the image                            '''

    # Initializer
    def __init__(self, label="", caption="", link_full="", link_gif=None, link_png="", link_jpg=""):
        self.__label = label
        self.__caption = caption
        self.__link_full = link_full
        super().__init__(link_gif, link_png, link_jpg)

    # Getters and setters
    def get_label(self):
        return self.__label
    
    def set_label(self, label):
        self.__label = label

    def get_caption(self):
        return self.__caption
    
    def set_caption(self, caption):
        self.__caption = caption

    def get_link_full(self):
        return self.__link_full
    
    def set_link_full(self, link):
        self.__link_full = link

    # Print data
    def print_details(self):
        print("Label: ", self.get_label())
        print("Caption: ", self.get_caption())
        print("Full link: ", self.get_link_full())
        super().print_details()


class Thumbnail(ImageFile):
    ''' A thumbnail object inherits from ImageFile and consists of several links:
        - A link to a GIF version of the thumbnail (for animated thumbs only)
        - A link to a PNG version of the thumbnail
        - A link to a JPG version of the thumbnail                                '''

    # Initializer
    def __init__(self, link_gif=None, link_png="", link_jpg=""):
        super().__init__(link_gif, link_png, link_jpg)

    # Print data
    def print_details(self):
        super().print_details()


class Video:
    ''' A video object consists of a type and a url. '''

    # Initializer
    def __init__(self, type="", url=""):
        self.__type = type
        self.__url = url

    # Getters and setters
    def get_type(self):
        return self.__type
    
    def set_type(self, type):
        self.__type = type

    def get_url(self):
        return self.__url
    
    def set_url(self, url):
        self.__url = url

    # Print data
    def print_details(self):
        print("Type: ", self.get_type())
        print("URL: ", self.get_url())


class ExternalLink:
    ''' An external link object consists of a caption, a url,
        and an optional embed link.                           '''

    # Initializer
    def __init__(self, caption="", url="", embed=None):
        self.__caption = caption
        self.__url = url
        self.__embed = embed

    # Getters and setters
    def get_caption(self):
        return self.__caption
    
    def set_caption(self, caption):
        self.__caption = caption

    def get_url(self):
        return self.__url
    
    def set_url(self, url):
        self.__url = url

    def get_embed(self):
        return self.__embed
    
    def set_embed(self, embed):
        self.__embed = embed

    # Print data
    def print_details(self):
        print("Caption: ", self.get_caption())
        print("URL: ", self.get_url())
        print("Embed link: ", self.get_embed())


class ImageFrontMatter:
    ''' An image front matter object consists of a category, a short name,
        a title, a preview image link, alt text and several lists:
        - A list of ExternalLink class objects.
        - A list of Video class objects.
        - A list of Thumbnail class objects.
        - A list of Image class objects.                                   '''

    # Initializer
    def __init__(self, category="", short_name="", title="", image="", alt=""):
        self.__category = category
        self.__short_name = short_name
        self.__title = title
        self.__image = image
        self.__alt = alt
        self.__external_links = []
        self.__videos = []
        self.__thumbnails = []
        self.__images = []

    # Getters and setters
    def get_category(self):
        return self.__category
    
    def set_category(self, category):
        self.__category = category

    def get_short_name(self):
        return self.__short_name
    
    def set_short_name(self, short_name):
        self.__short_name = short_name

    def get_title(self):
        return self.__title
    
    def set_title(self, title):
        self.__title = title

    def get_image(self):
        return self.__image
    
    def set_image(self, image):
        self.__image = image

    def get_alt(self):
        return self.__alt
    
    def set_alt(self, alt):
        self.__alt = alt

    def get_external_links(self):
        return self.__external_links
    
    def set_external_links(self, external_links):
        self.__external_links = external_links

    def get_videos(self):
        return self.__videos
    
    def set_videos(self, videos):
        self.__videos = videos

    def get_thumbnails(self):
        return self.__thumbnails
    
    def set_thumbnails(self, thumbnails):
        self.__thumbnails = thumbnails

    def get_images(self):
        return self.__images
    
    def set_images(self, images):
        self.__images = images

    # Print data
    def print_details(self):
        print("Category: ", self.get_category())
        print("Short name: ", self.get_short_name())
        print("Title: ", self.get_title())
        print("Image: ", self.get_image())
        print("Alt text: ", self.get_alt())
        print("External links:")
        for link in self.get_external_links():
            link.print_details()
        print("Videos:")
        for video in self.get_videos():
            video.print_details()
        print("Thumbnails:")
        for thumbnail in self.get_thumbnails():
            thumbnail.print_details()
        print("Images:")
        for image in self.get_images():
            image.print_details()