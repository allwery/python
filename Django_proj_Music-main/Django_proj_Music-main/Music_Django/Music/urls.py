from django.urls import path

from . views import(
    concert_detail, concert_home, concert_list, buying_create, buyer_create, buyer_list, buyer_update, buyer_detail
)

app_name = 'Music'

urlpatterns = [
    path("", concert_list),
    path('buyer_list/', buyer_list),
    path("home/", concert_home),
    path("detail/<int:id>/", concert_detail, name='detail'),
    path("details/<int:id>/", buyer_detail, name='details'),
    path("<int:id>/", concert_detail, name='detail'),
    path("<int:id>/update/", buyer_update, name='update'),
    path("buying/", buying_create),
    #path("<int:id>/delete/", buyer_delete, name='delete'),
]