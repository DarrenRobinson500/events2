from django.contrib import admin
from django.urls import path
from events import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', views.answer_list, name='answer_list'),

    path('tree_ask', views.tree_ask, name='tree_ask'),
    path('tree_event', views.tree_event, name='tree_event'),
    path('tree_not_event', views.tree_not_event, name='tree_not_event'),
    path('tree_list', views.tree_list, name='tree_list'),
    path('tree_upload', views.tree_upload, name='tree_upload'),
    path('tree_delete', views.tree_delete, name='tree_delete'),
    path('tree_new', views.tree_new, name='tree_new'),
    path('tree_update/<tree_id>', views.tree_update, name='tree_update'),
    path('tree_delete_one/<tree_id>', views.tree_delete_one, name='tree_delete_one'),
    path('tree_ind/<tree_id>', views.tree_ind, name='tree_ind'),

    path('answer_list', views.answer_list, name='answer_list'),
    path('answer_upload', views.answer_upload, name='answer_upload'),
    path('answer_delete', views.answer_delete, name='answer_delete'),
    path('answer_delete_one/<answer_id>', views.answer_delete_one, name='answer_delete_one'),
    path('answer_new', views.answer_new, name='answer_new'),
    path('logic_tree_update/<answer_id>', views.logic_tree_update, name='logic_tree_update'),
    path('answer_update/<answer_id>', views.answer_update, name='answer_update'),
    path('answer_send_email/<answer_id>', views.answer_send_email, name='answer_send_email'),
    path('answer_send_emails', views.answer_send_emails, name='answer_send_emails'),
    path('answer_status_update/<answer_id>', views.answer_status_update, name='answer_status_update'),
    path('answer_ind/<answer_id>', views.answer_ind, name='answer_ind'),
    path('answer_print/<answer_id>', views.answer_print, name='answer_print'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)