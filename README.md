<img src="https://budgetfamily.ru/static/media/logo.878f763e39bbd9badd1d83eccd3570c4.svg" alt="InCoin" width="377" height="82"/>&nbsp;

### Контроль расходов «Семейный бюджет»

Приветствуем вас в нашем pet-проекте по управлению семейным бюджетом - **InCoin**!  

**InCoin** позволяет удобно отслеживать доходы и расходы, планировать бюджет, анализировать финансовые показатели, и многое другое. Благодаря своему интуитивно понятному интерфейсу и разнообразным функциям, оно помогает пользователям принимать более осознанные финансовые решения и достигать финансовых целей.  

Это приложение разработано командой выпускников Яндекс.Практикума:
  - Project managers
    - [Георгий Кочнев](https://krasnodar.hh.ru/resume/158364e8ff0b05a3410039ed1f6b3578716a34)
    - [Дарья Серебрянская](https://cyber-dosa-d28.notion.site/3262193194414073aa6ac3aa927e7c59)
  - Backend developer
    - [Андрей Лабутин](https://github.com/agatinet31)
  - Frontend developers
    - [Маша Морева](https://github.com/MashaMoreva)
    - [Алексей Барабанов](https://github.com/VolcharaMastering)
    - [Любовь Васильева](https://github.com/Luba-web)
  - Quality Assurance (QA) engineers
    - [Александра Симонова](https://github.com/AISimonova)
    - [Гриша Наумов](https://github.com/caligulion)
    - [Надежда Володина](https://github.com/yareliance)
  - UI/UX Designers
    - [Лиза Вольская](https://t.me/balzarylovesgroove)
    - [Алиса Орлова](https://t.me/aleeseorlova)
    - [Евгения Бойко](https://t.me/justtjane)

#### Описание функциональности:

- **страница "Бюджет"**  
На главной странице пользователи могут видеть свой текущий баланс, а также визуально представленный спидометр, отражающий соотношение доходов и расходов. Встроенные градации цветов помогут быстро оценить финансовое положение - от зеленого (хорошее) до красного (нужно обратить внимание).
- **Управление расходами и доходами**  
InCoin позволяет вам учесть все ваши расходы и доходы. Вы можете быстро добавлять новые транзакции, указывая дату, категорию, сумму и другие детали. Система поддерживает удобный интерфейс и автоматический расчет баланса.
- **Управление счетами**  
Вы можете добавлять новые счета или удалять существующие.
- **Управление категориями**  
Приложение предоставляет возможность создания категорий для ваших транзакций. Вы можете определить собственные категории или использовать предустановленные. Это позволит более точно анализировать ваши финансы и увидеть, на что уходит больше всего средств.
- **Повторяющиеся расходы**  
InCoin предоставляет возможность установить повторяющиеся расходы, например, платежи за аренду или коммунальные услуги. Это упрощает учет регулярных затрат и помогает не упустить важные платежи.
- **Конверты накоплений**  
Управляйте накоплениями для достижения ваших финансовых целей с помощью функции конвертов. Создайте конверт, определите желаемую сумму, и приложение будет следить за ходом выполнения цели и эффективным использованием средств.
- **страница "Статистика"**  
Приложение предоставляет подробную статистику по доходам и расходам. Графики и диаграммы помогут вам анализировать свои финансовые показатели за разные периоды.
- **страница "Настройки профиля"**  
По клику на аватар пользователя в хедере, появляется окно с возможностью перехода в личный кабинет или выхода из приложения. В личном кабинете можно внести следующие изменения:
  - изменить аватар (для редактирования аватарки откроется дополнительное окно, позволяющее выбрать фотографию на вашем компьютере)
  - изменить данные
  - сменить пароль
  - удалить профиль
 - **страница "Помощь"**  
Здесь вы найдете ответы на наиболее часто задаваемые вопросы, которые помогут вам более эффективно использовать наше приложение
   
#### Развёртывание | Интеграция | Установка | Разработка | Запуск:

В данном разделе предоставлены подробные инструкции по подготовке окружения, развёртыванию проекта и интеграции с Docker для обеспечения более удобной и надежной разработки. Следуйте этим шагам, чтобы успешно запустить приложение.

- #### Предварительные требования:  
  - [**Poetry**](https://python-poetry.org/docs/cli/) (используется для управления зависимостями и пакетами)  
    - Установка Poetry версии 1.4.0  
      `curl -sSL https://install.python-poetry.org | python - --version 1.4.0`  
    - Добавление Poetry в переменную среды PATH  
      для Unix: `"$HOME/.local/bin"`  
      для Windows: `"%APPDATA%\Python\Scripts"`
  - [**Docker**](https://www.docker.com/) (обеспечивает создание и управление контейнерами)
  - [**Файлы requirements.txt**](https://pip.pypa.io/en/stable/user_guide/#requirements-files) (обновление зависимостей происходит автоматически через **pre-commit**)
  - [**pre-commit**](https://pre-commit.com) (при каждом коммите выполняются хуки перечисленные в  
    **.pre-commit-config.yaml**, если возникла ошибка, запустите хуки вручную: `pre-commit run --all-files`)
    
- #### Запуск проекта:
  _Backend_
    - клонирование репозитория: `git clone https://github.com/InCoinFamily/InCoin.git`
    - переход в папку проекта: `cd InCoin`
    - активация виртуального окружения: `poetry shell`
    - установка необходимых зависимостей: `poetry install`
    - миграция базы данных: `python manage.py migrate`
    - установка хуков pre-commit: `pre-commit install --all`
    - убедитесь, что при запуске используется правильное виртуальное окружение (посмотреть путь): `poetry env info --path`

  _Frontend_
    - клонирование репозитория: `git clone https://github.com/InCoinFamily/InCoin.git`
    - переход в папку проекта: `cd InCoin`
    - переход в папку разработки frontend-части: `cd frontend`
    - установка необходимых зависимостей: `npm install`
    - запуск проекта: `npm run start` (приложение будет доступно по адресу http://localhost:3000)

- #### Production Docker с Caddy:
  - перейдите в директорию infra: `cd infra`
  - создайте production env-файл: `cp .env.example .env`
  - заполните в `.env` минимум `DOMAIN`, `ACME_EMAIL`, `SECRET_KEY` и `POSTGRES_PASSWORD`
  - убедитесь, что DNS A/AAAA-запись домена указывает на сервер, а порты `80` и `443` открыты
  - соберите и запустите приложение: `docker compose up -d --build`
  - backend автоматически выполнит `migrate` и `collectstatic`, Caddy автоматически выпустит и продлит TLS-сертификат
  - для создания администратора выполните: `docker compose exec backend python manage.py createsuperuser`
  - приложение будет доступно по адресу `https://<DOMAIN>`

#### Технологии:

<img src="https://simpleicons.org/icons/git.svg" alt="git" width="50" height="50"/> <img src="https://simpleicons.org/icons/github.svg" alt="github" width="50" height="50"/> <img src="https://simpleicons.org/icons/postman.svg" alt="postman" width="50" height="50"/> <img src="https://simpleicons.org/icons/swagger.svg" alt="swagger" width="50" height="50"/> <img src="https://simpleicons.org/icons/figma.svg" alt="figma" width="50" height="50"/>
 
- _Backend_

<img src="https://simpleicons.org/icons/python.svg" alt="python" width="50" height="50"/> <img src="https://simpleicons.org/icons/django.svg" alt="django" width="50" height="50"/>
<img src="https://simpleicons.org/icons/postgresql.svg" alt="postgresql" width="50" height="50"/>  <img src="https://simpleicons.org/icons/docker.svg" alt="docker" width="50" height="50"/> <img src="https://simpleicons.org/icons/gunicorn.svg" alt="gunicorn" width="50" height="50"/> 
 
- _Frontend_
    
<img src="https://simpleicons.org/icons/javascript.svg" alt="javascript" width="50" height="50"/> <img src="https://simpleicons.org/icons/react.svg" alt="react" width="50" height="50"/> <img src="https://simpleicons.org/icons/redux.svg" alt="redux" width="50" height="50"/> <img src="https://simpleicons.org/icons/sass.svg" alt="scss" width="50" height="50"/>  <img src="https://simpleicons.org/icons/prettier.svg" alt="prettier" width="50" height="50"/> 
 

#### Не упустите шанс улучшить свои финансовые навыки с помощью InCoin!
* [Попробуйте сейчас!](https://budgetfamily.ru/)
