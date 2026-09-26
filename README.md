# 📚 Books — Django Project

**Books** — Django framework yordamida yaratilgan kitoblar bilan ishlashga mo‘ljallangan web loyiha.

## 🚀 Features

* 📖 Kitoblar ro‘yxatini ko‘rish
* 🔍 Kitoblarni qidirish
* ➕ Yangi kitob qo‘shish
* ✏️ Kitob ma’lumotlarini tahrirlash
* 🗑️ Kitoblarni o‘chirish
* 👤 Foydalanuvchilar bilan ishlash
* 🗄️ Database orqali ma’lumotlarni saqlash

## 🛠️ Technologies

* **Python**
* **Django**
* **SQLite / PostgreSQL**
* **HTML**
* **CSS**
* **Django Templates**

## 📁 Project Structure

```text
Books/
├── manage.py
├── db.sqlite3
├── books/
│   ├── migrations/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
└── Books/
    ├── settings.py
    ├── urls.py
    ├── asgi.py
    └── wsgi.py
```

## ⚙️ Installation

### 1. Repository'ni clone qilish

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd Books
```

### 2. Virtual environment yaratish

Windows:

```bash
python -m venv .venv
```

Linux / macOS:

```bash
python3 -m venv .venv
```

### 3. Virtual environment'ni ishga tushirish

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### 4. Kerakli paketlarni o‘rnatish

```bash
pip install -r requirements.txt
```

### 5. Migrationlarni bajarish

```bash
python manage.py migrate
```

### 6. Serverni ishga tushirish

```bash
python manage.py runserver
```

Loyiha quyidagi manzilda ishlaydi:

```text
http://127.0.0.1:8000/
```

## 👨‍💻 Author

**YaxyoHub**

Python / Django Developer

---

⭐ Agar loyiha foydali bo‘lsa, repository'ga star bosishni unutmang!
