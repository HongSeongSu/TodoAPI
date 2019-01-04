from django.db import models

PRIORITY = (
    ('1', '중요'),
    ('2', '보통'),
    ('3', '사소'),
)


class Todo(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    deadline = models.DateField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True, null=True)
    priority = models.CharField(max_length=1, choices=PRIORITY, default='2')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["priority"]

    objects = models.Manager()
