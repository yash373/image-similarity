from similarity import similarity
from image_upload import upload_image
from rating import rating

# Test

image1 = upload_image("img2.jpg")
image2 = upload_image("img2.jpg")

print(image1, image2)

print(similarity(image1,image2))