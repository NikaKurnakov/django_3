# Взламываем электронный дневник!

Этот проект предназначен для обучения работы с `django shell` и работы с файлом `models.py`.

### Функции проекта

Открыв файл `scripts.py`, вы можете увидеть две функции, которые помогут вам в некоторых хакерских делах с электронным дневником. Первая функция `fix_marks` поможет вам исправить неудовлетворяющие вас оценки на желаемые. Вторая функция `create_commendation` поможет вам создать похвалу по предмету, который вам хочется.

### Функция fix_marks

Для запуска этой функции вам надо сначала запустить `django shell` в терминале. После надо сделать import всех используемых моделей из файла `models.py`:

```
from datacenter.models import Schoolkid
from datacenter.models import Mark
```

После вставляете всю функцию в shell и вызываете ее, написав ее название и в скобках имя и фамилию человека, которому хотите исправить оценки. 

```
fix_marks("имя_фамилия_ребенка")
```

Придется немного подождать, когда оценки изменятся, так как у человека может быть много неудовлетворяющих оценок.

### Функция create_commendation

Так же для запуска этой функции вам надо запустить `django shell` в терминале или использовать уже ранее запущенный. Надо сделать import недостоющих моделей:

```
from datacenter.models import Subject
from datacenter.models import Teacher
from datacenter.models import Commendation
```

После так же ее добавляете в shell. В этой функции при вызове надо указать имя и фамилию ребенка, название предмета, имя и фамилию учителя.

```
create_commendation("имя_фамилия_ребенка", "предмет", "имя_фамилия_учителя")
```

Обновляете страницу и все получается!

### Запуск django shell

Открыть shell мы можете написав это в терминал приложения, в котором мы делаете этот урок. Это для Windows:

```
python manage.py shell
```

Это пример запуска для Linux:

```
py manage.py shell
```

### Зависимости

Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для 
установки зависимостей:

```
pip install -r requirements.txt
```
