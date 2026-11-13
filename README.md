# Ex.05 Book Cover Page Design

## Date: 13-11-2026
## Name: V Kamalesh Kannan
## Register Number: 26011247
## Course Code: 19AI414
## Course Title: Fundamentals of Web Application Development
## Department: Computer Science Engineering
## Institution: Saveetha Engineering College (Autonomous)

---

## AIM:
To design a book back cover page using HTML and CSS.

---

## DESIGN STEPS:

- **Step 1:** Create a Django Admin project.
- **Step 2:** Create an app in the Django interface.
- **Step 3:** Create a folder named 'static' in the app folder.
- **Step 4:** Create a new HTML file in the static folder.
- **Step 5:** Write the HTML code with relevant CSS properties.
- **Step 6:** Choose the appropriate style and color scheme.
- **Step 7:** Insert the images in their appropriate places.
- **Step 8:** Publish the website in the LocalHost.

---

## PROGRAM:

### 1. `bookcover_project/settings.py`
```python
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-bookcover-ex05-19ai414-secret-key-development'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cover_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bookcover_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'cover_app' / 'templates', BASE_DIR / 'cover_app' / 'static'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bookcover_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'cover_app' / 'static',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
```

### 2. `bookcover_project/urls.py`
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cover_app.urls')),
]
```

### 3. `cover_app/views.py`
```python
from django.shortcuts import render

def book_cover(request):
    """
    Renders the Book Back Cover Page Design.
    Ex. 05 - Web Application Development
    Student: V Kamalesh Kannan (26011247)
    """
    context = {
        'title': 'Mastering Modern Web Development & AI',
        'subtitle': 'Architecting High-Performance, Scalable Web Applications',
        'author': 'V Kamalesh Kannan',
        'edition': 'Second Edition',
        'isbn': '978-93-89845-05-9',
        'price': '₹799 / $39.99 USD',
    }
    return render(request, 'bookcover.html', context)
```

### 4. `cover_app/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_cover, name='book_cover'),
    path('cover/', views.book_cover, name='book_cover_alias'),
]
```

### 5. `cover_app/static/bookcover.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Book Back Cover Page Design - V Kamalesh Kannan (26011247)</title>
    <link rel="stylesheet" href="css/style.css">
