# Метапрограмування

**Лабораторна робота № 1:** *Примiтивний аналiз, модифiкацiя та генерацiя програмних кодiв*

## **Iнтроспектор класових iєрархiй Python** *(Варiант 2)*

+ Розробити консольну iнтерактивну утилiту для iнтроспекцiї класових iєрар-
хiй на мовi Python 3.x. Система повинна вмiти виконувати аналiз iєрархiй
та наступнi пункти:

### 1
Будувати транзитивнi ланцюги успадкування полiв та методiв мiж
усiма класами iєрархiї. Орiєнтований формат виводу:

```
----------------------------------------------------------
Transitive inheritance chains
----------------------------------------------------------
1. Start point: class1
----------------------------------------------------------
property_1: --> class11 --> class12 --> ...
property_1: --> class21 --> class22 --> ...
...
property_2: --> class11 --> class12 --> ...
...
method_1: --> class11 --> class12 --> ...
method_1: --> class21 --> class22 --> ...
...
method_2: --> class11 --> class12 --> ...
...
----------------------------------------------------------
2. Start point: class2
----------------------------------------------------------
...
----------------------------------------------------------
...
----------------------------------------------------------
n. Start point: classN
----------------------------------------------------------
...
----------------------------------------------------------
```

### 2
Виявляти перевизначенi поля та методи класiв (overriding). Орiєнто-
ваний формат виводу:

```
----------------------------------------------------------
Overrided attributes and methods
----------------------------------------------------------
1. attribute1 of class1 redefined in the class2
2. ...
----------------------------------------------------------
1. method1 of class1 redefined in the class2
2. ...
----------------------------------------------------------
```
Якщо iєрархiя не мiстить перевизначених атрибутiв та (або) методiв,
тодi використовувати формат:

```
----------------------------------------------------------
Overrided attributes and methods
----------------------------------------------------------
The hierarchy does not contain any overrided attributes
or methods.
----------------------------------------------------------
```

### 3
Визначати зв’язок мiж двома довiльними класами iєрархiї. Орiєнто-
ваний формат виводу:

```
----------------------------------------------------------
Relation between class1 and class2
----------------------------------------------------------
class1 is a superclass for class2
class1 --> ... --> class2
class2 is a superclass for class1
class2 --> ... --> class1
class1 and class2 have common superclass
class1 and class 2 have common subclass
class1 and class2 are the same class
----------------------------------------------------------
```

### 4
Визначити найбiльший спiльний пiдклас для двох довiльних класiв
iєрархiї. Орiєнтований формат виводу:

```
----------------------------------------------------------
The biggest common subclass for class1 and class2
----------------------------------------------------------
class1:
------------------------
attribute1Name
...
attributeMname
method1Name
...
methodMname
------------------------
class2:
------------------------
attribute1Name
...
attributeMname
method1Name
...
methodMname
------------------------
Biggest common subclass:
------------------------
attribute1Name
...
attributeMname
method1Name
...
methodMname
----------------------------------------------------------
```

### 5
Визначати найменший та найбiльший спiльнi суперкласи для двох до-
вiльних класiв iєрархiї. Орiєнтований формат виводу:

```
----------------------------------------------------------
The biggest common superclass for class1 and class2
----------------------------------------------------------
class1 --> ... --> BiggestCommonSpuerClass
class2 --> ... --> BiggestCommonSpuerClass
----------------------------------------------------------
----------------------------------------------------------
The least common superclass for class1 and class2
----------------------------------------------------------
class1 --> ... --> LeastCommonSpuerClass
class2 --> ... --> LeastCommonSpuerClass
----------------------------------------------------------
```

Якщо найменшого та (або) найбiльшого спiльного суперкласу не iснує,
тодi використовувати формат:

```
----------------------------------------------------------
The biggest common superclass for class1 and class2
----------------------------------------------------------
There is no biggest common superclass for class1 and
class2.
----------------------------------------------------------
----------------------------------------------------------
The least common superclass for class1 and class2
----------------------------------------------------------
There is no least common superclass for class1 and class2.
----------------------------------------------------------
```

### 6
Визначати кiлькiсть успадкованих полiв та методiв вiд кореневого
класу довiльним класом iєрархiї. Орiєнтований формат виводу:

```
----------------------------------------------------------
Attributes and methods inherited by class1 from RootClass
----------------------------------------------------------
attribute1
...
attribute1N
method1
...
methodM
----------------------------------------------------------
```

+ Реалiзувати окремi команди для виконання кожного виду аналiзу, та
команду для комплексного аналiзу пакету, який включає в себе пункти 1-6.
В якостi вхiдних даних системi може подаватися довiльна класова iєрар-
хiя на мовi *Python 3.x*. Пiсля виконання кожної з команд система повинна
виводити результати аналiзу у консоль а також формувати вiдповiдний звiт
записуючи його у вiдповiдний **.txt* файл. Iмена файлiв повиннi мiстити
назву кореневого класу iєрархiї.  
  - Орiєнтований формат для пунктiв 1-6: `rootClassNameTree_analysisType.txt`.
  - Орiєнтований формат для комплексного аналiзу: `rootClassNameTree_analysisType.txt`.
  - Утилiта повинна запускатися з командного рядка термiналу операцiйної
системи.

#### Виконанi пункти:
- [ ] [Перший](#1) 
- [ ] [Другий](#2)
- [ ] [Третiй](#3)
- [ ] [Четвертий](#4)
- [ ] [П'ятий](#5)
- [ ] [Шостий](#6)

## Мова програмування:
![logo] Python: 3.6.6

## Автор

:+1: Студент 4-го курсу КНУ iм.Шевченка **Гальченко Максим** (@maxs-im)

## Реалізація
[Private Github Repository](https://github.com/maxs-im/META)

[logo]: https://www.python.org/static/opengraph-icon-200x200.png
