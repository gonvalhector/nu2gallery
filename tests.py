from classes import Image, Thumbnail, Video, ExternalLink, ImageFrontMatter


def main():
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

    # Test ImageFrontMatter class
    ImageFrontMatterTests()
    print()

# Tests for Image class objects
def ImageTests():
    print("Images:")
    print()

    # Testing the proper implementation of an image object and inheritance of the ImageFile class
    image1 = Image("Final Version", "Designed with 60fps in mind.", "full-link", "gif-link", "png-link", "jpg-link")
    image1.print_details()

    print()

    # Testing an image object with no arguments passed
    image2 = Image()
    image2.print_details()


# Tests for Thumbnail class objects
def ThumbnailTests():
    print("Thumbnails:")
    print()

    # Testing the proper implementation of a thumbnail object and inheritance of the ImageFile class
    thumb1 = Thumbnail("gif-link", "png-link", "jpg-link")
    thumb1.print_details()

    print()

    # Testing a thumbnail object with no arguments passed
    thumb2 = Thumbnail()
    thumb2.print_details()


# Tests for Video class objects
def VideoTests():
    print("Videos:")
    print()

    # Testing the proper implementation of a video object
    video1 = Video("Animation", "video-url")
    video1.print_details()

    print()

    # Testing a video object with no arguments passed
    video2 = Video()
    video2.print_details()


# Tests for ExternalLink class objects
def ExternalLinkTests():
    print("External Links:")
    print()

    # Testing the proper implementation of an external link object
    el1 = ExternalLink("Instagram", "ig", "embed-link")
    el1.print_details()

    print()

    # Testing an external link object with no arguments passed
    el2 = ExternalLink()
    el2.print_details()

# Tests for ImageFrontMatter class objects
def ImageFrontMatterTests():
    print("Image Front Matter:")
    print()

    # Testing the proper implementation of an image front matter object
    ifm1 = ImageFrontMatter("categories", "short-name", "title", "image", "alt")
    ifm1.print_details()

    print()

    # Testing an image front matter object with no arguments passed
    ifm2 = ImageFrontMatter()
    ifm2.print_details()

if __name__ == "__main__":
    main()