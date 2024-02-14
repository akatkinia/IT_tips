# Типы операторов в SQL
Делятся на несколько групп:
* Операторы определения данных
* Операторы манипулирования данными
* Операторы доступа к данным
* Операторы управления транзакциями
  
Все последующие примеры будут использоваться в реляционной БД PostgreSQL.  

## Операторы определения данных и Операторы манипулирования данными
* ```CREATE database sql01;``` - создание БД sql01
* ```DROP DATABASE sql01;``` - удалить БД sql01
* ```\l+``` - вывод подробной (если ввести с '+') информации о базах данных, доступных на текущем сервере PostgreSQL
* ```\dn+``` - просмотр всех схем в текущей базе данных
* ```\c sql01``` - переключиться на БД sql01 (можно также использовать ```\connect sql01```)
* ```SELECT current_database();``` - узнать текущую базу данных, с которой вы работаете в интерактивной оболочке PostgreSQL. Также можно написать просто ```\c``` и получить информацию о той БД, к которой мы сейчас подключены.
* Пример создания таблицы users, если она ещё не существует. В таблице столбцы: id (является серией, т.е. при добавлении новой записи будет автоматически увеличиваться значение). Также этот столбец определён как PRIMARY, т.е. первичным ключом, что означает, что каждое значение в этом столбце должно быть уникальным. Столбец nickname типа varchar, который может хранить строковые значения длиной до 200 символов и с определением NOT NULL, что указывает, что для каждой записи обязательно должно быть значение в данном столбце. И столбец pass аналогичный столбцу nickname по своим свойствам:  
```sql
CREATE TABLE IF NOT EXISTS users (
    id   serial PRIMARY KEY,
    nickname   varchar(200) NOT NULL,
    pass   varchar(200) NOT NULL
    );
```  
* ```\dt+``` - это команда для вывода списка всех таблиц в текущей базе данных. Это аналогично выполнению SQL-запроса ```SELECT table_name FROM information_schema.tables WHERE table_schema='public';```
* Пример заполнения созданной таблицы users данными:  
```sql
INSERT INTO
  users (nickname, pass)
VALUES
  ('john1', 'password1'),
  ('mike2', 'password2'),
  ('steven3', 'password3'),
  ('peter4', 'password4');
```  
* ```CREATE INDEX idx_users_id ON users USING btree (id);``` - создает индекс с именем **idx_users_id** на столбце **id** (там может быть список столбцов, но в данном примере один столбец) таблицы **users**, используя B-дерево (B-tree) в качестве метода индексации (один из наиболее распространенных методов индексации в PostgreSQL. Он обеспечивает эффективный поиск, сортировку и слияние данных). Таким образом, данный запрос создает индекс на столбце id таблицы users, что позволит ускорить выполнение запросов, которые используют условия фильтрации или сортировки по этому столбцу.
* ```SELECT * FROM pg_indexes WHERE schemaname = 'public';``` - посмотреть созданные индексы
* ```DROP INDEX имя_индекса;``` - удалить индекс
* ```ALTER DATABASE sql01 RENAME TO auth01;``` - переименование БД sql01 в auth01
* ```ALTER TABLE users RENAME TO users01;``` - переименование таблицы users в users01
* ```ALTER TABLE users01 ADD COLUMN phone VARCHAR(200);``` - изменение существующей таблицы auth01 добавлением в неё колонки phone
* ```COMMENT ON TABLE имя_схемы.имя_таблицы IS 'Ваше описание';``` - добавить описание к таблице (когда выводим \dt+)
* ```ALTER USER postgres PASSWORD 'новый_пароль';``` - установить пароль для пользователя postgres (по умолчанию не назначен)
* ```psql -U postgres -w 'пароль'``` - подключиться к БД postgres под пользователем postgres (с указанием пароля). Если же указать -W то будет затребован пароль
* ```psql -U postgres -d auth01``` - подключиться к БД auth01
* ```SELECT * FROM users01 LIMIT 1;``` - выборка данных из таблицы users01 с ограничением результата до одной строки
* ```UPDATE users01 SET nickname='test2' WHERE id=2;``` - выполняет обновление данных в таблице "users01". Он изменяет значение столбца "nickname" на "test2" для той строки, у которой значение столбца "id" равно 2
* ```DELETE FROM users01 WHERE id=2;``` - удаляет строку из таблицы "users01", где значение столбца "id" равно 2  