</head>
<body>

    <!-- Academic & Student Information Header -->
    <header class="academic-header">
        <h1>Saveetha Engineering College</h1>
        <h2>Department of Artificial Intelligence and Data Science</h2>
        <div class="student-meta">
            <span><strong>Course:</strong> 19AI414 - FWAD</span>
            <span><strong>Exercise:</strong> Ex.05 Book Cover Page Design</span>
            <span><strong>Name:</strong> V Kamalesh Kannan</span>
            <span><strong>Register No:</strong> 26011247</span>
        </div>
    </header>

    <!-- Book Back Cover Component -->
    <main class="book-wrapper">
        <article class="book-back-cover">
            
            <!-- Top Metadata -->
            <div class="cover-top-bar">
                <span class="genre-tag">Computer Science / Artificial Intelligence</span>
                <span class="edition-badge">Second Edition</span>
            </div>

            <!-- Book Title & Subtitle -->
            <section class="book-header">
                <h1 class="book-title">Mastering Modern Web Development & AI</h1>
                <p class="book-subtitle">Architecting High-Performance, Scalable Web Applications</p>
            </section>

            <!-- Book Synopsis / Blurb -->
            <section class="synopsis-section">
                <p class="synopsis-headline">"The essential roadmap from foundational web protocols to enterprise-grade AI integration."</p>
                <p class="synopsis-text">
                    In today's fast-paced digital ecosystem, creating dynamic web applications requires far more than basic markup. 
                    This definitive handbook bridges the gap between sophisticated frontend interfaces, robust Django backend architectures, 
                    and state-of-the-art machine learning models. Whether you are building responsive UI layouts with HTML5 and modern CSS 
                    or orchestrating distributed REST APIs, this book equips you with battle-tested patterns, clear diagrams, and real-world 
                    practical implementations.
                </p>
            </section>

            <!-- Key Features / Highlights -->
            <section class="highlights-card">
                <h2 class="highlights-title">⚡ What You Will Master Inside</h2>
                <ul class="highlights-list">
                    <li><span class="bullet">✔</span> Modern HTML5 Semantic Markup & CSS3 Grid/Flexbox</li>
                    <li><span class="bullet">✔</span> Django Framework: MVC/MVT Architecture & Routing</li>
                    <li><span class="bullet">✔</span> Responsive Web Design & Interactive Media Integration</li>
                    <li><span class="bullet">✔</span> Production Deployment, Microservices & Security Best Practices</li>
                </ul>
            </section>

            <!-- Critical Acclaim & Reviews -->
            <section class="reviews-grid">
                <div class="review-card">
                    <div class="star-rating">★★★★★</div>
                    <p class="review-quote">"An authoritative masterpiece that demystifies modern full-stack web engineering with precision and flair."</p>
                    <p class="review-author">— Tech Review Quarterly</p>
                </div>
                <div class="review-card">
                    <div class="star-rating">★★★★★</div>
                    <p class="review-quote">"Hands down the most comprehensive and practical guide for students and experienced engineers alike."</p>
                    <p class="review-author">— Dr. S. Raman, AI Research Lead</p>
                </div>
            </section>

            <!-- Author Spotlight -->
            <section class="author-box">
                <img src="images/author.svg" alt="Author V Kamalesh Kannan">
                <div class="author-details">
                    <h4>V Kamalesh Kannan</h4>
                    <span class="author-role">Author & Software Architect</span>
                    <p>Researcher and full-stack specialist specializing in Artificial Intelligence and Web Application Frameworks at Saveetha Engineering College.</p>
                </div>
            </section>

            <!-- Footer: Publisher, Price, and Barcode -->
            <footer class="cover-footer">
                <div class="publisher-info">
                    <img src="images/publisher_logo.svg" alt="Saveetha Academic Press Logo">
                    <span class="publisher-url">www.saveetha.ac.in/press</span>
                </div>
                <div class="barcode-area">
                    <span class="price-tag">PRICE: ₹799 / $39.99 USD</span>
                    <img src="images/barcode.svg" alt="ISBN 978-93-89845-05-9 Barcode">
                </div>
            </footer>

        </article>
    </main>

    <!-- Lab Page Footer -->
    <footer class="page-footer">
        <p>19AI414 - Fundamentals of Web Application Development | Ex.05 Book Cover Page Design | Saveetha Engineering College</p>
    </footer>

</body>
</html>
```

### 6. `cover_app/static/css/style.css`
```css
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Inter:wght@300;400;500;600;700&family=Playfair+Display:ital,wght@0,600;1,400;1,600&display=swap');

