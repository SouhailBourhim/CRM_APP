# 🧠 CRM_APP – Customer Relationship Management System

Welcome to **CRM_APP**, a simple yet powerful Django-based CRM solution to manage clients, deals, and company sales processes effectively.

---

## 📌 Features

- 🔐 **User Authentication** – Register, login, logout.
- 🏢 **Organizations** – Each user belongs to an organization for better data separation.
- 🧍‍♂️ **Leads Management** – Create, update, assign, and categorize leads.
- ✅ **Agent Assignment** – Admins can assign leads to agents in their organization.
- 📊 **Dashboards** – Custom views for agents and organizers.
- ✉️ **Contact Form** – Built-in contact page for communication.
- 🌐 Fully responsive UI with Django templates.

---

## 🛠️ Tech Stack

- **Backend**: Django 4+
- **Frontend**: HTML, Bootstrap (via templates)
- **Database**: SQLite (default; easily switchable)
- **Forms**: Django Forms & ModelForms
- **Emailing**: Django’s email backend

---

## 🚀 Getting Started

### 🔄 Clone the repository

```bash
git clone https://github.com/SouhailBourhim/CRM_APP.git
cd CRM_APP
```

### 📦 Install dependencies

It is recommended to use a virtual environment.

```bash
python3 -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

### ⚙️ Configure settings

In `crm_project/settings.py`, set up your:

- Secret key 🔑
- Email backend 💌
- Debug mode (for development)

---

### 🧪 Run migrations and create a superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 🧯 Run the development server

```bash
python manage.py runserver
```

Access it at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Testing

Use Django’s built-in test framework:

```bash
python manage.py test
```

---

## 🗃️ Folder Structure

```
CRM_APP/
│
├── leads/             # Core CRM app logic
├── agents/            # Agent-specific views & management
├── landing/           # Landing page & contact form
├── crm_project/       # Main project settings
├── templates/         # HTML templates
├── static/            # Static files
├── db.sqlite3         # Default database
├── requirements.txt   # Python packages
└── manage.py
```

---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the project and submit PRs. For major changes, open an issue first to discuss your ideas.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Souhail Bourhim**  
📬 [LinkedIn](https://www.linkedin.com/in/souhailbourhim)  
💻 [Portfolio](https://souhailbourhim.github.io/Projet_dev_init.io/)  
📫 Contact: via contact form in the app

---

## 🌟 Show your support

If you like this project, consider giving it a ⭐ on [GitHub](https://github.com/SouhailBourhim/CRM_APP)!
