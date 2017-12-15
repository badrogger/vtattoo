from tattoo.models import Tattoo
from django.contrib.auth.models import User
from django.core.files import File
import os


def save_img(idx):
    admin_user = User.objects.all()[0]
    img_name = "index_{}".format(idx)
    st_path =  os.path.join("tattooimg", img_name + ".jpg")
    img_path = os.path.join("media", img_name + ".jpg")
    ti = Tattoo(owner=admin_user, name=img_name)
    with open(img_path, "rb") as im_file:
        ti.image_file.save(st_path, File(im_file), save=True)
    ti.save()


def main():
    for i in range(6):
        save_img(i + 1)

