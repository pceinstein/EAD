from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def course_chat_room(request, course_id):
    try:
        # obtém o curso cujo id foi especificado
        # e no qual o usuário se inscreveu
        course = request.user.courses_joined.get(id=course_id)
    except:
        # o usuário não é um aluno do curso ou o curso não existe
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'course': course})
