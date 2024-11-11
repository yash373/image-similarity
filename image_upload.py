from imgurpython import ImgurClient

def upload_image(path:str) -> None:
    client = ImgurClient(client_id="cb30ede881b8f55",client_secret="7b67ef91de5555e1ce8929f13cac909b8e1dfaf6")
    # Upload the image
    uploaded_image = client.upload_from_path(path, anon=True)
    # Return the URL of the uploaded image
    return uploaded_image['link']

# Test
# upload_image("images.jpeg")