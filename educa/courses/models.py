from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Course(models.Model):
    # O instrutor que criou o curso em questão
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)

    # O assunto ao qual o curso pertence. É um campo ForeignKey que aponta para o modelo Subject
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)

    # O título do curso
    title = models.CharField(max_length=200)

    # O slug do curso. Será usado nos URLs
    slug = models.SlugField(max_length=200, unique=True)

    # Um coluna TextField para armazenar uma descrição geral do curso
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)

    # Um campo ForeignKey para o modelo ContentType
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    # Um PositiveIntegerField para armazenar a chave primária do objeto relacionado
    object_id = models.PositiveIntegerField()

    # Um campo GenericForeignKey para o objeto relacionado combinando os dois campos anteriores
    item = GenericForeignKey('content_type', 'object_id')