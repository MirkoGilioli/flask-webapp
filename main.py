from app import flask_app
import googlecloudprofiler

try:
    googlecloudprofiler.start(verbose=3)
except (ValueError, NotImplementedError) as exc:
    print(exc)

if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0', port=8080)