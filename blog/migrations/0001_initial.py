# Generated by Django 4.0.6 on 2022-08-15 20:34

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('wagtailimages', '0024_index_image_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('custom_title', models.CharField(help_text='Overwrites the default title', max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('custom_title', models.CharField(help_text='Overwrites the default title', max_length=100)),
                ('content', wagtail.fields.StreamField([('title_and_text', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('text', wagtail.blocks.TextBlock(help_text='Add additonal text', required=True))])), ('full_richtext', streams.blocks.RichTextBlock()), ('cards', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(help_text='Add your title', required=True)), ('cards', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('title', wagtail.blocks.CharBlock(masx_lenght=40, required=True)), ('text', wagtail.blocks.TextBlock(max_length=200, required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(help_text='If the button text above is selected, it will be used.', required=False))])))])), ('cta', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(max_length=60, required=True)), ('text', wagtail.blocks.RichTextBlock(required=True)), ('button_page', wagtail.blocks.PageChooserBlock(required=False)), ('button_url', wagtail.blocks.URLBlock(required=False)), ('button_text', wagtail.blocks.CharBlock(default='Learn More', max_length=40, required=True))]))], blank=True, null=True, use_json_field=None)),
                ('blog_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]