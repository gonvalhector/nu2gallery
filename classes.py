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


''' An image object inherits from ImageFile and consists of a label, 
    a caption and several links:
    - A link to a full resolution version of the image
    - A link to a GIF version of the image (for animated images only)
    - A link to a PNG version of the image
    - A link to a JPG version of the image                            '''
class Image(ImageFile):
    # Initializer
    def __init__(self, label="", caption="", link_full="", /
                link_gif=None, link_png="", link_jpg=""):
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