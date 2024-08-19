from django.contrib import admin

# Register your models here.
from .models import Category, Items, Contact, CartItem, NewsletterSubscription

admin.site.register(Category)
admin.site.register(Items)
admin.site.register(Contact)
admin.site.register(NewsletterSubscription)

admin.display("zyenexadmin")