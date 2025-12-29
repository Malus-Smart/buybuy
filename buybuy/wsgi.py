"""
WSGI config for buybuy project.
"""

import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'buybuy.settings')

# Run migrations on startup (for Railway deployment)
if os.environ.get('RAILWAY_ENVIRONMENT'):
    print("Railway detected, running migrations...")
    from django.core.management import execute_from_command_line
    execute_from_command_line(['manage.py', 'migrate', '--noinput'])
    print("Migrations complete!")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
