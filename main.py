from similarity import similarity
from image_upload import upload_image

# Test

image1 = upload_image("IMG_20241110_000015_007.jpg")

image2 = upload_image("IMG_20241110_033148.jpg")

print(similarity(image1, image2))