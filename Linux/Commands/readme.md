# set

Команда set в командной оболочке Unix-подобных систем используется для управления настройками и поведением самой оболочки.  
Она позволяет включать и выключать опции, контролирующие различные аспекты выполнения команд и скриптов.  
Вот некоторые из наиболее распространенных опций set и примеры их использования:

* set -e или set -o errexit:
Эта опция активирует "режим выхода при ошибке". Если команда завершается с ненулевым кодом возврата, выполнение скрипта автоматически завершается.
  
Пример:  
```
#!/bin/bash
set -e

echo "This will be printed."
nonexistent_command  # This will cause an error and terminate the script.
echo "This will NOT be printed."
```

* set -u или set -o nounset:  
Эта опция активирует "режим выхода при использовании неопределенных переменных". Если попытаться использовать переменную, которая не была определена, скрипт завершит выполнение.
  
Пример:  
```
#!/bin/bash
set -u

echo "This will be printed."
echo "Value of variable: $undefined_variable"  # This will cause an error and terminate the script.
echo "This will NOT be printed."
```  

* set -x или set -o xtrace:  
Эта опция активирует "режим трассировки". Оболочка будет выводить на экран каждую выполняемую команду перед выполнением.
  
Пример:  
```
#!/bin/bash
set -x

echo "This will be printed."
echo "This will also be printed."
```

* set -o pipefail:  
Эта опция позволяет сохранять код завершения последней команды в цепочке через пайплайн.  
  
Пример:  
```
#!/bin/bash
set -o pipefail

cat nonexistent_file | grep "pattern"  # If 'cat' fails, this will cause the script to terminate.
```