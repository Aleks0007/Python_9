import model
import view


def start():
    while True:
        pb = model.get_phone_book()
        choise = view.main_menu()
        match choise:
            case 1:
                model.open_file()
                view.show_message('Файл успешно открыт')
            case 2:
                model.save_file()
                view.show_message('Файл успешно сохранён')
            case 3:
                view.show_contacts(pb, 'Телефонная книга пуста или не открыта')
            case 4:
                model.add_contact(view.add_contact())
            case 5:
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите порядковый номер изменяемого контакта: ')
                    contact = view.change_contact(pb, index)
                    model.change_contact(contact, index)
                    view.show_message(f'Контакт {model.get_phone_book()[index - 1].get("name")} успешно изменён!')
            case 6:
                search = view.input_search('Введите известные данные для поиска: ')
                result = model.find_contact(search)
                view.show_contacts(result, 'Контакты не найдены')
            case 7:
                if view.show_contacts(pb, 'Телефонная книга пуста или не открыта'):
                    index = view.input_index('Введите порядковый номер удаляемого контакта: ')
                    contact = pb[index-1]
                    if contact in pb:
                        pb.remove(contact)
                        view.show_message(f'Контакт {contact.get("name")} успешно удален!')
                    else:
                        view.show_message('Такого контакта не существует!')
            case 8:
                return