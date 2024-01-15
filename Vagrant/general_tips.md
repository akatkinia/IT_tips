# Ссылки
1. [Дистрибутив](https://hashicorp-releases.yandexcloud.net/vagrant)
2. [Документация по конфигурации VirtualBox в Vagrant](https://developer.hashicorp.com/vagrant/docs/providers/virtualbox/configuration)
3. [Образы проекта Bento](https://app.vagrantup.com/bento)

# Переменные окружения  
* [VAGRANT_DEFAULT_PROVIDER](https://developer.hashicorp.com/vagrant/docs/providers/default) - провайдер по умолчанию. Например, может принимать такие значения как ```virtualbox   ``` (по умолчанию) или ```vmware_desktop```.

# Команды  
* ```vagrant up``` - выполнение команды в директории с Vagrantfile запустит виртуальную машину
* ```vagrant up --debug > vagrant.log 2>&1``` - Запуск с логированием debug (stderr + stdin в файл vagrant.log)
* ```vagrant suspend``` - выключит виртуальную машину с сохранением ее состояния. Т.е. при следующем запуске будут запущены все процессы, которые работали ранее
* ```vagrant halt``` - выключит виртуальную машину штатным образом
* ```vagrant reload``` - перезапустит виртуальную машину
* ```vagrant reload --provision``` - выполнит перезагрузку и шаги провижининга (например, если были изменения в конфигурации Vagrantfile)
* ```vagrant ssh``` - подключиться к ВМ по SSH. Выполняется из каталога с Vagrantfile
* ```vagrant destroy -f``` - полное уничтожение виртуальной машины, созданной с использованием Vagrant. Эта команда прекращает работу и удаляет все следы виртуальной машины, включая все диски, сетевые интерфейсы и другие ассоциированные ресурсы
* ```vagrant status``` - покажет текущий статус виртуальной машины и некоторую информацию о ней, такую как используемый пров,айдер, имя и статус (выполнение из директории с Vagrantfile)
* ```vagrant global-status``` - выведет список машин, вместе с состоянием и с дирекорией, в которой размещён Vagrantfile (можно выполнять из любой директории)
* ```vagrant port``` - выведет список проброшенных портов
* ```vagrant box add bento/ubuntu-20.04 --provider=virtualbox --force``` - загрузить образ ОС (bento/ubuntu-20.04) для создания ВМ
* ```vagrant box list``` - посмотреть список доступных в образов в системе
