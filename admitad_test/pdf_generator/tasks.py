import os
import logging
import traceback
import sys

from weasyprint import HTML
from django.conf import settings
from admitad_test.celeryconf import app

logger = logging.getLogger('generation')


@app.task
def generate_file(source, report_name):
    try:
        HTML(source).write_pdf(os.path.join(settings.REPORT_ROOT, report_name))
        logger.debug(f'generated pdf from {source}')
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        str_traceback = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        logger.exception(str_traceback)
