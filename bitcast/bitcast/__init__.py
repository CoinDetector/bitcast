from __future__ import absolute_import

# Django가 시작할 때  shared_task가 이 앱을 이용할 수 있도록 app이 항상 import 되게 해준다.
from .celery import app as celery_app  # noqa


