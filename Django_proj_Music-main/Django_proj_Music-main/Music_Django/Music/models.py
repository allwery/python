from django.db import models


class Buyer(models.Model):
    first_name = models.CharField(max_length=200, default="", verbose_name='Имя')
    last_name = models.CharField(max_length=200, default="", verbose_name='Фамилия')
    email = models.CharField(max_length=254, verbose_name='Почта')

    def __unicode__(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'


class Place(models.Model):
    type = (("fun-zone", "Фан-Зона"),
            ("dance-floor", "Танцпол"),
            ("M-G", "Встреча с певцом"))
    place = models.CharField(max_length=50, choices=type, verbose_name='Тип билета')
    cost = models.IntegerField(verbose_name='Цена билета')

    def __unicode__(self):
        return self.place

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Concert(models.Model):
    name = models.CharField(max_length=200, default="", verbose_name='Название концерта')
    date_concert = models.DateTimeField(verbose_name='Дата проведения')
    place = models.CharField(max_length=200, default="", verbose_name='Место проведения')
    singer = models.CharField(max_length=200, default="", verbose_name='Певец')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Концерт'
        verbose_name_plural = 'Концерты'


class Buying(models.Model):
    buy_date = models.DateTimeField(verbose_name='Дата покупки билета')
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, verbose_name='Концерт')
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, verbose_name='Покупатель')
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место')

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Покупка билета'
        verbose_name_plural = 'Покупки билетов'
