import sqlite3
from tkinter import *
from tkinter import messagebox

def click():
    sel = lb_name.curselection()
    if sel == tuple():
        messagebox.showerror("Ошибка", "Не выбран район.\nНажмите на любой район в списке,\nчтобы его выбрать.")
    rayon = list()
    try:
        for n in range(len(cur_list)):
            if n == lb_name.index(sel[0]):
                rayon = cur_list[n]
        messagebox.showinfo(f"Информация о районе {rayon[0]}", f'''Название: {rayon[0]}
----------------------------------
Население: {rayon[1]} человек
----------------------------------
Административный округ: {rayon[2]}
----------------------------------
Транспортная доступность:
{rayon[3]}
----------------------------------
Площадь: {rayon[4]} гектар
        ''')
    except:
        print('NO')


def sort_click():
    global sw, lb_keys, lb_values
    sw = Tk()
    sw.geometry("800x500")
    sw.resizable(False, False)
    sw.title("Сортировка")

    Label(text="Признак", master=sw, font=("Moscow Sans", 16)).place(relx=0.01,rely=0.02)
    lb_keys = Listbox(master=sw, font=("Moscow Sans", 16))

    lb_keys.insert(0, "Административный округ")
    lb_keys.insert(1, "Развитость транспорта")
    lb_keys.insert(2, "Население")
    lb_keys.insert(3, "Площадь")

    Label(text="Значения", master=sw, font=("Moscow Sans", 16)).place(relx=0.51, rely=0.02)
    lb_values = Listbox(master=sw, font=("Moscow Sans", 16))

    lb_keys.place(relx=0.01, rely=0.07,relwidth=0.45)
    lb_keys.bind("<<ListboxSelect>>", lb_keys_select)
    lb_values.place(relx=0.51, rely=0.07, relwidth=0.45)

    sorter_button = Button(text="Сортировать", master=sw, command=sort, font=("Moscow Sans", 16))
    sorter_button.place(relx=0.4,rely=0.6)

    sw.mainloop()

def sort():
    global cur_list
    try:
        if sel == 2 or sel == 3:
            db = list(cursor.execute("SELECT * FROM Rayoni"))
            l = list()
            for i in db:
                if sel == 2:
                    l.append(i[1])
                else:
                    l.append(i[4])
            l.sort(reverse=(lb_values.curselection()[0] == 1))
            cur_list.clear()
            lb_name.delete(0, "end")
            for n in range(len(l)):
                if sel == 2:
                    line = list(cursor.execute(f"SELECT * FROM Rayoni WHERE naselenie={l[n]}"))
                else:
                    line = list(cursor.execute(f"SELECT * FROM Rayoni WHERE ploshad={l[n]}"))
                lb_name.insert(n, line[0][0])
                for i in line:
                    cur_list.append(i)
        elif sel == 0:
            ao = ("ЦАО", "САО", "СВАО", "ВАО", "ЮВАО", "ЮАО", "ЮЗАО", "ЗАО", "СЗАО", "ТиНАО")
            selected = int(lb_values.curselection()[0])
            res = list(cursor.execute(f"SELECT * FROM Rayoni WHERE okrug=\"{ao[selected]}\""))
            lb_name.delete(0, "end")
            for i in range(len(res)):
                line = res[i][0]
                lb_name.insert(i,line)
            cur_list = res
        elif sel == 1:
            lines = ("①","②","③","④","⑤","⑥","⑦","⑧","⑨","⑩","⑪","⑫","⑬","⑭","⑮","D1", "D2", "Ленинградское", "Казанское", "Киевское", "Волоколамское", "Ярославское", "Павелецкое")
            selected = int(lb_values.curselection()[0])
            res = list(cursor.execute(f"SELECT * FROM Rayoni WHERE transport LIKE \"%{lines[selected]}%\""))
            lb_name.delete(0, "end")
            for i in range(len(res)):
                line = res[i][0]
                lb_name.insert(i,line)
            cur_list = res
        messagebox.showinfo("Успех", "Сортировка успешно завершена.")
    except NameError:
        messagebox.showerror("Ошибка", "Не указаны критерии сортировки.")
    except:
        messagebox.showerror("Ошибка", "Во время сортировки произошла ошибка.")

