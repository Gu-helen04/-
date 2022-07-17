from reg import open_files, list_conversion, duplicate_search,file_record

if __name__ == '__main__':
    contacts_list = open_files()
    print(f'Фаил загружен')
    list_conversions = list_conversion(contacts_list)
    print('Фаил преобразован в канонический вид')
    list_without_doubles = duplicate_search(list_conversions)
    print('Дубликаты удалены')
    file_record(list_without_doubles)
    print('Новый фаил сохранен')

