import streemie.dark_arts  # noqa

from flask import Flask, jsonify
from streemie.db import db
from streemie.flask_config_environ import envvar, mergeall, to_bool

app = Flask(__name__)
app.config.from_object('streemie.config')
app.config.update(
    mergeall(
        envvar('STREEMIE_HOST', default='0.0.0.0', key='HOST'),
        envvar('STREEMIE_PORT', default=5000, convert=int, key='PORT'),
        envvar('STREEMIE_DEBUG', default=False, convert=to_bool, key='DEBUG'),
        envvar('STREEMIE_DATABASE_URI', key='SQLALCHEMY_DATABASE_URI'),
        envvar('STREEMIE_SECRET', key='SECRET_KEY')
    ))
db.init_app(app)
app.app_context().push()
db.engine.pool._use_threadlocal = True  # for gevent


@app.route('/api/encode', methods=['GET', 'POST'])
def encode():
    return jsonify({})


@app.route('/api/encode/<job_id>', methods=['GET', 'PATCH', 'DELETE', 'POST'])
def encoder_job(job_id):
    return jsonify({})


@app.route('/api/encode/<job_id>/output', methods=['GET', 'DELETE'])
def encoder_job_output(job_id):
    return jsonify({})


@app.route('/api/encode/<job_id>/output/<file_name>')
def encoder_job_output_file(job_id, file_name):
    return jsonify({})


if __name__ == '__main__':
    # TODO: replace with a proper warning log later
    print(
        'warn: this software is intended to be deployed via',
        'gunicorn and the gevent worker.',
        'Flask runner WILL NOT function properly.'
    )
    app.run()
