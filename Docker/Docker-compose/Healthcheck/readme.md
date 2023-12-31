Примеры приводятся на следующем сервисе:
```
services:
  db:
    image: postgres:13-alpine
    environment:
      POSTGRES_DB: user1
      POSTGRES_USER: user1
      POSTGRES_PASSWORD: password
    volumes:
    - ./pg_data:/var/lib/postgresql/data
    - ./db/init_db_script.sql:/docker-entrypoint-initdb.d/init_db.sql
    ports:
    - "5432:5432/tcp"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user1"]
      interval: 5s
      timeout: 5s
      retries: 20
```

Когда Docker-демон обнаруживает, что проверка здоровья контейнера не успешна, можно предпринять следующие действия:
- **Логирование и уведомление:** Внутри проверки здоровья можно вставить код, который будет записывать информацию о состоянии контейнера в лог. После этого можно отправить уведомление, например, в Slack или по электронной почте, чтобы администраторы могли быстро реагировать на нездоровое состояние и принимать дополнительные меры.  
```
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U user1 || echo 'Container is unhealthy' >> /var/log/health.log"]
```

- **Попытка автоматической коррекции:** В зависимости от проблемы, вы можете добавить код, который попытается автоматически исправить ситуацию. Например, если проблема связана с базой данных, можно попытаться перезапустить базу данных или выполнить другие восстановительные действия.  
```
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U user1 || (echo 'Container is unhealthy' >> /var/log/health.log && docker restart my_container)"]
```

- **Интеграция с системами мониторинга:** При нездоровом состоянии контейнера можно автоматически передавать информацию в системы мониторинга, чтобы обеспечить быстрое реагирование.  
```
healthcheck:
  test: ["CMD-SHELL", "pg_isready -U user1 || curl -X POST -H 'Content-type: application/json' --data '{"text":"Container is unhealthy"}' https://hooks.slack.com/services/your-webhook-url"]
```

## Подробное описание параметров healthcheck в Docker Compose:
- test: Обязательный параметр, который определяет команду (или массив команд), выполняемую для проверки здоровья контейнера. Если команда возвращает успешный код завершения (0), контейнер будет считаться здоровым. В противном случае, он будет считаться нездоровым.
- interval: Параметр, определяющий интервал между проверками здоровья. По умолчанию установлено значение 30 секунд.
- timeout: Параметр, определяющий максимальное время ожидания ответа от команды проверки здоровья. По умолчанию установлено значение 30 секунд.
- retries: Параметр, определяющий количество попыток проверки здоровья. По умолчанию установлено значение 3.
- start_period: Параметр, определяющий период времени, в течение которого проверка здоровья будет отключена после старта контейнера. Это полезно, чтобы дать приложению некоторое время на инициализацию перед началом проверки здоровья. По умолчанию установлено значение 0 секунд.  


Пример использования healthcheck с указанием параметров:  
```
version: '3'
services:
  your-service:
    image: postgres:13-alpine
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U user1"]
      interval: 10s
      timeout: 5s
      retries: 3
      start_period: 20s
```
