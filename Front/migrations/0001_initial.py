# Generated by Django 4.1.1 on 2022-09-29 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_us_section',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.repeatfields')),
                ('main_title', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            bases=('Authentication.repeatfields',),
        ),
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.repeatfields')),
                ('video', models.URLField()),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            bases=('Authentication.repeatfields',),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.repeatfields')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField()),
            ],
            bases=('Authentication.repeatfields',),
        ),
        migrations.CreateModel(
            name='Contact_section',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            bases=('Authentication.repeatfields',),
        ),
        migrations.CreateModel(
            name='Featured_Agents_Section',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            bases=('Authentication.repeatfields',),
        ),
        migrations.CreateModel(
            name='Newsletter_Section',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            bases=('Authentication.repeatfields',),
        ),
        migrations.CreateModel(
            name='Newsletters',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.repeatfields')),
                ('email', models.EmailField(max_length=254)),
            ],
            bases=('Authentication.repeatfields',),
        ),
        migrations.CreateModel(
            name='Recent_Property_Section',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            bases=('Authentication.repeatfields',),
        ),
        migrations.CreateModel(
            name='Reviews_Section',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            bases=('Authentication.repeatfields',),
        ),
        migrations.CreateModel(
            name='Site_Informations',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.repeatfields')),
                ('name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('copyright', models.TextField()),
                ('logo', models.ImageField(upload_to='Logo__Image')),
            ],
            bases=('Authentication.repeatfields',),
        ),
        migrations.CreateModel(
            name='Teams_meet_section',
            fields=[
                ('repeatfields_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Authentication.repeatfields')),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
            bases=('Authentication.repeatfields',),
        ),
    ]
