"""
flask创建web app
"""

from settings.create_app import create_app


app = create_app()


if __name__ == "__main__":
    app.run(debug=app.config["DEBUG"], host='0.0.0.0', port=8000)
