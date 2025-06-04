# from django.urls import  path
# from .views import analytics

# urlpatterns = [
#     path("analytics", analytics),
# ]

from django.urls import path, include
from .views import analytics, graph

analytics_patterns = [
    path('', analytics, name='analytics'),
    path('graph/', graph, name='analytics-graph'),
]

urlpatterns = [
    path('analytics/', include((analytics_patterns, 'analytics'))),
]
