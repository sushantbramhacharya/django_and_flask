from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home,name="home"),
    # path('products/',views.products,name="products"),

    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polts/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
