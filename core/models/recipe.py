from django.db import models




class Recipe(models.Model):
    title=models.CharField(max_length=500)
    owner=models.ForeignKey('User',on_delete=models.CASCADE,blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    is_public=models.BooleanField(default=False,blank=True)
    ingredients=models.JSONField(blank=True,default=list)
    steps=models.JSONField(blank=True,default=list)
    image=models.ImageField(upload_to='images/',blank=True,null=True)


    def __str__(self):
        return self.title





