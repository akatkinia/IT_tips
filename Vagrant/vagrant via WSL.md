# Для настройки vagrant на WSL  

1. Установить vagrant на WSL машине. Важно чтобы версия vagrant на WSL == версии vagrant в Windows
2. Добавить в переменные окружения:
```
export VAGRANT_WSL_ENABLE_WINDOWS_ACCESS="1"
export PATH="$PATH:/mnt/c/Windows/System32/WindowsPowerShell/v1.0"
export PATH="$PATH:/mnt/c/Windows/System32"
export PATH="$PATH:/mnt/c/Program Files/Oracle/VirtualBox"
```
3. Содержимое выше можно добавить в ```.bashrc``` и применить ```source ~/.bashrc```
4. Установить плагин **virtualbox_WSL2**: ```vagrant plugin install virtualbox_WSL2```  
  
5. Если наш Vagrantfile не в каталоге WSL, а в пределах ФС Windows:  
* Из каталога с Vagrantfile выполнить:
```
mkdir -p ~/vagrants/.project-vagrant           # Создать директорию в ФС Windows
ln -sv ~/vagrants/.project-vagrant .vagrant    # Создать символическую ссылку на созданную директорию из ФС WSL
```
* Запустить ```vagrant up``  
    
В части **п.5**, такой порядок действий необходим, так как происходит проблема с правами доступа к файлу (должно быть 0600, но в ФС Windows не поддерживает chmod). В противном случае возникнет следующая проблема:
```
The private key to connect to this box via SSH has invalid permissions
set on it. The permissions of the private key should be set to 0600, otherwise SSH will
ignore the key. Vagrant tried to do this automatically for you but failed. Please set the
permissions on the following file to 0600 and then try running this command again:

/mnt/c/Documents/DevOps/files/vagrant/.vagrant/machines/server1.devopsdomain/virtualbox/private_key

Note that this error occurs after Vagrant automatically tries to
do this for you. The likely cause of this error is a lack of filesystem
permissions or even filesystem functionality. For example, if your
Vagrant data is on a USB stick, a common case is that chmod is
not supported. The key will need to be moved to a filesystem that
supports chmod.
```
