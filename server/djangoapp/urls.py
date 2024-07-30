# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore
from . import views

app_name = 'djangoapp'
urlpatterns = [
    # # path for registration
     #path('registration/', views.registration_request, name='registration'),
    # path for login
     path(route='login', view=views.login_user, name='login'),
     #path('login/', TemplateView.as_view(template_name="index.html")), # type: ignore
    
    # path for dealer reviews view
     #path('logout/', views.logout_request, name='logout'),
    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
