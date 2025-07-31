# ☕ Zoon Cafe

**Zoon Cafe** is a dynamic web application built using the **Django** framework. It features a modern cafe website where users can browse the menu, make reservations, and interact with a stylish, responsive UI. The backend is powered by Django’s ORM and admin panel for easy content management.

---

## 🚀 Features

- Responsive frontend using HTML, CSS, JavaScript
- Menu display pulled dynamically from the database
- Table reservation form with backend storage
- Contact form with email/database integration
- Secure Django admin panel for content management
- URL routing, views, templates, and models

---

## 🛠 Technologies Used

- **Python 3.x**
- **Django 3.x / 4.x**
- **SQLite** (default) or MySQL/PostgreSQL (optional)
- **HTML5, CSS3, JavaScript**
- **Bootstrap** for responsive design
- Django’s built-in **admin panel**

---

## 💾 Database Models

Zoon Cafe uses Django models to store:

- Menu items (name, category, price, image, etc.)
- Table reservations (name, phone, date/time, etc.)
- Contact messages
- Admin-managed data (staff, events, specials)

---

## 📁 Project Structure

zoon_cafe/
├── cafe/ # Main Django app
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ └── static/
├── zoon_cafe/ # Project config directory
│ ├── settings.py
│ ├── urls.py
├── db.sqlite3
├── manage.py
├── README.md

yaml
Copy
Edit
