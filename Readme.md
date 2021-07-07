# DNA
Реализуйте программу, которая идентифицирует человека на основе его ДНК, согласно образцу ниже.
```sh
$ python dna.py databases/large.csv sequences/5.txt
Lavender
```
## Подготовка

 1. Склонируйте себе этот репозиторий. Или скачайте и распакуйте.
 2. Откройте его в своей любимой IDE.

## Описание

ДНК - носитель генетической информации живых существ, используется в правосудии на протяжении десятилетий. Но как именно работает профилирование ДНК? Имея последовательность ДНК, как следователи могут определить, кому она принадлежит?

Ну, на самом деле ДНК-это просто последовательность молекул, называемых нуклеотидами, расположенных в определенной форме (двойная спираль). Каждый нуклеотид ДНК содержит одно из четырех различных оснований: аденин (A), цитозин (C), гуанин (G) или тимин (T). Каждая человеческая клетка содержит миллиарды этих нуклеотидов, расположенных в определенной последовательности. Некоторые части этой последовательности (т. е. генома) одинаковы или, по крайней мере, очень похожи почти у всех людей, но другие части последовательности имеют более высокое генетическое разнообразие и, следовательно, более различаются в популяции.

Одним из мест, где ДНК имеет тенденцию к высокому генетическому разнообразию, являются короткие тандемные повторы (STR - Short Tandem Repeats). STR - это короткая последовательность оснований ДНК, которая имеет тенденцию повторяться последовательно много раз в определенных местах внутри ДНК человека. Количество повторений любого конкретного STR сильно варьируется у разных людей. Например, у Алисы, в приведенных ниже образцах ДНК, STR `AGAT` повторяется четыре раза, в то время как у Боба один и тот же STR повторяется пять раз.

![Sample STRs](strs.png)

