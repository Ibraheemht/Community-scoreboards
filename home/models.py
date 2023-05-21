from django.db import models
import uuid

class sbentry(models.Model):
    name = models.CharField(max_length=200)
    link = models.TextField(null=False, blank=False)
    featured_image = models.ImageField(upload_to='static/submitted', null=True, blank=True)
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " " + str(self.submit_date)

    class Meta:
        verbose_name_plural = "Scoreboard entries"
        ordering = ['-submit_date']