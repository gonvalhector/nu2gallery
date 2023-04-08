from classes import Image, Thumbnail, Video, ExternalLink

# Testing the proper implementation of an image object and inheritance of the ImageFile class
print("Images:")
print()

image1 = Image("Final Version", "Designed with 60fps in mind.", "full-link", "gif-link", "png-link", "jpg-link")
image1.print_details()

print()

# Testing an image object with no arguments passed
image2 = Image()
image2.print_details()

print()

# Testing the proper implementation of a thumbnail object and inheritance of the ImageFile class
print("Thumbnails:")
print()

thumb1 = Thumbnail("gif-link", "png-link", "jpg-link")
thumb1.print_details()

print()

# Testing a thumbnail object with no arguments passed
thumb2 = Thumbnail()
thumb2.print_details()

print()

# Testing the proper implementation of a video object
print("Videos:")
print()

video1 = Video("Animation", "video-url")
video1.print_details()

print()

# Testing a video object with no arguments passed
video2 = Video()
video2.print_details()

print()

# Testing the proper implementation of an external link object
print("External Links:")
print()

el1 = ExternalLink("Instagram", "ig", "embed-link")
el1.print_details()

print()

# Testing an external link object with no arguments passed
el2 = ExternalLink()
el2.print_details()

print()