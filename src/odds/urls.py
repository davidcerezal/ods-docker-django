from django.urls import path, re_path
from . import views


urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.

    path('surebet/<int:surebet_id>', views.sureBetDetail, name='surebet_detail')
]
