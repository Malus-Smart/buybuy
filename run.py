import os
import subprocess
import sys

# Run migrations
print("Running migrations...")
subprocess.run([sys.executable, "manage.py", "migrate", "--noinput"])

# Start gunicorn
print("Starting server...")
os.execvp("gunicorn", ["gunicorn", "buybuy.wsgi"])

