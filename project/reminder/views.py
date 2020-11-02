from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from reminder.models import Reminder

def manage(request):
    user_id = None
    if request.user.is_authenticated:
        user_id = request.user.id
    else:
        return HttpResponseRedirect("/admin/login/")
    reminders = Reminder.objects.filter(user_id=user_id)
    return render(request, 'manage.html', {'reminders':reminders})

def del_reminder(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect("/admin/login/")
    try:
        reminder_id = int(request.GET.get('id', ''))
        p = Reminder.objects.get(id=int(reminder_id))
        p.delete()
    except:
        pass
    return HttpResponseRedirect("/")
