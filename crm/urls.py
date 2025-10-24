from django.contrib import admin
from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),
]

# # 개발 환경에서 static 파일 서빙
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
