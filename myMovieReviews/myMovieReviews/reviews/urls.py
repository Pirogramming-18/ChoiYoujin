from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    #url과 view를 연결
    path('', view = views.post_list, name = 'list'),
    # pk를 index로 post 가지고 옴 posts/1 -> pk:1
    path('<int:pk>/', view = views.post_detail, name='detail'),
    # create로 가면 create가 실행이 되는 view
    path('create/', view = views.post_create, name='create'),
    # update
    path('<int:pk>/update', view=views.post_update, name='update'),
    # delete
    path('<int:pk>/delete', view = views.post_delete, name = 'delete')
]