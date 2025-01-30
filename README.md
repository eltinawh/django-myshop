# django-myshop
A Django app

## Key Features

## Requirement

Before you begin, make sure you have the following installed:
- Python 3.11 or higher
- pip (Python package installer)
- venv (Python virtual environment manager)
- git (version control system)
- docker (containerization platform)

We will use Django version >=5.1.

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/eltinawh/django-myshop.git

# navigate to the project directory
cd django-myshop
```

### 2. Set up a virtual environment
```bash
# Create a virtual environment
python3 -m venv .venv

# Activate the virtual environment (Linux/MacOS)
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations

Run the following commands to create the necessary database tables 
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a superuser

To access the Django admin panel, create a superuser account:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up the admin credentials.

### 6. Prepare Stripe API keys

[Stripe](https://stripe.com/) is a popular, reliable, secure third party payment gateway. We will use this to manage customers' orders and payment processing.

Register [here](https://dashboard.stripe.com/register), verify your email, and then create test [API key](https://dashboard.stripe.com/test/apikeys).

Create a `.env` file in the root directory and add Stripe published key and secret key to it.
```
STRIPE_PUBLISHABLE_KEY=pk_test_xxx
STRIPE_SECRET_KEY=sk_test_xxx
```

### 7. Prepare email backend

We will send order confirmation to user's email. For development purposes, we can use console email backend in which the email will be printed on the console. To enable this, update the `core/settings.py` file like so.
```
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_HOST = config("EMAIL_HOST")
# EMAIL_PORT = config("EMAIL_PORT")
# EMAIL_USE_TLS = config("EMAIL_USE_TLS")
# EMAIL_HOST_USER = config("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
# DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL")
```

Or you can use an external SMTP server, such as Google Mail and add these variables to the `.env` file and leave the `core/settings.py` file as is.
```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=[the email address]
EMAIL_HOST_PASSWORD=[the password]
DEFAULT_FROM_EMAIL=[default from email]
```


### 8. Install RabbitMQ docker image

Tasks that are data-heavy, resource-intensive, time-consuming, or prone to failure (requiring a retry mechanism) should be handled as asynchronous processes outside the request/response cycle. One of such tasks is sending order confirmation email to user. To enable the asynchronous tasks we will use [Celery](https://docs.celeryq.dev/en/stable/index.html) and [RabbitMQ](https://www.rabbitmq.com/).

We will use the RabbitMQ docker image.
```bash
docker pull rabbitmq:4.0.5-management
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0.5-management
# ...
# Server startup complete; 4 plugins started.
# ...
```
Open http://127.0.0.1:15672/ in your browser. You will see the login screen for the management UI of RabbitMQ. Enter `guest` as both the username and the password and click on Login.

### 9. Start Celery worker

Celery is installed as Python package listed in the requirements.txt. Open another shell and run this command.
```bash
celery -A core worker -l info
```

### 10. Install Redis docker image

Product recommendation engine utilizes Redis, a fast in-memory storage. We will use the Redis docker image.

```bash
docker pull redis:7.4.2
docker run -it --rm --name redis -p 6379:6379 redis:7.4.2
# Server initialized
# * Ready to accept connections
```
Keep the Redis server running.

### 11. Run the development server

Start the development server to verify everything is working correctly.
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` in your browser to see the application.

## Technical Details

### Project Structure
This project consists of the following apps:

1. **Shop app**

2. **Cart app**

3. **Orders app**

4. **Payment app**


## Documentation

[Official Django Documentation](https://www.djangoproject.com/)
