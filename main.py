from similarity import similarity
from image_upload import upload_image
from rating import rating

# Test

# print(upload_image("baku.jpg"))

image1 = upload_image("IMG_20241110_000015_007.jpg")

print(rating(image1))