import sys
sys.path.insert(0, '/var/www/sign-generator')
sys.stdout = sys.stderr
from sign_generator import app as application

