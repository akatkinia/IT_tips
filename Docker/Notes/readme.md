## Часто используемые команды
* ```docker run hello-world``` - запустить образ (по умолчанию как фоновый процесс -d). Если образ не найден на docker-host, он сначала будет скачен из подключенных репозиториев
* ```docker run -it -p 8000:8443 python:alpine /bin/sh``` - запустить контейнер на основе базового образа python:alpine, пробросить порты и провалиться внутрь контейнера в оболочку /bin/sh
* ```docker port <CONTAINER_NAME>``` - посмотреть проброшенные порты в контейнере, где первый порт это порт на хостовой машине, а второй порт это порт внутри контейнера. Т.е., например 8000:8443 если обратиться к порту 8000 на хостовой машине, запрос будет перенаправлен на порт 8443 внутри контейнер
* ```docker ps``` - посмотреть какие контейнеры запущены на машине
* ```docker ps -a``` - посмотреть все контейнеры как запущенные, так и не запущенные, но существующие локально
* ```docker stop <container_name>``` - остановить контейнер
* ```docker rm <container_name>``` - удалить контейнер
* ```docker rmi <image_name>``` - удалить образ
* ```docker system prune``` - удалить все неиспользующиеся образы в системе (очистить кэш слоев)
* ```docker attach <CONTAINER_NAME>``` - подключить к уже запущенному контейнеру
* ```docker exec -it <CONTAINER_NAME> /bin/bash``` - зайти в контейнер в новой оболочке, либо исполнить команду
* ```docker rm $(docker ps -f status=exited -aq)``` - удалить все контейнеры со статусом exited
* ```docker rm $(docker ps -aq)``` - удалить все контейнеры
* ```docker rmi $(docker images -a -q)``` - удалить все образы
* ```docker logs <container_name>``` - посмотреть логи контейнера
* ```docker build -t <CONTAINER_NAME> .``` - собрать образ из Dockerfile
* ```docker images``` - показать все образы, что доступны на docker-host
* ```docker pull <image_name>``` - скачать образ
* ```docker network create <network_name>``` - создание сети для контейнеров (подробнее расписано ниже в разделе DOCKER NETWORKS)
* ```docker network ls``` - посмотреть список доступных сетей на хосте
* ```docker run --net=my_network nginx``` - запустить контейнер nginx:latest с сетью my_network
* ```docker rename <old_container_name> <new_container_name>``` - переименование контейнера
* ```docker --help``` - полный перечень команд
* ```docker build -t <image_name>:<tag> .``` - сборка образа из Dockerfile. Ключ -t позволяет указать тег (именованная версия образа, которую можно использовать для его идентификации). Например ```docker build -t reponame/imagename:3.0.1 .```. Таким образом, команда строит Docker-образ с тегом 3.0.1 в репозитории reponame/imagename
* ```docker push <image_name:tag>``` - загрузить образ в registry. Например ```docker push reponame/imagename:3.0.1```.
* ```docker push <yourusername>/<imagename>:<tag>```- загрузить образ в свой собственный registry (не dockerhub). Например ```docker push gcr.io/your-project-id/imagename:3.0.1```
* ```docker login``` - войти в свой аккаунт на dockerhub
* ```docker login <registry_url>``` - войти в свой аккаунт в другом registry. Например ```docker login gcr.io```
  
## Монтирование  
Docker предоставляет два основных механизма для работы с файлами и данными между хост-системой и контейнерами: 
* **docker volumes (тома)** 
* **bind mounts (привязанные монтирования)**  
  
Они имеют различия в функциональности, использовании и характеристиках:
* **Docker Volumes (Тома):**  
  * Тома управляются Docker и хранятся в специальной части файловой системы Docker на хосте. Это означает, что они независимы от файловой системы хоста.
  * Тома могут быть совместно использованы между контейнерами, даже когда контейнеры запускаются на разных хостах в кластере Docker.
  * Docker позволяет более удобно управлять томами, например, переименовывать, удалять, создавать их заранее.
  * Тома могут иметь опции для шифрования данных в покое и т.д.
  * Используется с помощью ключевого слова volumes в Docker Compose или флага -v при запуске контейнера.
* **Bind Mounts (Привязанные монтирования):**
  * Привязанные монтирования монтируют прямо существующие пути с хост-системы в контейнер. Это означает, что они полностью зависят от файловой системы хоста.
  * Привязанные монтирования подходят для сценариев, где вы хотите, чтобы изменения в файлах контейнера сразу же отражались в файлах на хосте и наоборот.
  * Они позволяют более прямое управление над местоположением данных на хосте
  * Используется с помощью флага -v при запуске контейнера или секции volumes в Docker Compose.
  
