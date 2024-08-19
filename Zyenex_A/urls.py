from django.contrib import admin
from django.urls import path
from . import views
 



urlpatterns = [
    path("", views.Home, name="Home"),
    path("about/", views.About, name="about"),
    path("services/", views.Service, name="services"),
    path("contact/", views.contact, name="contact"),
    path("portfolio/", views.Portfolio, name="portfolio"),
    path("team/", views.Team, name="team"),
    path("termsofservice/", views.TermsOfService, name="TermsOfService"),
    path("privacypolicy/", views.PrivacyPolicy, name="privacypolicy"),
    path("contact/contactSuccess/", views.ContactSuccess, name="contactSuccess"),
    path("portfoliodetails/<int:item_id>/", views.PortfolioDetails, name="portfoliodetails"),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),    
    
    path("design/", views.Design, name="design"),
    path("design/about/", views.About, name="design-about"),
    path("services/design/", views.Design, name="design-services"),
    
    path("marketing/", views.Marteting, name="marketing"),
    path("marketing/about/", views.About, name="marketing-about"),
    path("services/marketing/", views.Marteting, name="design-services"),
    
    path("ecommerce/", views.Ecommerce, name="ecommerce"),
    path("ecommerce/about/", views.About, name="ecommerce-about"),
    path("services/ecommerce/", views.Ecommerce, name="design-services"),
    
    path("web/", views.WebDevelop, name="web"),
    path("web/about/", views.About, name="web-about"),
    path("services/web/", views.WebDevelop, name="design-services"),
    
    path("software/", views.SoftDevelop, name="software"),
    path("software/about/", views.About, name="software-about"),
    path("services/software/", views.SoftDevelop, name="design-services"),
    
    path("app/", views.AppDevelop, name="app"),
    path("app/about/", views.About, name="app-about"),
    path("services/app/", views.AppDevelop, name="design-services"),
]
