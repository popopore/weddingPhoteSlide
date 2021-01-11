import cloudinary
import cloudinary.uploader
from cloudinary.uploader import upload
import cloudinary.api
from cloudinary.utils import cloudinary_url
from flask import Flask

cloudinary.config(
    cloud_name = "yu1991ta",
    api_key = "648747536824239",
    api_secret = "F_PpehZ1SXIZKIYTZMynMHTENzw"
)

res = cloudinary.api.resources(type="upload",prefix = "01.WeddingPhoteSlide")
for img in res["resources"]:
    print(img["secure_url"])

    