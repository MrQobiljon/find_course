from django.db import models

# Create your models here.

class Category(models.Model):
    """Bu model tillarni yonlaishlari uchun. Maslan: Ingiliz tili"""
    name = models.CharField(max_length=255, verbose_name="Kategoriya nomi", unique=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class WebService(models.Model):
    """Bu model tilni o'rganish manbasi qaysi Web service da ekanligiga hizmat qiladi. Masalan: Sayt yoki Telegram"""
    name = models.CharField(max_length=255, verbose_name="Web service nomi", unique=True, help_text="Web service nomi, masalan: Telegram")
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Source(models.Model):
    name = models.CharField(max_length=255, verbose_name="Manba nomi", help_text="Masalan: IELTS 10 kun ichida")
    url = models.URLField(verbose_name="Manba linki")
    web_service = models.ForeignKey(WebService, on_delete=models.CASCADE, verbose_name="Web service nomi")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriyaysi")
    description = models.TextField(blank=True, null=True, verbose_name="Qo'shimcha ma'lumotlar uchun")

    def __str__(self):
        return self.name




# class LinkSource(models.Model):
#     # source = models.ForeignKey(Source, on_delete=models.CASCADE, verbose_name="Manba nomi", related_name="sources")
#     # topic = models.CharField(max_length=255, verbose_name="Dars yo'nalishi nomi", help_text="Masalan: IELTS 10 kun ichida")
#     # url = models.URLField(verbose_name="Manba linki")
#     # web_service = models.ForeignKey(WebService, on_delete=models.CASCADE, verbose_name="Web service nomi")
#
#     def __str__(self):
#         return self.web_service.name