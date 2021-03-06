### Usando fixtures para fornecer dados iniciais aos modelos

```
python manage.py dumpdata courses --indent=2 --output=courses/fixtures/subjects.json
```

```
python manage.py loaddata subjects.json
```

As fixtures são convenientes não só para carregar dados iniciais, mas também para fornecer 
dados de exemplo à sua aplicação ou dados necessários para testes.

### Usando herança de modelos

Django aceita herança de modelos. Ela funciona de modo semelhante à herança de classes padrão
de Python. As três opções a seguir estão disponíveis em Django para usar a herança de modelos:

* **Modelos abstrantos**: convenientes quando você quer colocar algumas informações comuns em vários modelos
* **Herança de modelos com várias tabelas**: aplicável quando cada modelo na hierarquia é considerado, por si só, um modelo completo
* **Modelos proxy**: convenientes quando precisamos alterar o comportamento de um modelo, por exemplo,
incluindo métodos adicionais, modificando o gerenciador default ou utilizando opções meta diferentes.

### Usando mixins com views baseadas em classe

As mixins são um tipo especial de herança múltipla para uma classe. Podemos usá-las para oferecer
funcionalidades discretas comuns, as quais, quando adicionadas a outras mixins, permitirão definir
o comportamento de uma classe. Há duas situações principais em que usamos mixins:

* queremos oferecer vários recursos opcionais a uma classe;
* queremos utilizar um recurso em particular em várias classes.