# Generated by Django 2.2.4 on 2021-06-04 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_delete_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='cate',
            field=models.ForeignKey(default='Hello', on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='app1.Category'),
            preserve_default=False,
        ),
    ]