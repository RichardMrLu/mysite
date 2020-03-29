import datetime

from django.db import models
from django.utils import timezone





# Create your models here.



class Question(models.Model):   #相当于一张表
    question_text = models.CharField(max_length=200)  #列名
    pub_date = models.DateTimeField('date published')  #列名

    def __str__(self):
        return self.question_text

    def was_published_recently(self): #self用来调用类自身的变量
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'


class Choice(models.Model):  #相当于一张表
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  #Choice表的外键为Question_id
    choice_text = models.CharField(max_length=200)  #列名
    votes = models.IntegerField(default=0)    #列名

    def __str__(self):
        return self.choice_text









#############################################################
    ##测试代码

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name



class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()        # 进组时间
    invite_reason = models.CharField(max_length=64)  # 邀请原因
