# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_question_questionid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='questionId',
        ),
    ]
