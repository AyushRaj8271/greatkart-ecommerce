from django.urls import path
from . import views
urlpatterns =[
    path('',views.store,name='store'), #as after sotre there will be nothing that is why we are keep it blank
    path('<slug:category_slug>/', views.store, name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),

    
]