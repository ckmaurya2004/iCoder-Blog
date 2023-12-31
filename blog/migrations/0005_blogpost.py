# Generated by Django 4.2.3 on 2023-07-21 04:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_alter_post_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('S_no', models.AutoField(primary_key=True, serialize=False)),
                ('comments', models.TextField(max_length=500)),
                ('timestemp', models.DateField(default=django.utils.timezone.now)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blogpost')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
