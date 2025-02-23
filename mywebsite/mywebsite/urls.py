from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', include('accounts.urls')),  
    path('blog/', include('blog.urls')),          
    path('forum/', include('forum.urls')),        
    path('marketplace/', include('marketplace.urls')),  
    path('admin/', admin.site.urls),
]