def lb_keys_select(*args):
    global sel
    try:
        sel = lb_keys.curselection()[0]
        lb_values.delete(0, "end")
        if sel == 0:
            lb_values.insert(0, "ЦАО")
            lb_values.insert(1, "САО")
            lb_values.insert(2, "СВАО")
            lb_values.insert(3, "ВАО") 
            lb_values.insert(4, "ЮВАО")
            lb_values.insert(5, "ЮАО")
            lb_values.insert(6, "ЮЗАО")
            lb_values.insert(7, "ЗАО")
            lb_values.insert(8, "СЗАО")
            lb_values.insert(9, "ТиНАО")
        elif sel == 1:
            lb_values.insert(0, "①Сокольническая линия")
            lb_values.insert(1, "②Замоскворецкая линия")
            lb_values.insert(2, "③Арбатско-Покровская линия")
            lb_values.insert(3, "④Филёвская линия")
            lb_values.insert(4, "⑤Кольцевая линия")
            lb_values.insert(5, "⑥Калужско-Рижская линия")
            lb_values.insert(6, "⑦Таганско-Краснопресненская линия")
            lb_values.insert(7, "⑧Калиниская и Солнцевская линии")
            lb_values.insert(8, "⑨Серпуховско-Тимирязевская линия")
            lb_values.insert(9, "⑩Люблинско-Дмитровская линия")
            lb_values.insert(10, "⑪Большая Кольцевая линия")
            lb_values.insert(11, "⑫Бутовская линия")
            lb_values.insert(12, "⑬Монорельс")
            lb_values.insert(13, "⑭МЦК")
            lb_values.insert(14, "⑮Некрасовская линия")
            lb_values.insert(15, "D1 / Белорусско-Савёловский")
            lb_values.insert(16, "D2 / Курско-Рижский")
            lb_values.insert(17, "Ленинградское направление МЖД")
            lb_values.insert(18, "Казанское направление МЖД")
            lb_values.insert(19, "Киевское направление МЖД")
            lb_values.insert(20, "Волоколамское направление МЖД")
            lb_values.insert(21, "Ярославское направление МЖД")
            lb_values.insert(22, "Павелецкое направление МЖД")
        elif (sel == 2) or (sel == 3):
            lb_values.insert(0, "По возрастанию")
            lb_values.insert(1, "По убыванию")
    except:
        print("ERROR")



line = ""

