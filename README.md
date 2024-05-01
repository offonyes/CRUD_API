# Djagno REST API
## Description
This is a simple Django REST API that allows users to create, read, update and delete Products and Category.


## Endpoints:
### Products:
- /products/ - GET
- /products/create/ - POST (Only admin user)
- /products/:id/ - GET
- /products/:id/update/ - PATCH (Only admin user)
- /products/:id/delete/ - DELETE (Only admin user)
### Category:
- /categories/ - GET
- /categories/ - POST (Only admin user)
- /categories/:id/ - GET 
- /categories/:id/update/ - PATCH (Only admin user)
- /categories/:id/delete/ - DELETE (Only admin user)

## Prerequisites

- Python 3.12
- Django
- Djange REST Framework

## Installation

1. Clone or download the project repository.
2. Install the required dependencies using the provided requirements.txt file:

```py
pip install -r requirements.txt
```
3. After installing the dependencies, run the server to start.
```py
python manage.py runserver
```