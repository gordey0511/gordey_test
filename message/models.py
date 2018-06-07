from django.db import models


class Message(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)
    message = models.CharField(max_length=128,null=True)


    def __str__(self):
        return "Пользователь %s %s %s" % ( self.email, self.name, self.message)

    class Meta:
        verbose_name = 'MyMessage'
        verbose_name_plural = 'A lot of Message'