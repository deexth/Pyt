from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    

    class Meta:
        verbose_name = _("BlogPost")
        verbose_name_plural = _("BlogPosts")

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("BlogPost_detail", kwargs={"pk": self.pk})
