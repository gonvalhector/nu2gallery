''' An image object consists of a label, a caption and several links:
    - A link to a full resolution version of the image
    - A link to a GIF version of the image (for animated images only)
    - A link to a PNG version of the image
    - A link to a JPG version of the image                            '''
class Image:
    def __init__(self, label="", caption="", link_full="", /
                link_GIF=None, link_PNG="", link_JPG=""):
        self.label = label
        self.caption = caption
        self.link_full = link_full
        self.link_GIF = link_GIF
        self.link_PNG = link_PNG
        self.link_JPG = link_JPG