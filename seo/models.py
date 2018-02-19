from django.db import models

# Create your models here.
class SeoModel(models.Model):
    class Meta:
        db_table = "seo"

    page_name_uk = models.CharField(max_length = 70)
    page_name_en = models.CharField(max_length = 70)
    page_name_ru = models.CharField(max_length = 70)

    seo_title_uk = models.CharField(max_length = 170)
    seo_title_en = models.CharField(max_length = 170)
    seo_title_ru = models.CharField(max_length = 170)

    seo_description_uk = models.TextField()
    seo_description_en = models.TextField()
    seo_description_ru = models.TextField()

    seo_keywords_uk = models.TextField()
    seo_keywords_en = models.TextField()
    seo_keywords_ru = models.TextField()

def __str__(self):
    return self.page_name_en
