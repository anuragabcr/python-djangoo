from django.db import models
from PIL import Image, ImageOps


# Create your models here.
class Images(models.Model):
    img1 = models.ImageField(upload_to='images/')
    img2 = models.ImageField(upload_to='images/')
    img3 = models.ImageField(upload_to='images/')
    img4 = models.ImageField(upload_to='images/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # saving image first

        img = Image.open(self.img1.path)  # Open image using self
        img.thumbnail((200, 300))
        img.save(self.img1.path)

        img = Image.open(self.img2.path)
        img.thumbnail((500, 500))
        img.save(self.img2.path)

        img = Image.open(self.img3.path)
        img.thumbnail((1024, 768))
        img.save(self.img3.path)

        img = Image.open(self.img4.path)
        img = ImageOps.grayscale(img)
        img.save(self.img4.path)
