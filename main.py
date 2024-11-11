from similarity import similarity
from image_upload import upload_image

# Test

image1 = "https://t1.gstatic.com/licensed-image?q=tbn:ANd9GcQsu7yYuRPXNK9eHHSFD2tUYO4stQDb1Ez8vjqGERfs9xqYLLnY_y6lQkPFZa-44cqn"

image2 = "https://media.npr.org/assets/img/2012/02/02/mona-lisa-copy_custom-876888c0699fe7bd9ad55f7c974e59115683995e.jpg"

print(similarity(image1, image2))