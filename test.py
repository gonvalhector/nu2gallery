from classes import Image

# Testing the proper use of an image object and inheritance of the ImageFile class
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