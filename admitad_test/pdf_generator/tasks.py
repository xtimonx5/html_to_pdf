import os

from weasyprint import HTML
from django.conf import settings
from admitad_test.celeryconf import app


@app.task
def generate_file(source, report_name):
    HTML(source).write_pdf(os.path.join(settings.REPORT_ROOT, report_name))
