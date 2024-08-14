from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from time import localtime
from django.utils.timezone import localtime  # noqa: F811
from .models import get_duration, format_duration
import locale


def storage_information_view(request):
    visits_without_leave = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = []
    for visit in visits_without_leave:
        duration = get_duration(visit)
        duration_str = format_duration(duration)
        non_closed_visit = {
            "who_entered": visit.passcard,
            "entered_at": localtime(visit.entered_at).strftime("%d %B %Y г. %H:%M"),
            "duration": duration_str,
        }
        non_closed_visits.append(non_closed_visit)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
