# 🧠 CRM_APP – Customer Relationship Management System

**CRM_APP** (also called DCRM) is a web-based Customer Relationship Management system built using Django. It demonstrates key full-stack web development practices and addresses real-world business needs through customer and lead management tools.

---

## 📌 Key Features

- ✅ Complete CRUD operations for customer and lead management
- 🔐 Secure user authentication and role-based authorization
- 🖥️ Responsive user interface using Bootstrap
- 🧠 Clean and modular Django architecture with efficient ORM usage
- 🧪 Built-in testing suite for core functionalities
- ⚙️ Form validation and error handling
- 🗃️ Django ORM for structured and performant database operations

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (via Django ORM)
- **Authentication**: Django’s built-in security framework

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/SouhailBourhim/CRM_APP.git
cd CRM_APP
```

### Create a virtual environment and install dependencies

```bash
python3 -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
pip install -r requirements.txt
```

### Apply migrations and create a superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### Run the development server

```bash
python manage.py runserver
```

Then open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 🗃️ Project Structure

```
CRM_APP/
├── agents/           # Agent-specific views and forms
├── leads/            # Lead management logic
├── landing/          # Static landing and contact pages
├── crm_project/      # Main project settings and URLs
├── templates/        # HTML templates
├── static/           # Static files (CSS, JS)
├── requirements.txt  # Dependencies
└── manage.py
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Souhail Bourhim**  
🔗 [LinkedIn](https://www.linkedin.com/in/souhail-bourhim-67b878307/)  
🌐 [Portfolio](https://portfolio-git-main-souhails-projects-dfdb3e43.vercel.app)

---

## ⭐ Support

If you find this project helpful, consider starring it on [GitHub](https://github.com/SouhailBourhim/CRM_APP).
