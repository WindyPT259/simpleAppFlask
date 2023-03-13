D:\
cd /d "D:\WORKS\04_PYTHON\simpleAppFlask"
start /K redis-cli shutdown
start timeout 5
start CMD /K redis-server
start CMD /K celery -A main.celery worker -l info
start CMD /K celery -A main.celery beat -l info -s log/celerybeat-schedule
start CMD /K py main.py
start CMD /K celery -A main.celery flower