from django.contrib import admin
from django.urls import path

from django.conf.urls import include

urlpatterns = [
    path(r"^admin/", admin.site.urls),
    path(r"^api/", include("backend.company.urls")),
    path(r"^api/employee/", include("backend.employee.urls")),
    path(r"^api/user/", include("backend.user.urls")),
]
