from django.shortcuts import render, get_object_or_404
from .models import Topic

def topic_list_view(request):
    topics = Topic.objects.all()
    return render(request, 'forum/topic_list.html', {'topics': topics})

def topic_detail_view(request, pk):
    topic = get_object_or_404(Topic, pk=pk)
    return render(request, 'forum/topic_detail.html', {'topic': topic})