## Операторы доступа к данным
* ```CREATE ROLE test_user LOGIN PASSWORD 'password';``` - создает новую роль (пользователя) в базе данных с именем "test_user". Опция ```LOGIN``` указывает, что этот пользователь может входить в систему базы данных. Опция ```PASSWORD``` устанавливает пароль 'password' для этого пользователя. Таким образом, после выполнения этой команды будет создан новый пользователь "test_user" с паролем "password", который сможет входить в систему базы данных. По умолчанию, при создании нового пользователя или роли в PostgreSQL, ему не назначаются какие-либо специфические права. Новый пользователь создается без каких-либо привилегий, кроме базовых прав, необходимых для входа в систему базы данных.
* ```GRANT SELECT ON TABLE users01 TO test_user;``` - предоставляет право на выполнение операции SELECT для таблицы "users01" пользователю "test_user".
* Чтобы посмотреть гранты, предоставленные определенному пользователю, вы можете выполнить следующий запрос к системной таблице information_schema.table_privileges:  
```sql
SELECT grantee, table_schema, table_name, privilege_type
FROM information_schema.table_privileges
WHERE grantee = 'имя_пользователя';
```
* ```REVOKE SELECT ON TABLE users01 FROM test_user;``` - отзывает право на выполнение операции SELECT для таблицы "users01" у пользователя "test_user"
* ```REVOKE ALL PRIVILEGES ON ALL TABLES IN SCHEMA public FROM test_user;``` - отзывает все предоставленные ранее привилегии для пользователя "test_user" на все таблицы в схеме "public"
* ```SET ROLE test_user;``` - установка роли пользователя. В нашем случае, команда устанавливает текущую роль пользователя в test_user. Это позволяет временно перейти к другой роли с правами доступа, определенными для этой роли
* ```RESET ROLE;``` - вернуться к предыдущей роли или сбросить текущую роль и вернуться к роли, которая была активной до установки новой роли
* ```SELECT current_user;``` - узнать текущую роль можно обратившись к системной переменной current_user  
  
## Операторы управления транзакциями
**Операторы управления транзакциями** - это специальные команды или инструкции, которые позволяют контролировать начало, завершение и состояние транзакций в базе данных.  
**Транзакция** - это логическая единица работы, которая состоит из одного или нескольких SQL операторов, образующих логическую последовательность действий. Транзакции обычно используются для обеспечения целостности данных в базе данных и атомарности операций (все операции в транзакции успешно завершаются и вносят свои изменения в базу данных, либо ни одна из них не выполняется в случае возникновения ошибки).  
  
**Транзакция** - набор последовательных операций над БД, представляющих логическую единицу.  
  
**Оысновные операторы управления транзакциями включают:**
* ```BEGIN``` (или ```START TRANSACTION```) -- Этот оператор начинает новую транзакцию. Все последующие операции, выполненные в рамках этой транзакции, будут рассматриваться как часть той же транзакции, пока транзакция не будет завершена с помощью ```COMMIT``` или ```ROLLBACK```
* ```COMMIT``` - Этот оператор завершает транзакцию и сохраняет все изменения, сделанные в рамках этой транзакции
* ```ROLLBACK``` - Этот оператор отменяет все изменения, сделанные в рамках текущей транзакции, и возвращает базу данных к состоянию, предшествующему началу транзакции
* ```SAVEPOINT <имя точки>``` - Этот оператор устанавливает точку сохранения внутри транзакции, что позволяет частично откатывать изменения, сделанные после этой точки, без отката всей транзакции  
* ```ROLLBACK TO SAVEPOINT my_savepoint;``` - Откат до сохранённой точки
  
Транзакции обеспечивают атомарность, целостность и изолированность операций в базе данных, что означает, что либо все операции в транзакции будут успешно завершены и внесены в базу данных, либо ни одна из них не будет выполнена.  
  
**Пример:**  
```sql
BEGIN;
UPDATE users01 SET nickname='nick3' WHERE id=3;  
```  
  
