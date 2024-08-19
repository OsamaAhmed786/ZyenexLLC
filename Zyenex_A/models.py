from django.db import models

# Create your models here.



class Category(models.Model):
    Ca_id = models.AutoField(primary_key=True, auto_created=True, default=None) 
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"ID-{self.Ca_id} ------------ CATEGORY-{self.name}"  

class Items(models.Model):
    I_id = models.AutoField(primary_key=True, auto_created=True, default=None) 
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static\\DB_upload', null=True, blank=True)
    video = models.FileField(upload_to='static\\DB_upload\\videos', null=True, blank=True)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ID-{self.I_id} ------------  TITLE-{self.title} ----------- CATEGORY-{self.category}"  

class Contact(models.Model):
    Co_id = models.AutoField(primary_key=True, auto_created=True, default=None) 
    name = models.CharField(max_length=100, verbose_name='Name')
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=200, verbose_name='Subject')
    message = models.TextField(verbose_name='Message')
    date_sent = models.DateTimeField(auto_now_add=True, verbose_name='Date Sent')

    def __str__(self):
        return f"ID-{self.Co_id} -------- NAME-{self.name}"



class CartItem(models.Model):
    Order_ID = models.AutoField(primary_key=True, auto_created=True, default=None) 
    portfolio_item = models.ForeignKey(Items, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    
class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email