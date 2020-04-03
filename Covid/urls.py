from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    
    path("", views.Landing,name="Landing"),
    path("Checkup", views.index,name="home"),
    path('Process', views.process,name="process"),
    path('Analysis',views.Analysis,name="Analysis"),
    path('Search',views.Search,name="Search"),
    path('Find',views.Find,name="Find"),
    path('FindLocation',views.FindLocation,name="FindLocation"),
    path('InsertPositionLogin',views.InsertPositionLogin,name="InsertPositionLogin"),
    path('LoginPositionValidation',views.LoginPositionValidation,name="LoginPositionValidation"),
    path('SubmissionInsertPosition',views.SubmissionInsertPosition,name="SubmissionInsertPosition"),
 	path('LoginSimtermsValidation',views.LoginSimtermsValidation,name="LoginSimtermsValidation"),
 	path('InsertSimtermLogin',views.InsertSimtermLogin ,name="InsertSimtermLogin"),
 	path('SubmissionInsertSimterms',views.SubmissionInsertSimterms ,name="SubmissionInsertSimterms"),
    path('AboutProject',views.AboutProject,name="AboutProject"),
    path('ContactUs',views.ContactUs,name="ContactUs"),


   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
