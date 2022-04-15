from app import flask_app
import googlecloudprofiler

if __name__ == '__main__':

    # Profiler initialization. It starts a daemon thread which continuously
    # collects and uploads profiles. Best done as early as possible.
    try:
        googlecloudprofiler.start(
            service='webapp',
            # verbose is the logging level. 0-error, 1-warning, 2-info, 3-debug. It defaults to 0 (error) if not set.
            verbose=3,
            # project_id must be set if not running on GCP.
            # project_id='my-project-id',
        )
    except (ValueError, NotImplementedError) as exc:
        print(exc)  # Handle errors here
    flask_app.run(debug=True, host='0.0.0.0', port=8080)