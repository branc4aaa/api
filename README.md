# API (Django Backend)

Este es un backend en Django para manejar Posts, usuarios y carga de imágenes. Es parte de mi portfolio como desarrolladora backend.

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
├── api/ # carpeta de configuración principal
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── appi/ # tu app principal
│ ├── migrations/
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ └── templates/
│ ├── index.html
│ └── posts.html
├── static/ # archivos estáticos (CSS, JS)
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
   python manage.py makemigrations
   python manage.py migrate
   python manage.py runserver o python3 manage.py runserver


