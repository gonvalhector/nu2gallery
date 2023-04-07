from classes import Image, Thumbnail

# Testing the proper implementation of an image object and inheritance of the ImageFile class
image1 = Image("Final Version", "Designed with 60fps in mind.", "full-link", "gif-link", "png-link", "jpg-link")
image1.print_details()

print()

# Testing an image object with no arguments passed
image2 = Image()
image2.print_details()

print()

# Testing the proper implementation of a thumbnail object and inheritance of the ImageFile class
thumb1 = Thumbnail("gif-link", "png-link", "jpg-link")
thumb1.print_details()

print()

# Testing a thumbnail object with no arguments passed
thumb2 = Thumbnail()
thumb2.print_details()