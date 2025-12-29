"""
WSGI config for buybuy project.
"""

import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'buybuy.settings')

# Run migrations and create superuser on startup (for Railway deployment)
if os.environ.get('RAILWAY_ENVIRONMENT'):
    print("Railway detected, running migrations...")
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'migrate', '--noinput'])
    print("Migrations complete!")
    
    # Create superuser if not exists
    import django
    django.setup()
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    admin_username = os.environ.get('ADMIN_USERNAME', 'admin')
    admin_email = os.environ.get('ADMIN_EMAIL', 'admin@buybuy.com')
    admin_password = os.environ.get('ADMIN_PASSWORD', 'admin123456')
    
    if not User.objects.filter(username=admin_username).exists():
        User.objects.create_superuser(admin_username, admin_email, admin_password)
        print(f"Superuser '{admin_username}' created!")
    else:
        print(f"Superuser '{admin_username}' already exists.")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
