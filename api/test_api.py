from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def create_app():
    from api.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    return app


@app.route("/")
def demo_text():
    return "Everything works!"


def test_app_status():
    """тест на отклик сайта"""
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert response.data == b'Everything works!'


@app.route("/alice")
def get_json():
    data = {"name": "Алиса"}
    return jsonify(data)


def test_app_get_json():
    """ тест на взятие json-данных """
    response = app.test_client().get('/alice')
    assert response.json.get("name") == "Алиса", "Имя получено неверно"