# Первичные и внешние ключи  
Ключи - это некие сущности, созданные для установления определённых ограничений, которые поддерживают целостность и доступность данных в таблицах баз данных.  
Ключи могут быть первичными и внешними:  
* **Первичный ключ**, или **primary key**, означает, что в таблице значение колонки primary key не может повторяться.
* **Внешний ключ**, или **foreign key**, устанавливает взаимосвязь между данными в разных таблицах. Для foreign key существует несколько способов связывания таблиц:
  * Один к одному
  * Один ко многим
  * Многие ко многим

# Индексы  
**Индексы** - это специальные структуры в базах данных, которые позволяют ускорить поиск и сортировку по определённому полю или набору полей в таблице, а также используются для обеспечения уникальности данных.  
  
## Общие принципы, связанные с созданием индексов
* Индексы необходимо создавать для столбцов, которые используются в JOIN-операциях, по которым часто производятся поиск и операции сортировки
* Для столбцов, на которые наложено ограничение уникальности, индекс создаётся в автоматическом режиме
* Индексы лучше создавать для тех столбцов, в которых минимальное число повторяющихся значений и данные распределены равномерно
* При внесении изменений в таблицы автоматически изменяются и индексы, наложенные на эту таблицу
  
**Индексы делятся на две подгруппы:**
* Кластерные
* Некластерные  
  
Большинство современных СУБД поддерживает несколько полезных алгоритмов индексации.
* **Индексы в B-деревьях**, такие как INDEX, FULLTEXT, PRIMARY KEY и UNIQUE
* **Индексы в R-деревьях**, например индексы для пространственных типов данных
* **Хеш-индексы и инвертированные списки** при использовании индексов FULLTEXT
  
# EXPLAIN
С помощью оператора EXPLAIN мы можем выполнить анализ SQL-запроса и посмотреть план его выполнения. По результатам анализа данного плана мы можем понять, требуется ли построить дополнительные индексы, для того чтобы ускорить производительность данного запроса.  
Таким образом, данный оператор предоставляет полную информацию выполнения запроса.  
  
Пример: ```EXPLAIN SELECT * FROM <table_name>```  
  
**Описание параметров вывода: пример для MySQL:**
| Параметр       | Значение                                                                                      |
|----------------|-----------------------------------------------------------------------------------------------|
| id             | Порядковый номер для каждого SELECT внутри запроса (когда имеется несколько подзапросов)    |
| select_type    | Тип запроса SELECT                                                                            |
| table          | Таблица, к которой относится выводимая строка                                                 |
| type           | Тип связи используемых таблиц                                                                 |
| possible_keys  | Индексы, которые могут быть использованы для нахождения строк в таблице                        |
| key            | Использованный индекс                                                                         |
| key_len        | Длина индекса                                                                                 |
| ref            | Столбцы или константы, которые сравниваются с индексом, указанным в поле key                  |
| rows           | Число записей, обработанных для получения выходных данных                                      |
| Extra          | Содержит дополнительную информацию, относящуюся к плану выполнения запроса                    |
  
# Транзакции
О том, что такое транзакции описано ранее в разделе **Операторы управления транзакциями**.
  
**Базовые типы блокировок (Транзакции в MySQL):**
* **shared lock** - позволяет читать, но не позволяет изменять данные и ставить exclusive lock
* **exclusive lock** - запрещает другим тразакциям блокировать строку, а также может блокировать её на запись и на чтение в зависимости от уровня изоляции  
  
## Уровни изоляции в транзакции
Поддерживаемые типы изоляции в MySQL:
* **Read uncommited** — чтение незафиксированных данных
  * В этом уровне изоляции транзакция может видеть изменения, сделанные другими транзакциями, даже если они еще не зафиксированы.
  * Это самый низкий уровень изоляции и он не гарантирует согласованности данных.
  * Могут возникнуть аномалии, такие как грязное чтение, неповторяющееся чтение и фантомное чтение.
* **Read committed** — чтение зафиксированных данных
  * Этот уровень изоляции гарантирует, что транзакция видит только те данные, которые были зафиксированы до момента начала чтения.
  * Исключаются аномалии грязного чтения, но могут по-прежнему возникать неповторяющееся чтение и фантомное чтение.
