
get_formatted = lambda key, title: key + ": " + title


print(get_formatted("Описание", "Программа для вывода информации"))
print(get_formatted("Версия", "1.0"))
print(get_formatted("Разработчик", "Рябцев М. П."))
print(get_formatted("Группа", "41703621"))
print(get_formatted("Дата разработки", "09.11.2022"))

input('\nНажмите <ENTER> для завершения')
