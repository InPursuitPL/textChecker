# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 08:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textChecker', '0002_personaldata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personaldata',
            old_name='bad_words',
            new_name='wrong_words',
        ),
    ]
