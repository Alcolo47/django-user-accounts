# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_fix_str'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='language',
            field=models.CharField(choices=[('af', 'Afrikaans'), ('ar', 'العربيّة'), ('ast', 'asturian'), ('az', 'Azərbaycanca'), ('bg', 'български'), ('be', 'беларуская'), ('bn', 'বাংলা'), ('br', 'brezhoneg'), ('bs', 'bosanski'), ('ca', 'català'), ('cs', 'česky'), ('cy', 'Cymraeg'), ('da', 'dansk'), ('de', 'Deutsch'), ('el', 'Ελληνικά'), ('en', 'English'), ('en-a', 'Australian English'), ('en-gb', 'British English'), ('eo', 'Esperanto'), ('es', 'español'), ('es-ar', 'español de Argentina'), ('es-mx', 'español de Mexico'), ('es-ni', 'español de Nicaragua'), ('es-ve', 'español de Venezuela'), ('et', 'eesti'), ('e', 'Basque'), ('fa', 'فارسی'), ('fi', 'suomi'), ('fr', 'français'), ('fy', 'frysk'), ('ga', 'Gaeilge'), ('gl', 'galego'), ('he', 'עברית'), ('hi', 'Hindi'), ('hr', 'Hrvatski'), ('h', 'Magyar'), ('ia', 'Interlingua'), ('id', 'Bahasa Indonesia'), ('io', 'ido'), ('is', 'Íslenska'), ('it', 'italiano'), ('ja', '日本語'), ('ka', 'ქართული'), ('kk', 'Қазақ'), ('km', 'Khmer'), ('kn', 'Kannada'), ('ko', '한국어'), ('lb', 'Lëtzebuergesch'), ('lt', 'Lietuviškai'), ('lv', 'latvieš'), ('mk', 'Македонски'), ('ml', 'Malayalam'), ('mn', 'Mongolian'), ('mr', 'मराठी'), ('my', 'မြန်မာဘာသာ'), ('nb', 'norsk (bokmål)'), ('ne', 'नेपाली'), ('nl', 'Nederlands'), ('nn', 'norsk (nynorsk)'), ('os', 'Ирон'), ('pa', 'Punjabi'), ('pl', 'polski'), ('pt', 'Português'), ('pt-br', 'Português Brasileiro'), ('ro', 'Română'), ('r', 'Русский'), ('sk', 'slovenský'), ('sl', 'Slovenščina'), ('sq', 'shqip'), ('sr', 'српски'), ('sr-latn', 'srpski (latinica)'), ('sv', 'svenska'), ('sw', 'Kiswahili'), ('ta', 'தமிழ்'), ('te', 'తెలుగు'), ('th', 'ภาษาไทย'), ('tr', 'Türkçe'), ('tt', 'Татарча'), ('udm', 'Удмурт'), ('uk', 'Українська'), ('ur', 'اردو'), ('vi', 'Tiếng Việt'), ('zh-cn', '简体中文'), ('zh-hans', '简体中文'), ('zh-hant', '繁體中文'), ('zh-tw', '繁體中文')], max_length=10, verbose_name='language', default='fr'),
        ),
    ]
