from django.shortcuts import render, redirect, get_object_or_404 
from .models import Items,  Contact , Category , CartItem
from .forms import ContactForm, NewsletterSubscriptionForm
from django.contrib import messages
import logging
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseServerError
# Create your views here.
logger = logging.getLogger(__name__)

def Home(request):
    return render(request, 'index.html')


def About(request):
    return render(request, 'about.html')


def Service(request):
    return render(request, 'services.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contactSuccess/')  # Redirect to a success page
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def Portfolio(request):
    try:
        categories = Category.objects.all()  # Fetch all categories
        items = Items.objects.all()  # Fetch all items
    except Exception as e:
        logger.error("Error in Portfolio view: %s", e)
        items = []
        categories = []
    return render(request, 'portfolio.html', {'categories': categories, 'items': items})


def Team(request):
    return render(request, 'team.html')


def TermsOfService(request):
    return render(request, 'TermsOfService.html')


def PrivacyPolicy(request):
    return render(request, 'PrivacyPolicy.html')


def ContactSuccess(request):
    return render(request, 'contactSuccess.html')


def PortfolioDetails(request, item_id):
    try:
        item = Items.objects.get(pk=item_id)
    except Items.DoesNotExist:
        logger.error("Item with ID %s does not exist.", item_id)
        return HttpResponseNotFound("Item not found.")
    except Exception as e:
        logger.error("Error in PortfolioDetails view: %s", e)
        return HttpResponseServerError("Internal server error.")
    return render(request, 'portfolio-details.html', {'item': item})


def subscribe_newsletter(request):
    try:
        if request.method == 'POST':
            form = NewsletterSubscriptionForm(request.POST)
            if form.is_valid():
                form.save()
                return JsonResponse({'success': True, 'message': 'Thank you for subscribing to our newsletter!'})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid email address. Please try again.'})
    except Exception as e:
        logger.error("Error in subscribe_newsletter view: %s", e)
        return JsonResponse({'success': False, 'message': 'An error occurred. Please try again later.'})
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def Design(request):
    return render(request, 'design.html')


def Marteting(request):
    return render(request, 'marketing.html')


def Ecommerce(request):
    return render(request, 'e-commerce.html')


def WebDevelop(request):
    return render(request, 'web-develop.html')


def SoftDevelop(request):
    return render(request, 'software-development.html')


def AppDevelop(request):
    return render(request, 'app-development.html')