### VOLUMES
**Тома (Volumes)** - внешнее хранилище. Тома могут быть расположены на docker-хосте или даже на удалённой машине.  
Когда контейнер умирает, все данные, которые он создал (журналы, БД и тд) умирают вместе с ним. Чтобы избежать потери данных, следует использовать тома.  
Тома можно монтировать в режиме только для чтения.  
```--volume``` - создать файл или каталог, если он не находится в docker host
```--mount``` - не создаёт его автоматически, но генерирует ошибку  
  
#### Примеры команд:
* ```docker volume create <VOLUME_NAME>``` - создать том
* ```docker volume rm <VOLUME_NAME>``` - удалить том
* ```docker volume prune``` - удалить неиспользуемые тома
* ```docker volume inspect <VOLUME_NAME>``` - посмотреть том
* ```run -it -v my-volume:/data --name my-container selaworkshop/busybox:latest``` - запуск контейнера в интерактивном режиме и подключает volume my-volume (создаёт если его нет, либо использует существующий если он есть) в директорию /data, монтируя его с docker-host (как правило находится по пути /var/lib/docker/volumes/ на Linux)  
  
### BIND MOUNTS

___

## Отправить образ в удалённый репозиторий
1. Войти в наш репозиторий ```docker login <registry hub>``` (по умолчанию удалённый репозиторий используется как dockerhub)
2. Тегирование образа. Когда образ создан, ему нужно присвоить тег, который будет идентифицировать версию или какую-либо метку образа. Обычно это делается с помощью команды docker tag следующим образом: ```docker tag <имя_образа>:<текущий_тег> <имя_репозитория>:<новый_тег>```. Например: ```docker tag my-app:latest myusername/my-app:v1.0```
3. Отправка образа. Затем используйте команду docker push, чтобы отправить образ в репозиторий. Укажите имя репозитория и тег: ```docker push <имя_репозитория>:<тег>```. Например: ```docker push myusername/my-app:v1.0```

## Отправить образ в локальный репозиторий
1. Сначала необходимо протегировать образ ```docker tag slowe/image3:0.1 localhost:5000/image3:0.1```. Таким образом если посмотреть в ```docker image ls``` мы увидим, будто у нас создался второй образ ```slowe/image3:0.1```, но имеющий префикс ```localhost:```.  
**Теги** - это просто указатели на образы. Эта команда тегирует существующий Docker-образ ```slowe/image3:0.1``` новым именем и тегом: ```localhost:5000/image3:0.1```.  
Тегирование образа означает создание новой ссылки на существующий образ. Новый тег ```localhost:5000/image3:0.1``` будет указывать на тот же самый образ, что и ```slowe/image3:0.1```.  
2. Теперь имея localhost tag мы можем использовать команду ```docker push``` чтобы отправить этот образ в **registry**, что работает в нашей системе ```docker push localhost:5000/image3```. Эта команда отправляет Docker-образ с тегом ```localhost:5000/image3:0.1``` в "удалённый реестр" по адресу ```localhost:5000```  
  
  
## Как запускать Docker без sudo
Наиболее распространенный способ - добавить вашего пользователя в группу docker. Это позволит вам запускать Docker команды без использования sudo.  
```sudo usermod -aG docker $USER```  
После этого выходите из текущей сессии или перезагрузите систему, чтобы изменения вступили в силу.  
  
  
## DOCKER NETWORKS  
**Docker networks** предоставляют механизм для изоляции контейнеров, а также обеспечивают коммуникацию между ними. С их помощью можно создавать виртуальные сети, внутри которых контейнеры могут взаимодействовать друг с другом без необходимости использовать хост-сеть (Хост-сеть в Docker представляет собой сеть, в которой контейнеры могут использовать сетевые ресурсы хоста напрямую, минуя изоляцию. Когда вы запускаете контейнер с использованием опции ```--network=host```, контейнер использует сетевые настройки хоста вместо создания собственной изолированной сети. Это может быть полезным, когда вам нужно, чтобы контейнер имел доступ к сетевым службам на хосте, например, к базе данных или веб-серверу, работающему на хосте).  
Это повышает безопасность, управляемость и масштабируемость приложений, использующих Docker.  
  
Несколько примеров работы с Docker networks:  
**1. Создание Docker Networks:**  
```docker network create my_network``` - эта команда создает новую сеть с именем my_network  
```docker network ls``` - посмотреть список доступных сетей на хосте