* **Repeatable read** — повторяемое чтение (используется по умолчанию)
  * В этом уровне изоляции гарантируется, что все данные, прочитанные в рамках транзакции, останутся неизменными на протяжении всей транзакции.
  * Это предотвращает неповторяющееся чтение, так как данные не изменяются для данной транзакции, но все еще допускается фантомное чтение.
  * В MySQL по умолчанию используется уровень изоляции REPEATABLE READ.
* **Serializable** — сериализуемость
  * Этот уровень изоляции обеспечивает самый высокий уровень изоляции.
  * Гарантируется, что параллельные транзакции производят такие же результаты, как если бы они выполнялись последовательно (как будто не параллельно).
  * Предотвращает фантомное чтение и другие аномалии, обеспечивая полную изоляцию транзакций.
  * Однако это может привести к блокировкам и ухудшению производительности в случае большого количества параллельных транзакций.  
  
Выбор уровня изоляции зависит от конкретных требований к целостности данных и производительности приложения.  
  
# Репликации
**Репликация** - это процесс копирования и распространения данных с одной базы данных на другую. Она позволяет создавать копии данных из исходной (мастер) базы данных на одну или несколько целевых (слейв) баз данных. Репликация широко используется для распределения нагрузки на чтение, повышения отказоустойчивости и обеспечения более высокой доступности данных.  
  
**Распространенные виды репликации:**
* Репликация master-slave (мастер-слейв):
  * В этом типе репликации одна база данных (мастер) является основным источником данных, а другие базы данных (слейвы) содержат копии данных из мастер базы данных.
  * Мастер база данных принимает все записи и обновления данных, а слейвы реплицируют эти изменения от мастера.
  * Чтение данных может происходить как с мастера, так и с любого из слейвов, что позволяет распределять нагрузку на чтение.
* Мульти-мастер репликация (multi-master):
  * В мульти-мастер репликации каждая база данных может выступать в качестве мастера и принимать записи и обновления данных.
  * Это позволяет распределить нагрузку на запись между несколькими узлами и обеспечить более высокую отказоустойчивость.
  * Однако, у мульти-мастер репликации могут возникнуть конфликты записей, которые требуют дополнительных механизмов разрешения.
* Две мастер базы данных, много слейвов (two masters many slaves):
  * Этот тип репликации подобен мульти-мастер репликации, но имеет две мастер базы данных вместо нескольких.
  * Каждый мастер базы данных принимает записи и обновления данных и реплицирует их на многочисленные слейвы.
  * Это помогает распределить нагрузку на запись между двумя мастерами и обеспечить отказоустойчивость.

Выбор типа репликации зависит от конкретных требований к производительности, отказоустойчивости и консистентности данных в приложении или системе баз данных.  
  
**Также следует помнить о split-brain** - это ситуация, когда в распределенной системе или кластере каждый из узлов считает себя единственным активным и потерял связь с другими узлами. В результате возникает разделение кластера на две или более независимых групп, каждая из которых продолжает работать независимо от других.  
Эта проблема особенно критична в системах с репликацией данных, где наличие нескольких копий данных может привести к их расхождению и потере целостности. Например, в системах баз данных с мастер-мастер репликацией, если происходит split-brain, обе части кластера могут продолжать принимать записи, что приведет к конфликтам данных и потере согласованности.
Существуют различные стратегии и механизмы обнаружения и решения split-brain:  
* Механизмы обнаружения split-brain: Каждый узел в кластере может периодически проверять доступность других узлов и обнаруживать, если он потерял связь с ними. Также могут быть использованы механизмы голосования или "более чем половина" для определения состояния кластера.
* Механизмы решения split-brain: Когда сплит-мозг обнаружен, система должна принять меры для восстановления единства кластера. Это может включать в себя выбор "победителя" среди активных узлов или временное отключение всех узлов, чтобы избежать дальнейших изменений данных.
* Изоляция split-brain: Некоторые системы могут автоматически изолировать узлы, которые не могут связаться с большинством других узлов, чтобы предотвратить распространение проблемы на другие части кластера.  
  
Решение split-brain является критически важной частью разработки и настройки распределенных систем, особенно в системах с высокими требованиями к доступности и согласованности данных.  
  