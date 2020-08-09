from django.db import models

# Create your models here.


property_type = (
    ('sale' , "sale"),
    ('rent' , "rent")
)
class Employee(models.Model):

    name = models.CharField(max_length=50, default=None)
    property_type = models.CharField(choices=property_type , max_length=10)
    price = models.PositiveIntegerField()
    category = models.ForeignKey('Category2' ,null=True ,on_delete=models.SET_NULL)
    area = models.DecimalField(decimal_places=2 ,max_digits=8 )
    beds_number = models.PositiveIntegerField()
    baths_number = models.PositiveIntegerField()
    garages_number = models.PositiveIntegerField()
    image = models.ImageField(upload_to='property2/', null=True, verbose_name="" )
    location = models.CharField(max_length=50 , null=True)
    user_desc = models.CharField(max_length=100, default='')


    def __str__(self):
        return self.name


    class Meta:
        db_table = "employee"  


class Category2(models.Model):
    category_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='category2/' , null=True)


    def __str__(self):
        return self.category_name