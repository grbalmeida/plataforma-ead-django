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

# Cache

### Usando o framework de cache

Ao fazer caching de consultas, resultados de cálculos ou de conteúdos renderizados em uma requisição
HTTP, evitaremos operações custosas nas próximas requisições. Isso se traduz em tempos de
resposta mais rápidos e em menos processamento do lado do servidor.

### Backends de cache disponíveis

Django inclui vários backends de cache. São eles:

* backends.memcached.MemcachedCache ou backends.memcached.PyLibMCCache: O Memcached é um servidor
de cache rápido e eficiente, baseado em memória.
* backends.db.DatabaseCache: utiliza o banco de dados com um sistema de cache.
* backends.db.FileBasedCache: utiliza um sistema de armazenagem de arquivos. Cada valor de cache
é serializado e armazenado como um arquivo separado.
* backends.locmem.LocMemCache: um backend para cache na memória local. É o backend de cache default.
* backends.dummy.DummyCache: um backend de cache dummy, para uso somente durante a fase de desenvolvimento.

**IMPORTANTE:** Para ter o melhor desempenho possível, utilize um backend de cache baseado em
memória, como o backend Memcached.

### Instalando o Memcached

O Memcached executa na memória e tem uma quantidade específica de RAM alocada para ele.
Quando a RAM alocada estiver cheia, o Memcached comecará a remover os dados mais antigos
para armazenar novos dados.

[Link para instalar Memcached no Windows](https://stackoverflow.com/questions/59476616/install-memcached-on-windows)

### Configurações de cache

Django disponibiliza as seguintes configurações de cache:

* CACHES: um dicionário que contém todos os caches disponíveis ao projeto;
* CACHE_MIDDLEWARE_ALIAS: o alias do cache a ser usado para armazenagem.
* CACHE_MIDDLEWARE_KEY_PREFIX: o prefixo a ser usado nas chaves do cache.
Define um prefixo para evitar colisões de chaves caso você compartilhe o cache
entre vários sites.
* CACHE_MIDDLEWARE_SECONDS: o número default de segundos para as páginas do cache.

### Níveis de cache

Django oferece os seguintes níveis de caching, listados a seguir em ordem crescente de especificidade:

* **API de baixo nível para o cache:** oferece o maior nível de especificidade. Permite fazer o caching
de consultas ou de cálculos específicos.
* **Cache de template:** permite fazer caching de fragmentos de templates.
* **Cache por view:** oferece caching para views individuais.
* **Cache por site:** o nível mais alto de caching. Faz o caching de todo o site.

**IMPORTANTE:** Pense em sua estratégia de caching antes de implementá-la. Mantenha o foco inicialmente
nas consultas ou nos cálculos custosos, que não sejam feitos por usuário.

### Caching de views

**IMPORTANTE:** O cache por view utiliza o URL para criar a chave de cache. Vários
URLS que apontem para a mesma view serão armazenados em cache separadamente.

# REST

### Definindo serializadores

O framework disponibiliza as classes a seguir para construir serializadores para objetos individuais:

* Serializer: provê serialização para instâncias de classes Python comuns;
* ModelSerializer: provê serialização para instâncias de modelos;
* HyperlinkedModelSerializer: igual a ModelSerializer, mas representa relacionamentos
entre objetos com links em vez de usar chaves primárias.

# Autenticação

### Lidando com autenticação

Eis os backends de autenticação oferecidos pelo framework REST:

* BasicAuthentication: é a autenticação HTTP básica. O usuário e a senha são enviados pelo cliente
no cabeçalho HTTP Authorization, codificados com Base64.

* TokenAuthentication: é a autenticação baseada em token. Um modelo Token é usado para armazenar
tokens de usuários. Os usuários incluem o token no cabeçalho HTTP Authorization para autenticação.

* SessionAuthentication: utiliza o backend de sessão de Django para autenticação. Esse backend
é conveniente para fazer requisições AJAX autenticadas à API a partir do frontend de seu site.

* RemoteUserAuthentication: permite que você delegue a autenticação para o seu servidor web,
que define uma variável de ambiente REMOTE_USER.

**IMPORTANTE:** A autenticação apenas identifica o usuário que está fazendo a requisição.
Ela não permite nem proíbe o acesso às views. Você deve usar as permissões para restringir
o acesso a elas.