**2. Запуск контейнера в определенной сети:**  
```docker run --name my_container --network my_network -d nginx``` - эта команда запускает контейнер с именем my_container в сети my_network, используя образ Nginx в фоновом режиме.  

**3. Связывание контейнеров в одной сети:**  
```
docker run --name container1 --network my_network -d nginx
docker run --name container2 --network my_network -d nginx
```
Оба контейнера (container1 и container2) теперь находятся в сети my_network и могут взаимодействовать друг с другом по именам контейнеров.

**4. Использование пользовательских сетей:**  
```docker network create --driver bridge my_custom_network``` - эта команда создает пользовательскую сеть с именем my_custom_network с использованием драйвера bridge ( тип драйвера сети, который создает виртуальную сеть на хосте для взаимодействия между контейнерами. Без указания --driver используется по умолчанию)  
Также могут быть следующие вариации драйверов для --driver:  
* **host**: Использует сетевые настройки хоста, минуя изоляцию контейнеров. Это означает, что контейнер имеет доступ к сетевым ресурсам хоста.
* **overlay**: Позволяет создавать виртуальные сети, которые могут объединять контейнеры, работающие на разных хостах, для построения распределенных приложений.
* **macvlan**: Позволяет контейнерам иметь собственные MAC-адреса в сети и появляться как физические устройства в сети.
* **none**: Отключает сеть для контейнера, т.е. контейнер не будет иметь сетевого интерфейса.
* **ipvlan**: Позволяет контейнерам иметь собственные IP-адреса в сети и появляться как физические устройства в сети.  

**5. Создание сети с ограниченным доступом:**  
```docker network create --internal my_internal_network``` - эта команда создает внутреннюю сеть my_internal_network, которая ограничивает доступ к контейнерам извне.  
  
  
## DOCKERFILE  
**Инструкции в Dockerfile:**  
* ```FROM <image_name>``` - указывает на базовый образ сборки
* ```RUN <shell_command>``` - выполняет требуемую команду во время сборки docker образа. В Dockerfile может использоваться несколько инструкций RUN
* ```LABEL``` - добавляет к образу метаданные. Например ```LABEL maintainer="Your Name <your.email@example.com>"```
* ```ARG``` - определяет переменные окружения на время сборки. Например ```ARG version=latest``` (в общем случае, инструкция ARG обычно размещается в начале Dockerfile, перед инструкцией FROM)
* ```HEALTHCHECK``` - определяет команду, оценивающую состояние контейнера (выполняется после запуска контейнера. В случае успешного её завершения, контейнер будет считаться живым и готовым к работе). Например ```HEALTHCHECK --interval=30s --timeout=5s CMD curl -f http://localhost/ || exit 1```
* ```SHELL``` - устанавливает программу по умолчанию, которая будет использоваться для интерпретации строкового синтаксиса RUN, CMD. Например ```SHELL ["/bin/bash", "-c"]```
* ```WORKDIR``` - задаёт рабочую директорию для следующей инструкции. Например ```WORKDIR /app```
* ```USER``` - устанавливает имя пользователя или UID для использования сборки из образа и при запуске контейнера. Например ```USER nobody```
* ```VOLUME``` - создаёт точку монтирования для работы с постоянным хранилищем. Например ```VOLUME /data```
* ```CMD``` - устанавливает команду, которая будет выполнена при запуске контейнера. Если инструкция CMD отсутствует в Dockerfile, по умолчанию будет выполнена команда /bin/sh -c, но это поведение может быть переопределено в инструкциях ENTRYPOINT. Например ```CMD ["nginx", "-g", "daemon off;"]```
* ```ENTRYPOINT``` - устанавливает исполняемый файл или команду, которая будет выполняться при запуске контейнера. Если используется инструкция ENTRYPOINT, то инструкция CMD дополняет (а не перезаписывает) аргументы команды. Например ```ENTRYPOINT ["nginx", "-g", "daemon off;"]```, т.е. при запуске контейнера с дополнительными аргументами, например, docker ```run -it mynginx -c /path/to/nginx.conf```, аргументы ```-c /path/to/nginx.conf``` будут добавлены к команде ```nginx```
* ```COPY``` - копирует локальные файлы и директории в образ. Например ```COPY app /app```
* ```ADD``` - также как и COPY копирует, но также включает дополнительные функции, такие как извлечение файлов из URL, автоматическое распаковывание архивов. Однако для простых операций рекомендуется использовать COPY вместо ADD. Пример использования: ```ADD app.tar.gz /app```  
  
  
## DOCKER-COMPOSE  
