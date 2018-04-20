from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/encode', methods=['GET', 'POST'])
def encode():
    return jsonify({})


@app.route(
    '/api/encode/<job_id>', methods=['GET', 'PATCH', 'DELETE', 'POST'])
def encoder_job(job_id):
    return jsonify({})


@app.route('/api/encode/<job_id>/output', methods=['GET', 'DELETE'])
def encoder_job_output(job_id):
    return jsonify({})


@app.route('/api/encode/<job_id>/output/<file_name>')
def encoder_job_output_file(job_id, file_name):
    return jsonify({})


if __name__ == '__main__':
    app.run()
