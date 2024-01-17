from django.urls import path,include
from .apis import (dropDown,derivatives)

urlpatterns = [
    path('dropDown',dropDown.dropDownApi.as_view()),
    path('derivatives',derivatives.derivativesApi.as_view())
]
