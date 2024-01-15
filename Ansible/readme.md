# Инфо
В данном каталоге размещены примеры с уроков Ansible. Здесь могут быть заметки для уроков.
  
# Ansible-vault (урок 13)  
* ```ansible-vault create [filename]``` - создать зашифрованный текстовый файл
* ```ansible-vault view [encrypted-file]``` - посмотреть зашифрованный файл
* ```ansible-vault edit [encrypted-file]``` - отредактировать зашифрованный файл
* ```ansible-vault rekey [encrypted-file]``` - изменить пароль у зашифрованного файла
* ```ansible-vault decrypt [encrypted-file]``` - расшифровать зашифрованный файл

Пароль от плейбука 13 урока "hello"  
Для того чтобы запустить зашифрованный плейбук:  
* ```ansible-playbook [encrypted-playbook.yml] --ask-vault-pass```
* Создать файл [filename] с паролем внутри и запустить плейбук ```ansible-playbook [encrypted-playbook.yml --vault-password-file [filename]```  
  
Для шифрования не всего файла, а только определённой строчки:  
* ```ansible-vault encrypt_string```
* ```ansible-vault encrypt_string --stdin-name "My_password"```
* ```echo -n "Secret" | ansible-vault encrypt_string```
  
# Заметки
Теги используются как метки, которые присваиваются задаче. Пример:  
```
---
- name: Example playbook
  hosts: all
  tasks:
    - name: Install nginx
      package:
        name: nginx
        state: present
      tags:
        - webserver
```  
Таким образом можно выполнить плейбук только с определёнными тасками ```ansible-playbook your_playbook.yml --tags=webserver```  
Если тегов несколько, перечисляем их через запятую: ```ansible-playbook your_playbook.yml --tags=webserver,another_tag,yet_another_tag```  
Если хотим исключить выполнение задач, связанных с определенными тегами, используем параметр --skip-tags: ```ansible-playbook your_playbook.yml --skip-tags=tag_to_skip```  
  
Если же необходимо как-то выделить хост чем-то похожим на метки, необходимо использовать переменные в инвентари. Например:  
```
web:
  hosts:
    server1.netology:
      ansible_host: 127.0.0.1
      ansible_port: 22
      ansible_user: vagrant
      webserver_tag: nginx
```  
Пример с использованием условия для выполнения задачи на определенных хостах (типа с тегом, на деле переменной):  
```
---
- name: Example playbook
  hosts: web
  tasks:
    - name: Install nginx on hosts with the 'nginx' tag
      package:
        name: nginx
        state: present
      when: "'nginx' in hostvars[inventory_hostname].webserver_tag|default([])"
```  
  
Если у нас есть несколько групп, и мы хотим выполнить плейбук на хостах, которые принадлежат к нескольким группам, мы можем указать их через запятую:  
```ansible-playbook your_playbook.yml --limit group1,group2```  
Можно сократить до ключа -l или вовсе не указывать его: ```ansible-playbook your_playbook.yml group1,group2```  
  
Если у нас есть подгруппы инвентари, и мы хотим выполнить на всех хостах из подгруппы, мы также можем использовать --limit для указания подгруппы:  
```ansible-playbook your_playbook.yml --limit your_parent_group:your_subgroup```  
  
