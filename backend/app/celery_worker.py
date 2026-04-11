from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['broken_url'],
        backend=app.config['result_backend']
    )
    celery.conf.update(app.config)

    return celery