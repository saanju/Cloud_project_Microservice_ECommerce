# run.py
from application import create_app
#to run this application,use run.py
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
