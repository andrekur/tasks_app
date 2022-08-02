from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class TaskModel(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField()
    end_date = models.DateField()
    create_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='my_tasks'
    )
    task_performers = models.ManyToManyField(UserModel)

    # TODO verbose_name

    def __str__(self):
        return f'{self.name}_{self.owner.username}'
