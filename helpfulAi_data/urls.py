from django.urls import path
from .views import mess
from .views import index
from .views import peopleLog
from .views import peopleCreate
from .views import getPerson
from .views import logOut
urlpatterns = [
    path('', index, name="client"),
    path('mess/', mess, name="data"),
    path('login/', peopleLog, name="login"),
    path('create/', peopleCreate, name="create"),
    path('getUse/', getPerson, name="getUser"),
    path('logOut/', logOut, name="logOutUser"),
]