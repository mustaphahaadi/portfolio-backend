from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_api', '0010_merge_0008_seed_data_0009_backfill_seed_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture_url',
            field=models.URLField(
                blank=True,
                help_text='Public image URL for free hosting (Cloudinary/GitHub/Imgur), used before file upload',
                null=True,
            ),
        ),
    ]
