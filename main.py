from similarity import similarity
from image_upload import upload_image

# Test

image1 = upload_image("img1.jpg")

image2 = upload_image("img2.jpg")

print((similarity(image1, image2)/10000)*100)