# 🧠 FrAIgrance Backend

This is the backend service powering **FrAIgrance**, an AI-driven storytelling platform for fragrances. Built with Django and PostgreSQL, it handles authentication, credit management, AI generation logic, and Stripe integration.

---

## 🚀 Getting Started

### **1️⃣ Clone the Repository**

```sh
 git clone https://github.com/AlexandruCrisan/FrAIgrance-be.git
 cd FrAIgrance-be
```

### **2️⃣ Install Dependencies**

```sh
 pip install -r requirements.txt
```
### **3️⃣ Set Up Environment Variables**

Create a `.env` file and add:

```env
# Django
SECRET_KEY=your_django_secret_key
DEBUG_MODE=True

# Database
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=1234

# Auth0
AUTH0_DOMAIN=your_auth0_domain
AUTH0_AUDIENCE=your_auth0_audience
AUTH0_CLIENT_ID=your_auth0_client_id
AUTH0_CLIENT_SECRET=your_auth0_client_secret
ALGORITHMS=RS256

# Stripe
STRIPE_API_SECRET_KEY=your_stripe_api_secret_key
STRIPE_WEBHOOK_SECRET=your_stripe_webhook_secret

# (Optional) Prices from Stripe
PRICE_ID0 = price_...
PRICE_ID1 = price_...
...

# OpenAI
OPENAI_API_KEY=your_openai_api_key

# Client (frontend)
CLIENT_URL = http://localhost:3000  (for development env)
```

### **4️⃣ Apply Migrations and Run the Server**

```sh
 python manage.py makemigrations
 python manage.py migrate
 python manage.py runserver
```

---
