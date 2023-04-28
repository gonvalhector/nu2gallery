from classes import Image, Thumbnail, Video, Mirror, ExternalLink, ImageFrontMatter


def main():
    '''Calls all test functions. '''

    '''
    # Test Image class
    ImageTests()
    print()

    # Test Thumbnail class
    ThumbnailTests()
    print()
    
    '''
    # Test Video class
    VideoTests()
    print()

    '''
    # Test ExternalLink class
    ExternalLinkTests()
    print()

    # Test ImageFrontMatter class
    ImageFrontMatterTests()
    print()
    '''


def ImageTests():
    ''' Tests for Image class objects. '''

    print("Images:")
    print()

    # Testing the proper implementation of an image object and inheritance of the ImageFile class
    #image1 = Image("Final Version", "Designed with 60fps in mind.", "full-link", "gif-link", "png-link", "jpg-link")
    #image1.print_details()
    #print()

    # Testing an image object with no arguments passed
    #image2 = Image()
    #image2.print_details()

    # Test for proper implementation of get_data() with animated image
    image = Image()
    image.set_label("Final Version")
    image.set_caption("Designed with 60fps in mind.")
    image.set_link_full("https://lh3.googleusercontent.com/pw/AM-JKLVrBC8U=s1080")
    image.set_link_gif("https://lh3.googleusercontent.com/pw/AM-JKLWKRht0Z=s1080")
    image.set_link_png("https://lh3.googleusercontent.com/pw/AM-JKLUYD5yoV=s1080")
    image.set_link_jpg("https://lh3.googleusercontent.com/pw/AM-JKLWdajfvb=s1080")
    print(image.get_data())

    # Test for proper implementation of get_data() with no animated image
    image2 = Image()
    image2.set_label("Final Version")
    image2.set_caption("Designed with 60fps in mind.")
    image2.set_link_full("https://lh3.googleusercontent.com/pw/AM-JKLVrBC8U=s1080")
    image2.set_link_png("https://lh3.googleusercontent.com/pw/AM-JKLUYD5yoV=s1080")
    image2.set_link_jpg("https://lh3.googleusercontent.com/pw/AM-JKLWdajfvb=s1080")
    print(image2.get_data())

def ThumbnailTests():
    ''' Tests for Thumbnail class objects. '''

    print("Thumbnails:")
    print()

    '''
    # Testing the proper implementation of a thumbnail object and inheritance of the ImageFile class
    thumb1 = Thumbnail("gif-link", "png-link", "jpg-link")
    thumb1.print_details()

    print()

    # Testing a thumbnail object with no arguments passed
    thumb2 = Thumbnail()
    thumb2.print_details()
    '''

    # Test for proper implementation of get_data() with animated thumbnail
    thumb = Thumbnail()
    thumb.set_link_gif("https://lh3.googleusercontent.com/pw/AM-JKLWKRht0Z=s1080")
    thumb.set_link_png("https://lh3.googleusercontent.com/pw/AM-JKLUYD5yoV=s1080")
    thumb.set_link_jpg("https://lh3.googleusercontent.com/pw/AM-JKLWdajfvb=s1080")
    print(thumb.get_data())

    # Test for proper implementation of get_data() with no animated thumbnail
    thumb2 = Thumbnail()
    thumb2.set_link_png("https://lh3.googleusercontent.com/pw/AM-JKLUYD5yoV=s1080")
    thumb2.set_link_jpg("https://lh3.googleusercontent.com/pw/AM-JKLWdajfvb=s1080")
    print(thumb2.get_data())


def VideoTests():
    ''' Tests for Video class objects. '''

    print("Videos:")
    print()

    '''
    # Testing the proper implementation of a video object
    video1 = Video("Animation", "video-url")
    video1.print_details()

    print()

    # Testing a video object with no arguments passed
    video2 = Video()
    video2.print_details()
    '''

    # Test for proper implementation of get_data()
    video = Video()
    video.set_type("Animation")
    video.set_url("https://youtu.be/LioP2bn03sY")
    print(video.get_data())


def ExternalLinkTests():
    ''' Tests for ExternalLink class objects. '''

    print("External Links:")
    print()

    # Testing the proper implementation of an external link object
    el1 = ExternalLink("Instagram", "ig", "embed-link")
    el1.print_details()

    print()

    # Testing an external link object with no arguments passed
    el2 = ExternalLink()
    el2.print_details()


def ImageFrontMatterTests():
    ''' Tests for ImageFrontMatter class objects. '''

    print("Image Front Matter:")
    print()

    '''
    # Testing the proper implementation of an image front matter object
    ifm1 = ImageFrontMatter("categories", "short-name", "title", "image", "alt")
    ifm1.print_details()

    print()

    # Testing an image front matter object with no arguments passed
    ifm2 = ImageFrontMatter()
    ifm2.print_details()

    print()

    # Testing the proper implementation of palette and mirrors properties
    ifm3 = ImageFrontMatter()
    ifm3.set_palette("DS-34")
    mirrors = []
    mirrors.append(Mirror("Zip File", "/assets/downloads/palettes/ds-34 palette.zip"))
    ifm3.set_mirrors(mirrors)
    ifm3.print_details()    
    '''

    # Test for proper implementation of get_data()
    ifm = ImageFrontMatter()

    image = Image()
    image.set_label("Final Version")
    image.set_caption("Designed with 60fps in mind.")
    image.set_link_full("https://lh3.googleusercontent.com/pw/AM-JKLVrBC8U=s1080")
    image.set_link_gif("https://lh3.googleusercontent.com/pw/AM-JKLWKRht0Z=s1080")
    image.set_link_png("https://lh3.googleusercontent.com/pw/AM-JKLUYD5yoV=s1080")
    image.set_link_jpg("https://lh3.googleusercontent.com/pw/AM-JKLWdajfvb=s1080")

    thumb = Thumbnail()
    thumb.set_link_gif("https://lh3.googleusercontent.com/pw/AM-JKLWKRht0Z=s1080")
    thumb.set_link_png("https://lh3.googleusercontent.com/pw/AM-JKLUYD5yoV=s1080")
    thumb.set_link_jpg("https://lh3.googleusercontent.com/pw/AM-JKLWdajfvb=s1080")


if __name__ == "__main__":
    main()