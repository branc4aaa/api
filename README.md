# API (Django Backend)

Este es un backend en Django para manejar Posts, usuarios y carga de imágenes. Es parte de mi portfolio como desarrollador backend.

---

## Tecnologías usadas

- Python 3.11  
- Django 5.x  
- SQLite (o PostgreSQL, ver configuración)  
- Django Forms para subida de imágenes  
- Autenticación con usuarios de Django  
- `MEDIA_ROOT` para almacenar imágenes

---

##  Estructura del proyecto

api/
├── manage.py
├── api/ 
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── appi/ 
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ └── templates/
│ ├── index.html
│ └── posts.html
└── media/ # imágenes u otros archivos subidos

yaml
Copiar código

---

## Cómo instalar y correr

1. Cloná el repositorio:  
   ```bash
   git clone https://github.com/branc4aaa/api.git
   cd api
   python -m venv venv o python3 -m venv venv
   source venv/bin/activate  # o venv\Scripts\activate en Windows
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver o python3 manage.py runserver

## Endpoints

http://localhost:8000/index

http://localhost:8000/index/singup/

http://localhost:8000/index/login/

http://localhost:8000/index/posts/

http://localhost:8000/index/addpost/

http://localhost:8000/index/logout/
