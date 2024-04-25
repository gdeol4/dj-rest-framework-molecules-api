from django.urls import path
from . import views

urlpatterns = [
    # in the url below, the first arg is the url pattern that is routed too
    # the next arg specifies the view - which needs to also call ".as_view()"
    # the last arg
    path("molecules/", views.MoleculesListCreate.as_view(), name = "molecule-view-create"),
    path("molecules/<int:pk>/", views.MoleculesListRetrieveUpdateDestroy.as_view(), name="update"),
    ]