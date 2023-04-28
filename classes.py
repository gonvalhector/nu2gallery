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
        self.__link_gif = self.get_split_link(link)

    def get_link_png(self):
        return self.__link_png
    
    def set_link_png(self, link):
        self.__link_png = self.get_split_link(link)

    def get_link_jpg(self):
        return self.__link_jpg
    
    def set_link_jpg(self, link):
        self.__link_jpg = self.get_split_link(link)

    # Print data
    def print_details(self):
        print("GIF link: ", self.get_link_gif())
        print("PNG link: ", self.get_link_png())
        print("JPG link: ", self.get_link_jpg())

    # Returns a link without the image's width
    def get_split_link(self, link):
        return link.split("=")[0]


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

    # Returns a string with all data correctly formatted
    def get_data(self):
        # Define type of identations for proper line formatting
        indentations = {"default" : "    ", "start" : "- ", "specific" : "  ", "newline" : "\n"}

        # Label line
        data = indentations["default"] + indentations["start"] + "label: " + self.get_label() + indentations["newline"]

        # Caption line
        data += indentations["default"] + indentations["specific"] + "caption: " + self.get_label() + indentations["newline"]

        # Full link line
        data += indentations["default"] + indentations["specific"] + "full: " + self.get_link_full() + indentations["newline"]

        # GIF link line
        if self.get_link_gif():
            data += indentations["default"] + indentations["specific"] + "GIF: " + self.get_link_gif() + indentations["newline"]

        # PNG link line
        data += indentations["default"] + indentations["specific"] + "PNG: " + self.get_link_png() + indentations["newline"]

        # JPG link line
        data += indentations["default"] + indentations["specific"] + "JPG: " + self.get_link_jpg() + indentations["newline"]

        return data


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

    # Returns a string with all data correctly formatted
    def get_data(self):
        # Define type of identations for proper line formatting
        indentations = {"default" : "    ", "newline" : "\n"}

        data = ""

        # GIF link line
        if self.get_link_gif():
            data += indentations["default"] + "GIF: " + self.get_link_gif() + indentations["newline"]

        # PNG link line
        data += indentations["default"] + "PNG: " + self.get_link_png() + indentations["newline"]

        # JPG link line
        data += indentations["default"] + "JPG: " + self.get_link_jpg() + indentations["newline"]

        return data


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
        self.__url = self.get_embed_url(url)

    # Print data
    def print_details(self):
        print("Type: ", self.get_type())
        print("URL: ", self.get_url())

    # Takes a "shareable" url and returns an "embed" url
    def get_embed_url(shareable_url):
        split_url = shareable_url.split("https://youtu.be/")[1]
        return "https://www.youtube.com/embed/" + split_url + "?rel=0"  

    # Returns a string with all data correctly formatted
    def get_data(self):
        # Define type of identations for proper line formatting
        indentations = {"default" : "    ", "start" : "- ", "specific" : "  ", "newline" : "\n"}

        # Type line
        data = indentations["default"] + indentations["start"] + "type: " + self.get_type() + indentations["newline"]

        # URL line
        data += indentations["default"] + indentations["specific"] + "url: " + self.get_url() + indentations["newline"]

        return data       


class Mirror:
    ''' A mirror object consists of a caption and a url. '''
    # Initializer
    def __init__(self, caption="", url=""):
        self.__caption = caption
        self.__url = url

     # Getters and setters
    def get_caption(self):
        return self.__caption
    
    def set_caption(self, caption):
        self.__caption = caption

    def get_url(self):
        return self.__url
    
    def set_url(self, url):
        self.__url = url

    # Print data
    def print_details(self):
        print("Caption: ", self.get_caption())
        print("URL: ", self.get_url())

    # Returns a string with all data correctly formatted
    def get_data(self):
        # Define type of identations for proper line formatting
        indentations = {"default" : "    ", "start" : "- ", "specific" : "  ", "newline" : "\n"}

        # Caption line
        data = indentations["default"] + indentations["start"] + "type: " + self.get_caption() + indentations["newline"]

        # URL line
        data += indentations["default"] + indentations["specific"] + "url: " + self.get_url() + indentations["newline"]

        return data   


