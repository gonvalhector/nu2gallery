from classes import Image, Thumbnail

# Testing the proper implementation of an image object and inheritance of the ImageFile class
image1 = Image("Final Version", "Designed with 60fps in mind.", "full-link", "gif-link", "png-link", "jpg-link")
print("Label: ", image1.get_label())
print("Caption: ", image1.get_caption())
print("Full link: ", image1.get_link_full())
print("GIF link: ", image1.get_link_gif())
print("PNG link: ", image1.get_link_png())
print("JPG link: ", image1.get_link_jpg())

print()

# Testing an image object with no arguments passed
image2 = Image()
print("Label: ", image2.get_label())
print("Caption: ", image2.get_caption())
print("Full link: ", image2.get_link_full())
print("GIF link: ", image2.get_link_gif())
print("PNG link: ", image2.get_link_png())
print("JPG link: ", image2.get_link_jpg())

# Testing the proper implementation of a thumbnail object and inheritance of the ImageFile class
thumb1 = Thumbnail("gif-link", "png-link", "jpg-link")
print("GIF link: ", thumb1.get_link_gif())
print("PNG link: ", thumb1.get_link_png())
print("JPG link: ", thumb1.get_link_jpg())

# Testing a thumbnail object with no arguments passed
thumb2 = Thumbnail()
print("GIF link: ", thumb2.get_link_gif())
print("PNG link: ", thumb2.get_link_png())
print("JPG link: ", thumb2.get_link_jpg())