from django.db import models

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel/', blank=False, null=False )

    class Meta:
        verbose_name = "Fotot e para"
        

    def __str__(self):
        return f"Slide {self.id}"

class Video(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    

    def __str__(self):
        # Ensure that the __str__ method returns a string
        return self.title if self.title else 'Untitled Video'