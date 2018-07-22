activate_this = '/home/mzhang/flask-payment/ENV/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0, '/home/mzhang/flask-payment')

from app import app as application

