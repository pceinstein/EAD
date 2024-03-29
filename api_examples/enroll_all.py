import requests

# substitua os valores das variáveis pelas credenciais de um usuário existente
username = ''
password = ''

base_url = 'http://127.0.0.1:8000/api/'

# obtém todos os cursos
r = requests.get(f'{base_url}courses/')
courses = r.json()
available_courses = ', '.join([course['title'] for course in courses])
print(f'Available courses: {available_courses}')

for course in courses:
    course_id = course['id']
    course_title = course['title']
    r = requests.post(f'{base_url}courses/{course_id}/enroll/',
                      auth=(username,password))
    
    if r.status_code == 200:
        # requisição bem-sucedida
        print(f'Successfully enrolled in {course_title}')