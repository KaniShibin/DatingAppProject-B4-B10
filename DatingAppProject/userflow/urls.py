from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'userflow'
urlpatterns = [
    path('settings/',views.SettingsView.as_view(),name="SettingsView"),
    path('privacy-settings/',views.PrivacySettingsView.as_view(),name="PrivacySettingsView"),
    path('filter/',views.FilterView.as_view(),name="FilterView"),
    path('preference/',views.PreferenceView.as_view(),name="PreferenceView"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)