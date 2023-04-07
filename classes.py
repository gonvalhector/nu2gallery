''' An image file consists of several links:
    - A link to a GIF version of the image (for animated images only)
    - A link to a PNG version of the image
    - A link to a JPG version of the image                            '''
class ImageFile:
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


''' An image object inherits from ImageFile and consists of a label, 
    a caption and several links:
    - A link to a full resolution version of the image
    - A link to a GIF version of the image (for animated images only)
    - A link to a PNG version of the image
    - A link to a JPG version of the image                            '''
class Image(ImageFile):
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


''' A thumbnail object inherits from ImageFile and consists of several links:
    - A link to a GIF version of the thumbnail (for animated thumbs only)
    - A link to a PNG version of the thumbnail
    - A link to a JPG version of the thumbnail                                '''
class Thumbnail(ImageFile):
    # Initializer
    def __init__(self, link_gif=None, link_png="", link_jpg=""):
        super().__init__(link_gif, link_png, link_jpg)

    # Print data
    def print_details(self):
        super().print_details()


''' A video object consists of a type and a url.'''
class Video:
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


''' An external link object consists of a caption, a url,
    and an optional embed link'''
class ExternalLink:
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