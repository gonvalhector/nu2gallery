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
    
    # Test Video class
    VideoTests()
    print()

    # Test ExternalLink class
    ExternalLinkTests()
    print()

    '''

    # Test ImageFrontMatter class
    ImageFrontMatterTests()
    print()


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

    '''
    # Testing the proper implementation of an external link object
    el1 = ExternalLink("Instagram", "ig", "embed-link")
    el1.print_details()

    print()

    # Testing an external link object with no arguments passed
    el2 = ExternalLink()
    el2.print_details()
    '''

    # Test for proper implementation of get_data() with embed link
    el = ExternalLink()
    el.set_caption("Instagram")
    el.set_url("ig")
    el.set_embed("https://www.instagram.com/p/CEMjnnMnwkh/?utm_source=ig_embed&amp;utm_campaign=loading")
    print(el.get_data())

    # Test for proper implementation of get_data() with no embed link
    el2 = ExternalLink()
    el2.set_caption("GameJolt")
    el2.set_url("https://gamejolt.com/p/yay-for-videos-video-version-of-my-ruins-of-a-church-animated-pi-tqchpznm")
    print(el2.get_data())


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

    # Test for proper implementation of get_data() with no palette and mirrors
    ifm = ImageFrontMatter()

    ifm.set_category("pixel_art")
    ifm.set_short_name("roac_animated")
    ifm.set_title("Ruins of a Church Animated")
    ifm.set_preview("https://lh3.googleusercontent.com/pw/ACtC-3egaI1Wc9dhcGCoUxyEd5do=w1200-h630-no?authuser=0")
    ifm.set_alt("Animated pixel art painting of a church in ruins")

    external_links = []
    el = ExternalLink()
    el.set_caption("Instagram")
    el.set_url("ig")
    el.set_embed("https://www.instagram.com/p/CEMjnnMnwkh/?utm_source=ig_embed&amp;utm_campaign=loading")
    external_links.append(el)
    el2 = ExternalLink()
    el2.set_caption("GameJolt")
    el2.set_url("https://gamejolt.com/p/yay-for-videos-video-version-of-my-ruins-of-a-church-animated-pi-tqchpznm")
    external_links.append(el2)
    ifm.set_external_links(external_links)

    videos = []
    video = Video()
    video.set_type("Animation")
    video.set_url("https://youtu.be/LioP2bn03sY")
    videos.append(video)
    ifm.set_videos(videos)

    thumb = Thumbnail()
    thumb.set_link_gif("https://lh3.googleusercontent.com/pw/AM-JKLWKRht0Z=s1080")
    thumb.set_link_png("https://lh3.googleusercontent.com/pw/AM-JKLUYD5yoV=s1080")
    thumb.set_link_jpg("https://lh3.googleusercontent.com/pw/AM-JKLWdajfvb=s1080")
    ifm.set_thumbnail(thumb)

    images = []
    image = Image()
    image.set_label("Final Version")
    image.set_caption("Designed with 60fps in mind.")
    image.set_link_full("https://lh3.googleusercontent.com/pw/AM-JKLVrBC8U=s1080")
    image.set_link_gif("https://lh3.googleusercontent.com/pw/AM-JKLWKRht0Z=s1080")
    image.set_link_png("https://lh3.googleusercontent.com/pw/AM-JKLUYD5yoV=s1080")
    image.set_link_jpg("https://lh3.googleusercontent.com/pw/AM-JKLWdajfvb=s1080")
    images.append(image)
    ifm.set_images(images)

    print(ifm.get_data())

    print()

    # Test for proper implementation of get_data() with palette and mirrors
    ifm2 = ImageFrontMatter()

    ifm2.set_category("pixel_art")
    ifm2.set_short_name("roac_animated")
    ifm2.set_title("Ruins of a Church Animated")
    ifm2.set_preview("https://lh3.googleusercontent.com/pw/ACtC-3egaI1Wc9dhcGCoUxyEd5do=w1200-h630-no?authuser=0")
    ifm2.set_alt("Animated pixel art painting of a church in ruins")
    ifm2.set_palette("DS-34")

    mirrors = []
    mirror = Mirror()
    mirror.set_caption("Zip File")
    mirror.set_url("/assets/downloads/palettes/ds-34 palette.zip")
    mirrors.append(mirror)
    mirror2 = Mirror()
    mirror2.set_caption("Gdrive")
    mirror2.set_url("https://drive.google.com/drive/foldersVUp9QVWIPloV?usp=sharing")
    mirrors.append(mirror2)
    ifm2.set_mirrors(mirrors)

    external_links = []
    el = ExternalLink()
    el.set_caption("Instagram")
    el.set_url("ig")
    el.set_embed("https://www.instagram.com/p/CEMjnnMnwkh/?utm_source=ig_embed&amp;utm_campaign=loading")
    external_links.append(el)
    el2 = ExternalLink()
    el2.set_caption("GameJolt")
    el2.set_url("https://gamejolt.com/p/yay-for-videos-video-version-of-my-ruins-of-a-church-animated-pi-tqchpznm")
    external_links.append(el2)
    ifm2.set_external_links(external_links)

    videos = []
    video = Video()
    video.set_type("Animation")
    video.set_url("https://youtu.be/LioP2bn03sY")
    videos.append(video)
    ifm2.set_videos(videos)

    thumb = Thumbnail()
    thumb.set_link_gif("https://lh3.googleusercontent.com/pw/AM-JKLWKRht0Z=s1080")
    thumb.set_link_png("https://lh3.googleusercontent.com/pw/AM-JKLUYD5yoV=s1080")
    thumb.set_link_jpg("https://lh3.googleusercontent.com/pw/AM-JKLWdajfvb=s1080")
    ifm2.set_thumbnail(thumb)

    images = []
    image = Image()
    image.set_label("Final Version")
    image.set_caption("Designed with 60fps in mind.")
    image.set_link_full("https://lh3.googleusercontent.com/pw/AM-JKLVrBC8U=s1080")
    image.set_link_gif("https://lh3.googleusercontent.com/pw/AM-JKLWKRht0Z=s1080")
    image.set_link_png("https://lh3.googleusercontent.com/pw/AM-JKLUYD5yoV=s1080")
    image.set_link_jpg("https://lh3.googleusercontent.com/pw/AM-JKLWdajfvb=s1080")
    images.append(image)
    ifm2.set_images(images)

    print(ifm2.get_data())


if __name__ == "__main__":
    main()