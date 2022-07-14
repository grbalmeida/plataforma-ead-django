### Usando fixtures para fornecer dados iniciais aos modelos

```
python manage.py dumpdata courses --indent=2 --output=courses/fixtures/subjects.json
```

```
python manage.py loaddata subjects.json
```

As fixtures são convenientes não só para carregar dados iniciais, mas também para fornecer 
dados de exemplo à sua aplicação ou dados necessários para testes.