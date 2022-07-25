from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.loader import render_to_string
from .fields import OrderField

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

    students = models.ManyToManyField(User, related_name='courses_joined', blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # Isso significa que o número de ordem de um novo módulo será atribuído
    # somando-se 1 ao último módulo do mesmo objeto Course.
    order = OrderField(blank=True, for_fields=['course'])

    def __str__(self):
        return f'{self.order}. {self.title}'

    class Meta:
        ordering = ['order']

class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)

    # Um campo ForeignKey para o modelo ContentType
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model_in': ('text', 'video', 'image', 'file')})

    # Um PositiveIntegerField para armazenar a chave primária do objeto relacionado
    object_id = models.PositiveIntegerField()

    # Um campo GenericForeignKey para o objeto relacionado combinando os dois campos anteriores
    item = GenericForeignKey('content_type', 'object_id')

    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']

class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title

    def render(self):
        return render_to_string(
            f'courses/content/{self._meta.model_name}.html', {'item': self})

class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
    file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()