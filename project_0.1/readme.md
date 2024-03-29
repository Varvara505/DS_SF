# Проект 0.1. Угадай число!

## Оглавление

[1. Описание проекта](https://github.com/Varvara505/DS_SF/tree/main/project_0.1/readme.md#Описание-проекта)

[2. Какой кейс решаем?](https://github.com/Varvara505/DS_SF/tree/main/project_0.1/readme.md#Какой-кейс-решаем?)

[3. Краткая информация о данных](https://github.com/Varvara505/DS_SF/tree/main/project_0.1/readme.md#Краткая-информация-о-данных)

[4. Результат](https://github.com/Varvara505/DS_SF/tree/main/project_0.1/readme.md#Результат)

[5. Выводы](https://github.com/Varvara505/DS_SF/tree/main/project_0.1/readme.md#Выводы)

### Описание проекта 
Угадать загаданное компьютером число за минимальное число попыток.

:arrow_up: [к оглавлению](https://github.com/Varvara505/DS_SF/tree/main/project_0.1/readme.md#Описание-проекта)

### Какой кейс решаем?

Нужно написать программу, которая угадывает число за минимальное число попыток.

**Условия соревнования**
- компьютер загадывает целое число от 1 до 100, и нам нужно его угадать. Под "угадать" подразумевается "написать программу, которая угадывает число".
- алгоритм учитывает информацию о том, больше ли случайное число или меньше нужного нам.
- Необходимо добиться того, чтобы программа угадывала число меньше, чем за 20 попыток.

**Метрика качества** 

Результаты оцениваются по среднему количеству попыток при 1000 повторений. Необходимо добиться минимального количества попыток.

**Что практикуем**

- Учимся писать хороший код на Python.
- Учимся работать с IDE.
- Учимся работать с GitHub.

:arrow_up: [к оглавлению](https://github.com/Varvara505/DS_SF/tree/main/project_0.1/readme.md#Какой-кейс-решаем?)

### Краткая информация о данных

1. Импортируем библиотеку, которая для генерации случайных чисел.

2. Имея отсортированный массив (от 1 до 100), для получения минимального количества попыток будем использовать двоичный поиск.

> Двоичный (бинарный) поиск (также известен как метод деления пополам или дихотомия) — классический алгоритм поиска элемента в отсортированном массиве (векторе), использующий дробление массива на половины.

3. Далее, напишем функцию, которая принимает на вход загаданное число и возвращает число попыток угадывания.
4. Оценим качество алгоритма с помощью ранее использованной функции для определения среднего количества попыток за 1000 подходов.

:arrow_up: [к оглавлению](https://github.com/Varvara505/DS_SF/tree/main/project_0.1/readme.md#Краткая-информация-о-данных)

### Результат

Используя бинарный поиск [в функции](https://github.com/Varvara505/DS_SF/blob/main/project_0.1/guess_the_number.p) мы максимально сократим количество попыток. 

А также - при оценке алгоритма среднее число меньше 20.

:arrow_up: [к оглавлению](https://github.com/Varvara505/DS_SF/tree/main/project_0.1/readme.md#Результат)

### Выводы

Хороший курс и конкурсы интересные.

:arrow_up: [к оглавлению](https://github.com/Varvara505/DS_SF/tree/main/project_0.1/readme.md#Выводы)