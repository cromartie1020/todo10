from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views
from user import views
from django.conf import settings
from django.conf.urls.static import static
#from image_app.views import success, hotel_image_view
from todo import views as todo_view

urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('user/',include('user.urls')),
    path('envelope/',include('envelope.urls')),
    #path('success/', success, name = 'success'), 
    #path('image_upload/', hotel_image_view, name = 'image_upload'), 
    path('',todo_view.todo,name='todo'),
    path('newtodo/',todo_view.todo_form,name='newtodo'),
    path('deletetodo/<int:pk>/',todo_view.todo_delete,name='deletetodo'),
    path('updatetodo/<int:pk>/',todo_view.todo_update,name='updatetodo'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)