class ExternalLink(Mirror):
    ''' An external link object inherits from the Mirror class
        and adds an optional embed link.                       '''

    # Initializer
    def __init__(self, caption="", url="", embed=None):
        super().__init__(caption, url)
        self.__embed = embed

    # Getters and setters
    def get_embed(self):
        return self.__embed
    
    def set_embed(self, embed):
        self.__embed = embed

    # Print data
    def print_details(self):
        super().print_details()
        if self.get_embed():
            print("Embed link: ", self.get_embed())

    # Returns a string with all data correctly formatted
    def get_data(self):
        # Define type of identations for proper line formatting
        indentations = {"default" : "    ", "start" : "- ", "specific" : "  ", "newline" : "\n"}

        # Caption line
        data = indentations["default"] + indentations["start"] + "type: " + self.get_caption() + indentations["newline"]

        # URL line
        data += indentations["default"] + indentations["specific"] + "url: " + self.get_url() + indentations["newline"]

        # Embed line
        if self.get_embed():
            data += indentations["default"] + indentations["specific"] + "embed: " + self.get_embed() + indentations["newline"]

        return data


class ImageFrontMatter:
    ''' An image front matter object consists of a category, a short name,
        a title, a preview image link, alt text, an optional palette, a Thumbnail class object and several lists:
        - A list of ExternalLink class objects.
        - A list of Video class objects.
        - A list of Image class objects.                                                                          
        - An optional list of "mirrors" which is a second list of ExternalLink class objects.                     '''

    # Initializer
    def __init__(self, category="", short_name="", title="", preview="", alt=""):
        self.__category = category
        self.__short_name = short_name
        self.__title = title
        self.__preview = preview
        self.__alt = alt
        self.__external_links = []
        self.__videos = []
        self.__thumbnail = Thumbnail()
        self.__images = []
        self.__palette = None
        self.__mirrors = None

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

    def get_preview(self):
        return self.__preview
    
    def set_preview(self, preview):
        self.__preview = preview

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

    def get_thumbnail(self):
        return self.__thumbnail
    
    def set_thumbnail(self, thumbnail):
        self.__thumbnail = thumbnail

    def get_images(self):
        return self.__images
    
    def set_images(self, images):
        self.__images = images

    def get_palette(self):
        return self.__palette
    
    def set_palette(self, palette):
        self.__palette = palette

    def get_mirrors(self):
        return self.__mirrors
    
    def set_mirrors(self, mirrors):
        self.__mirrors = mirrors

    # Print data
    def print_details(self):
        print("Category: ", self.get_category())
        print("Short name: ", self.get_short_name())
        print("Title: ", self.get_title())
        print("Image: ", self.get_preview())
        print("Alt text: ", self.get_alt())
        print("External links:")
        for link in self.get_external_links():
            link.print_details()
        print("Videos:")
        for video in self.get_videos():
            video.print_details()
        print("Thumbnail:")
        self.get_thumbnail().print_details()
        print("Images:")
        for image in self.get_images():
            image.print_details()
        if self.__palette:
            print("Palette: ", self.get_palette())
            for mirror in self.get_mirrors():
                mirror.print_details()

    # Returns a string with all data correctly formatted
    def get_data(self):
        triple_dashes = "---"
        newline = "\n"

        # Start of front matter data
        data = triple_dashes + newline

        # Category line
        data += "category: " + self.get_category() + newline

        # Short name line
        data += "short_name: " + self.get_short_name() + newline

        # Title line
        data += "title: " + self.get_title() + newline

        # Preview image line
        data += "image: " + self.get_preview() + newline

        # Alternate text line
        data += "alt: " + self.get_alt() + newline

        # External Links lines
        if self.get_external_links():
            data += "external:" + newline
            for link in self.get_external_links():
                data += link.get_data()

        # Videos lines
        if self.get_videos():
            data += "video:" + newline
            for video in self.get_videos():
                data += video.get_data()

        # Palette line
        if self.get_palette():
            data += "palette: " + self.get_palette() + newline
        
        # Mirrors lines
        if self.get_mirrors():
            data += "mirrors:" + newline
            for mirror in self.get_mirrors():
                data += mirror.get_data()

        # Thumbs lines
        data += "thumbs:" + newline
        data += self.get_thumbnail().get_data()

        # Images lines
        data += "images:" + newline
        for image in self.get_images():
            data += image.get_data()

        # End of front matter data
        data += triple_dashes + newline

        return data