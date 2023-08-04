from django.urls import path
from .views import *
urlpatterns=[
    path('',home,name='home'),
    path('add/',create_view,name='add'),
    path('list/',viewss,name='all'),
    path('<id>/delete/',delete_view,name='delete'),
    path('<id>/update/',update_view,name='update'),
    path("add/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("remove/<int:cart_item_id>/", remove_from_cart, name="remove_from_cart"),
    path("cart/", cart_detail, name="cart_detail"),
    path('product/<int:product_id>/', product_detail, name='product_detail'),

]