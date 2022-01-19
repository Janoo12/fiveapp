from django.shortcuts import render
from codingsession.models import CodingSession
from django.utils import timezone
from django.utils.timezone import utc

# Create your views here.

def codingsessionspage(request):
    coding_sessions = CodingSession.objects.filter(starting_time__gte=timezone.now())
    return render(request, template_name="codingsession/all.html",
                  context={'coding_sessions' : coding_sessions}
                  )
