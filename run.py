from flask_hello import create_app
from flask_hello.config import dev_config

app = create_app(dev_config)

if __name__ == '__main__':
    with app.app_context():
        app.run()
