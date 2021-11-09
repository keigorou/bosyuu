from django.db import models




class StoreList(models.Model):
    name = models.CharField(verbose_name='店舗名', max_length=50)
    slug = models.SlugField(blank=True, null=True, unique=True)
    email = models.EmailField(verbose_name='メールアドレス')

    def __str__(self) -> str:
        return self.name

class Recruit(models.Model):
    store = models.ForeignKey(StoreList, on_delete=models.CASCADE)
    recruitment_type = models.CharField(verbose_name='職種', max_length=50, blank=True)
    hourlywage = models.IntegerField(verbose_name='時給')
    hourlywage_description = models.CharField(verbose_name='時給詳細', max_length=50, blank=True)
    worktime = models.CharField(verbose_name='勤務時間', max_length=50, blank=True)
    worktime_description = models.CharField(verbose_name='勤務時間詳細', max_length=100, blank=True)
    description = models.TextField(verbose_name='詳細', blank=True)
    publish = models.BooleanField(verbose_name='公開する', blank=True, null=True)


    def __str__(self) -> str:
        return self.store.name

class User(models.Model):
    GENDER_CHOICES = (
        ('1', '女性'),
        ('2', '男性'),
    )
    user_store = models.ForeignKey(StoreList, blank=True, null=True, on_delete=models.CASCADE)
    user_name = models.CharField(verbose_name='名前', max_length=50)
    user_age = models.IntegerField(verbose_name='年齢')
    user_gender = models.CharField(verbose_name='性別', choices=GENDER_CHOICES, max_length=2, default=1)
    user_email = models.EmailField(verbose_name='メールアドレス')
    user_tel = models.CharField(verbose_name='電話番号', max_length=20)

    def __str__(self) -> str:
        return self.user_name