:root {
    --bg-page: #0f172a;
    --cover-bg-start: #0a0f1d;
    --cover-bg-end: #1e293b;
    --accent-gold: #f59e0b;
    --accent-cyan: #38bdf8;
    --text-primary: #f8fafc;
    --text-secondary: #cbd5e1;
    --text-muted: #94a3b8;
    --card-surface: rgba(255, 255, 255, 0.05);
    --card-border: rgba(255, 255, 255, 0.12);
    --spine-shadow: rgba(0, 0, 0, 0.55);
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background: radial-gradient(circle at top, #1e293b 0%, #0f172a 50%, #020617 100%);
    color: var(--text-primary);
    min-height: 100vh;
    padding: 30px 15px;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.academic-header {
    width: 100%;
    max-width: 820px;
    background: rgba(15, 23, 42, 0.85);
    backdrop-filter: blur(8px);
    border: 1px solid var(--card-border);
    border-radius: 12px;
    padding: 18px 24px;
    margin-bottom: 25px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.35);
    text-align: center;
}

.academic-header h1 {
    font-size: 20px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.academic-header h2 {
    font-size: 13px;
    font-weight: 500;
    color: var(--accent-gold);
    letter-spacing: 0.8px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.student-meta {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    gap: 10px;
    background: rgba(0, 0, 0, 0.25);
    padding: 10px 15px;
    border-radius: 8px;
    font-size: 13px;
    color: var(--text-secondary);
    border-left: 4px solid var(--accent-cyan);
}

.student-meta span strong {
    color: #ffffff;
}

.book-wrapper {
    perspective: 1200px;
    margin-bottom: 30px;
}

.book-back-cover {
    position: relative;
    width: 100%;
    max-width: 740px;
    background: linear-gradient(145deg, #090d16 0%, #111827 50%, #1e293b 100%);
    border-radius: 12px 18px 18px 12px;
    padding: 45px 50px 40px 65px;
    box-shadow: 
        -12px 0 25px var(--spine-shadow),
        0 25px 50px -12px rgba(0, 0, 0, 0.7),
        inset 0 0 0 1px rgba(255, 255, 255, 0.1);
    overflow: hidden;
}

.book-back-cover::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 28px;
    background: linear-gradient(to right,
        rgba(0, 0, 0, 0.7) 0%,
        rgba(255, 255, 255, 0.08) 35%,
        rgba(0, 0, 0, 0.5) 70%,
        rgba(0, 0, 0, 0.1) 100%
    );
    border-right: 1px solid rgba(255, 255, 255, 0.08);
}

.book-back-cover::after {
    content: '';
    position: absolute;
    top: 15px;
    right: 15px;
    bottom: 15px;
    left: 38px;
    border: 1px solid rgba(245, 158, 11, 0.18);
    border-radius: 6px;
    pointer-events: none;
}

.cover-top-bar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 22px;
    position: relative;
    z-index: 1;
}

.genre-tag {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2px;
    color: var(--accent-cyan);
    text-transform: uppercase;
    background: rgba(56, 189, 248, 0.1);
    padding: 5px 12px;
    border-radius: 20px;
    border: 1px solid rgba(56, 189, 248, 0.25);
}

.edition-badge {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 1.5px;
    color: var(--accent-gold);
    text-transform: uppercase;
    background: rgba(245, 158, 11, 0.1);
    padding: 5px 12px;
    border-radius: 20px;
    border: 1px solid rgba(245, 158, 11, 0.25);
}

.book-header {
    text-align: center;
    margin-bottom: 25px;
    position: relative;
    z-index: 1;
}

.book-title {
    font-family: 'Cinzel', serif;
    font-size: 26px;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: 2px;
    text-transform: uppercase;
    line-height: 1.25;
    background: linear-gradient(180deg, #ffffff 0%, #cbd5e1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 6px;
}

.book-subtitle {
    font-size: 13.5px;
    font-weight: 400;
    color: var(--accent-gold);
    letter-spacing: 1px;
    text-transform: uppercase;
}

.synopsis-section {
    position: relative;
    z-index: 1;
    margin-bottom: 22px;
}

.synopsis-headline {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 17px;
    color: #f1f5f9;
    line-height: 1.45;
    margin-bottom: 12px;
    text-align: center;
}

.synopsis-text {
    font-size: 13.5px;
    line-height: 1.7;
    color: var(--text-secondary);
    text-align: justify;
    margin-bottom: 16px;
}

.highlights-card {
    background: var(--card-surface);
    border: 1px solid var(--card-border);
    border-radius: 8px;
    padding: 16px 20px;
    margin-bottom: 22px;
    position: relative;
    z-index: 1;
}

.highlights-title {
    font-size: 13px;
    font-weight: 700;
    color: var(--accent-gold);
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
}

.highlights-list {
    list-style: none;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px 18px;
}

.highlights-list li {
    font-size: 12.5px;
    color: var(--text-secondary);
    display: flex;
    align-items: center;
    gap: 8px;
}

.highlights-list li span.bullet {
    color: var(--accent-cyan);
    font-weight: bold;
    font-size: 14px;
}

.reviews-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 15px;
    margin-bottom: 22px;
    position: relative;
    z-index: 1;
}

.review-card {
    background: rgba(0, 0, 0, 0.28);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-left: 3px solid var(--accent-gold);
    border-radius: 6px;
    padding: 12px 14px;
}

.star-rating {
    color: var(--accent-gold);
    font-size: 12px;
    margin-bottom: 6px;
    letter-spacing: 2px;
}

.review-quote {
    font-family: 'Playfair Display', serif;
    font-style: italic;
    font-size: 12.5px;
    line-height: 1.5;
    color: #e2e8f0;
    margin-bottom: 6px;
}

.review-author {
    font-size: 11px;
    font-weight: 600;
    color: var(--text-muted);
    text-align: right;
}

.author-box {
    display: flex;
    align-items: center;
    gap: 16px;
    background: var(--card-surface);
    border: 1px solid var(--card-border);
    border-radius: 8px;
    padding: 14px 18px;
    margin-bottom: 24px;
    position: relative;
    z-index: 1;
}

.author-box img {
    width: 68px;
    height: 68px;
    border-radius: 50%;
    border: 2px solid var(--accent-cyan);
    object-fit: cover;
    flex-shrink: 0;
}

.author-details h4 {
    font-size: 14.5px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 2px;
}

.author-details .author-role {
    font-size: 11.5px;
    font-weight: 600;
    color: var(--accent-gold);
    margin-bottom: 4px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.author-details p {
    font-size: 12px;
    line-height: 1.5;
    color: var(--text-secondary);
}

.cover-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-top: 18px;
    border-top: 1px dashed rgba(255, 255, 255, 0.15);
    position: relative;
    z-index: 1;
}

.publisher-info {
    display: flex;
    flex-direction: column;
    gap: 4px;
}

.publisher-info img {
    height: 38px;
    width: auto;
}

.publisher-url {
    font-size: 10.5px;
    color: var(--text-muted);
    letter-spacing: 0.5px;
}

.barcode-area {
    display: flex;
    flex-direction: column;
    align-items: flex-end;
    gap: 4px;
}

.barcode-area img {
    height: 62px;
    width: auto;
    background: #ffffff;
    padding: 3px;
    border-radius: 3px;
}

.price-tag {
    font-size: 12px;
    font-weight: 700;
    color: var(--accent-gold);
    letter-spacing: 1px;
}

.page-footer {
    font-size: 12px;
    color: var(--text-muted);
    text-align: center;
    margin-top: 10px;
}
```

---

## OUTPUT:
The book back cover webpage rendered at `http://127.0.0.1:8000/`:

```text
==========================================================================================
                               SAVEETHA ENGINEERING COLLEGE
                  DEPARTMENT OF ARTIFICIAL INTELLIGENCE AND DATA SCIENCE
------------------------------------------------------------------------------------------
Student Name: V Kamalesh Kannan   | Register No: 26011247   | Course: 19AI414 - FWAD
==========================================================================================

+----------------------------------------------------------------------------------------+
| [COMPUTER SCIENCE / AI]                                              [SECOND EDITION]  |
|                                                                                        |
|                     MASTERING MODERN WEB DEVELOPMENT & AI                              |
|             Architecting High-Performance, Scalable Web Applications                   |
|                                                                                        |
|  "The essential roadmap from foundational web protocols to enterprise AI integration." |
|                                                                                        |
|  In today's fast-paced digital ecosystem, creating dynamic web applications requires   |
|  far more than basic markup. This definitive handbook bridges frontend interfaces,     |
|  Django architectures, and machine learning models into unified solutions...           |
|                                                                                        |
|  WHAT YOU WILL MASTER INSIDE:                                                          |
|  ✔ Modern HTML5 Semantic Markup & CSS3 Grid/Flexbox                                    |
|  ✔ Django Framework: MVC/MVT Architecture & Routing                                    |
|  ✔ Responsive Web Design & Interactive Media Integration                               |
|  ✔ Production Deployment, Microservices & Security Best Practices                      |
|                                                                                        |
|  REVIEWS:                                                                              |
|  ★★★★★ "An authoritative masterpiece that demystifies full-stack engineering."         |
|  ★★★★★ "Hands down the most comprehensive and practical guide for students."           |
|                                                                                        |
|  AUTHOR SPOTLIGHT:                                                                     |
|  [Photo] V Kamalesh Kannan - Author & Software Architect                               |
|          Researcher specializing in AI and Web Frameworks at SEC.                      |
|                                                                                        |
|  SAVEETHA ACADEMIC PRESS                       PRICE: ₹799 / $39.99 USD                |
|  www.saveetha.ac.in/press                      ||||||||||||||||||||||||||              |
|                                                ISBN 978-93-89845-05-9                  |
+----------------------------------------------------------------------------------------+
==========================================================================================
```

---

## RESULT:
The program for designing book back cover page using HTML and CSS is completed successfully.
