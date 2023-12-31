"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import nearHundred, stringSplosion, catDog, loneSum
urlpatterns = [
    path('warmup-1/near-hundred/<int:n>', nearHundred),
    path('warmup-2/string-splosion/<string>', stringSplosion),
    path('string-2/cat-dog/<string>', catDog),
    path('logic-2/lone-sum/<int:n1>/<int:n2>/<int:n3>', loneSum),
    path('admin/', admin.site.urls),
]