connection = sqlite3.connect('districts.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Rayoni
(
    imya TEXT,
    naselenie INT,
    okrug TEXT,
    transport TEXT,
    ploshad INT
)''')

cur_list = list()

rayoni = [
    ('Академический', 110161, 'ЮЗАО', 'Метро ⑥Академическая, ⑥Профсоюзная\n4 трамвайных маршрутов\n31 автобусный маршрут', 557),
    ('Алексеевский', 79193, 'СВАО', 'Метро ⑥ВДНХ, ⑥Алексеевская\n2 трамвайного маршрута\n24 автобусных маршрутов', 529),
    ('Алтуфьевский', 57361, 'СВАО', 'D1 Бескудниково\n13 автобусных маршрутов', 325),
    ('Арбат', 35796, 'ЦАО', 'Метро ①Библиотека им. Ленина, ③④Арбатская, ③④Смоленская, ④Александровский сад, ⑨Боровицкая\n23 автобусных маршрута', 211),
    ('Аэропорт', 79283, 'САО', 'Метро ②Динамо, ②Аэропорт, ②Сокол, ⑪Петровский парк\nD2 Красный Балтиец\n24 автобусных маршрута', 458),
    ('Бабушкинский', 88092, 'СВАО', 'Метро ⑥Бабушкинская\nТрамвайный маршрут 17\n25 автобусных маршрутов', 507),
    ('Басманный', 110928, 'ЦАО', 'Метро ①Красные Ворота, ①Чистые пруды, ①Лубянка, ③Бауманская, ③⑤Курская, ⑥⑦Китай-город, ⑩Чкаловская, ⑮Электрозаводская\nD2 Курский вокзал\n12 трамвайных маршрутов\n12 автобусных маршрутов', 837),
    ('Беговой', 41991, 'САО', 'D1 Белорусская\n21 автобусный маршрут', 556),
    ('Бескудниковский', 78567, 'САО', 'Метро ⑩Верхние Лихоборы, ⑩Селигерская, ⑩⑭Окружная\n28 автобусных маршрутов', 330),
    ('Бибирево', 158939, 'СВАО', 'Метро ⑨Алтуфьево, ⑨Бибирево\n29 автобусных маршрутов', 645),
    ('Бирюлёво Восточное', 152843, 'ЮАО', 'Метро ②Царицыно, ②Кантемировская, ⑨Пражская\nD2 Царицыно, Бирюлёво-Товарная и Бирюлёво-Пассажирская (Павелецкое направление МЖД)\n22 автобусных маршрута', 148),
    ('Бирюлёво Западное', 87787, 'ЮАО', 'D2 Покровское, D2 Красный Строитель, Бирюлёво-Товарная и Бирюлёво-Пассажирская (Павелецкое направление МЖД)\n9 автобусных маршрутов', 851),
    ('Богородское', 110049, 'ВАО', 'Метро ①Преображенская площадь, ①⑭Бульвар Рокоссовского, ⑭Белокаменная\n9 трамвайных маршрутов\n9 автобусных маршрутов\nст. Яуза (Ярославское направление МЖД)', 102),
    ('Братеево', 108582, 'ЮАО', 'Метро ②Алма-Атинская, ⑩Борисово\nПричал Братеево\n18 автобусных маршрутов', 763),
    ('Бутырский', 70597, 'СВАО', 'Метро ⑨⑪Савёловская, ⑨Дмитровская, ⑨Тимирязевская, ⑩Фонвизинская, ⑩Бутырская, ⑬Тимирязевская, ⑬Улица Милашенкова\nD1 Савёловская, D1 Тимирязевская\n18 автобусных маршрутов', 504),
    ('Вешняки', 120953, 'ВАО', 'Метро ⑦Выхино\nпл. Плющево, Вешняки, Выхино (Казанское направление МЖД), пл. Кусково, Новогиреево (Горьковское направление МЖД)', 107),
    ('Внуково', 24687, 'ЗАО', 'Метро ①Саларьево, ①Румянцево, ⑧Рассказовка, ⑧Новопеределкино\nТолстопальцево, пл. Аэропорт (Киевское направление МЖД)\n13 автобусных маршрутов', 169),
    ('Войковский', 70499, 'САО', 'Метро ②⑭Войковская, ②Водный стадионn\n4 трамвайных маршрута\n17 автобусных маршрутов', 661),
    ('Восточное Дегунино', 98046, 'САО', 'D1 Бескудниково, D1 Дегунино, D1 Лианозово\n17 автобусных маршрутов', 377),
    ('Восточное Измайлово', 77314, 'ВАО', '3 трамвайных маршрута\n18 автобусных маршрутов', 385),
    ('Восточный', 13503, 'ВАО', 'Нет', 320),
    ('Выхино-Жулебино', 225043, 'ЮВАО', 'Метро ⑦Выхино, ⑦Лермонтовский проспект, ⑦Жулебино, ⑦Котельники, ⑮Юго-Восточная, ⑮Косино\nпл. Выхино, Косино, Ухтомская (Казанское направление МЖД)\n29 автобусных маршрутов', 1497),
    ('Гагаринский', 81420, 'ЮЗАО', 'Метро ①Университет, ①Воробьёвы горы, ⑥Ленинский проспект, ⑭Площадь Гагарина', 550),
    ('Головинский', 102722, 'САО', 'Метро ②Водный стадион, ⑭Лихоборы\n23 автобусных маршрута', 893),
    ('Гольяново', 161126, 'ВАО', 'Метро ③Щёлковская, ⑭Локомотив\n25 автобусных маршрутов', 1499),
    ('Даниловский', 94232, 'ЮАО', 'Метро ②⑭Автозаводская, ②Технопарк, ⑨Тульская, ⑭ЗИЛ\nпл. Москва-Товарная-Павелецкая, Тульская (Павелецкое направление МЖД)\n8 трамвайных маршрутов\n35 автобусных маршрутов', 1259),
    ('Дмитровский', 92656, 'САО', 'D1 Марк', 729),
    ('Донской', 50460, 'ЮАО', 'Метро ⑥Шаболовская, ⑥Ленинский проспект, ⑭Верхние Котлы, ⑭Крымская\n9 трамвайных маршрутов\n24 автобусных маршрутов', 573),
    ('Дорогомилово', 75105, 'ЗАО', 'Метро ③④⑤Киевская, ③⑧Парк Победы, ④Студенческая, ④⑭Кутузовская, ⑧Минская\nD1 Фили, Киевский вокзал\n28 автобусных маршрутов', 793),
    ('Замоскворечье', 58665, 'ЦАО', 'Метро ②Новокузнецкая, ②⑤Павелецкая, ⑤Добрынинская, ⑥⑧Третьяковская, ⑨Серпуховская\nПавелецкий вокзал\n5 трамвайных маршрутов\n16 автобусных маршрутов', 432)
]


for n in rayoni:
    if n not in list(cursor.execute('SELECT * FROM Rayoni')):
        cursor.execute(f'INSERT INTO Rayoni VALUES (?, ?, ?, ?, ?)', n)
        connection.commit()
        print('Добавлено')
    else:
        print(f'{n} уже добавлен в базу данных')

tk = Tk()
tk.title("Районы")
tk.geometry("800x600")
tk.resizable(False, False)
lb_name = Listbox(font=("Moscow Sans", 24))
get_button =  Button(text="Выбрать", command=click, font=("Moscow Sans", 20))
sort_button = Button(text="Сортировать по...", command=sort_click, font=("Moscow Sans",20))

for n in range(len(list(cursor.execute("SELECT * FROM Rayoni")))):
    line = list(cursor.execute("SELECT * FROM Rayoni"))[n]
    cur_list.append(tuple(cursor.execute("SELECT * FROM Rayoni"))[n])
    lb_name.insert(n,line[0])
print(cur_list)

Label(text="Названия",font=("Moscow Sans", 24)).place(relx=0.001, rely=0.001)
lb_name.place(relx=0.001,rely=0.101,relheight=0.8)
get_button.place(relx=0.65, rely=0.25)
sort_button.place(relx=0.575,rely=0.50)

tk.mainloop()
