from app import create_app

app = create_app()
@app.route('/')
def hello():
    count = 3
    return 'Hello World! I have been seen {} times.\n'.format(count)