Использование нескольких STR, а не только одного, может повысить точность профилирования ДНК. Если вероятность того, что у двух людей одинаковое количество повторов для одного STR, составляет 5%, и аналитик рассматривает 10 разных STR, то вероятность того, что два образца ДНК совпадут чисто случайно, составляет примерно 1 из 1 квадриллиона (при условии, что все STR независимы друг от друга). Таким образом, если два образца ДНК совпадают по количеству повторов для каждого из STR, аналитик может быть вполне уверен, что они произошли от одного и того же человека. [CODIS](https://www.fbi.gov/services/laboratory/biometric-analysis/codis/codis-and-ndis-fact-sheet), база данных ДНК ФБР, использует 20 различных STR в рамках процесса профилирования ДНК.

Как может выглядеть такая база данных ДНК? Ну, в простейшей форме вы можете представить форматирование базы данных ДНК в виде CSV-файла, в котором каждая строка соответствует отдельному человеку, а каждый столбец соответствует определенному STR.

```
name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25
```
Данные в приведенном выше файле предполагают, что у Алисы где-то в ДНК последовательность `AGAT` повторяется 28 раз подряд, последовательность `AATG` повторяется 42 раза, а `TATC` повторяется 14 раз. Боб, тем временем, повторил те же три STR 17 раз, 22 раза и 19 раз соответственно. И у Чарли те же три STR повторяются 36, 18 и 25 раз соответственно.

Итак, учитывая последовательность ДНК, как вы могли бы определить, кому она принадлежит? Ну, представьте, что вы просмотрели последовательность ДНК для самой длинной непрерывной последовательности повторяющихся `AGAT` и обнаружили, что самая длинная последовательность состояла из 17 повторов. Если бы затем вы обнаружили, что самая длинная последовательность `AATG` имеет длину 22 повтора, а самая длинная последовательность `TATC` имеет длину 19 повторов, это дало бы довольно веские доказательства того, что ДНК принадлежала Бобу. Конечно, также возможно, что после того, как вы проведете подсчет для каждого из STR, он не совпадет ни с кем в вашей базе данных ДНК, и в этом случае у вас нет совпадения.

На практике, поскольку аналитики знают, на какой хромосоме и в каком месте ДНК будет найден STR, они могут сузить свой поиск (искать только на узком участке ДНК). Но мы проигнорируем эту деталь.

Ваша задача состоит в том, чтобы написать программу, которая возьмет последовательность ДНК и CSV-файл, содержащий STR данные, для списка лиц, а затем выведет, кому (скорее всего) принадлежит ДНК.

## Инструкция
В файле под названием `dna.py`, реализуйте программу, которая идентифицирует кому принадлежит последовательность ДНК.

*  Программа должна требовать в качестве своего первого аргумента командной строки имя CSV-файла, с STR данными, а также в качестве второго аргумента командной строки имя текстового файла, содержащего последовательность ДНК.
    * Если вашу программу запускают с неправильным количеством аргументов командной строки, ваша программа должна напечатать сообщение об ошибке (текст на ваше усмотрение) (`print('...')`). Если указано правильное количество аргументов, мы считаем, что первый аргумент действительно является именем CSV-файла, а второй аргумент является именем  текстового файла.
* Ваша программа должна открыть CSV-файл и прочитать его содержимое в память.
    * Мы предполагаем, что первая строка CSV-файла это имена столбцов. В первом столбце будет слово `name`, а остальные столбцы это STR последовательности.
* Ваша программа должна открыть последовательность ДНК и прочитать ее содержимое в память.
* Для каждого из STR (из первой строки CSV-файла) ваша программа должна вычислить наибольшее количество непрерывных повторов STR в последовательности ДНК.
* Если количество STR точно совпадает с кем-то из лиц в файле CSV, ваша программа должна распечатать имя соответствующего лица.
    * Вы можете предположить, что рассчитанные STR данные не будет соответствовать более чем одному человеку.
    * Если рассчитанные STR данные не совпадает точно ни с одним из лиц в файле CSV, ваша программа должна напечатать `"No match"`.

## Советы
* [Csv](https://docs.python.org/3/library/csv.html) модуль Python’а может быть полезен для чтения CSV-файлов в память. Возможно вы захотите использовать [csv.reader](https://docs.python.org/3/library/csv.html#csv.reader) или [csv.DictReader](https://docs.python.org/3/library/csv.html#csv.DictReader).
* Функции [open](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) и [read](https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects) могут быть полезными.
* [List](https://docs.python.org/3/tutorial/introduction.html#lists) или [dict](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) возможно тоже пригодятся.
* Эти советы, являются просто советами и вы можете использовать любой свой собственный подход. 
* [Дзен питона](https://tyapk.ru/blog/post/the-zen-of-python) прекрасен.

## Тестирование
Обязательно протестируйте свой код с помощью следующих тестовых данных:

* Run your program as `python dna.py databases/small.csv sequences/1.txt`. Your program should output `Bob`.
* Run your program as `python dna.py databases/small.csv sequences/2.txt`. Your program should output `No match`.
* Run your program as `python dna.py databases/small.csv sequences/3.txt`. Your program should output `No match`.
* Run your program as `python dna.py databases/small.csv sequences/4.txt`. Your program should output `Alice`.
* Run your program as `python dna.py databases/large.csv sequences/5.txt`. Your program should output `Lavender`.
* Run your program as `python dna.py databases/large.csv sequences/6.txt`. Your program should output `Luna`.
* Run your program as `python dna.py databases/large.csv sequences/7.txt`. Your program should output `Ron`.
* Run your program as `python dna.py databases/large.csv sequences/8.txt`. Your program should output `Ginny`.
* Run your program as `python dna.py databases/large.csv sequences/9.txt`. Your program should output `Draco`.
* Run your program as `python dna.py databases/large.csv sequences/10.txt`. Your program should output `Albus`.
* Run your program as `python dna.py databases/large.csv sequences/11.txt`. Your program should output `Hermione`.
* Run your program as `python dna.py databases/large.csv sequences/12.txt`. Your program should output `Lily`.
* Run your program as `python dna.py databases/large.csv sequences/13.txt`. Your program should output `No match`.
* Run your program as `python dna.py databases/large.csv sequences/14.txt`. Your program should output `Severus`.
* Run your program as `python dna.py databases/large.csv sequences/15.txt`. Your program should output `Sirius`.
* Run your program as `python dna.py databases/large.csv sequences/16.txt`. Your program should output `No match`.
* Run your program as `python dna.py databases/large.csv sequences/17.txt`. Your program should output `Harry`.
* Run your program as `python dna.py databases/large.csv sequences/18.txt`. Your program should output `No match`.
* Run your program as `python dna.py databases/large.csv sequences/19.txt`. Your program should output `Fred`.
* Run your program as `python dna.py databases/large.csv sequences/20.txt`. Your program should output `No match`.
