from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Course

def subdomain_course_middleware(get_response):
    """
    Subdomínios para os cursos
    """
    def middleware(request):
        host_parts = request.get_host().split('.')
        if len(host_parts) > 2 and host_parts[0] != 'www':
            # obtém o curso para o dado subdomínio
            course = get_object_or_404(Course, slug=host_parts[0])
            course_url = reverse('course_detail',
                                 args=[course.slug])
            # redireciona a requisição atual para a view course_detail
            url = '{}://{}{}'.format(request.scheme,
                                     '.'.join(host_parts[1:]),
                                     course_url)
            return redirect(url)
        
        response = get_response(request)
        return response
    
    return middleware