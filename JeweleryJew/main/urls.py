from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('urgent_repairs', urgent_repairs, name='urgent_repairs'),
    path('d_dev', d_dev, name='d_dev'),
    path('exchange_fund', exchange_fund, name='exchange_fund'),
    path('restoration', restoration, name='restoration'),
    path('<slug:category_slug>', show_category),
]
