import allure

from data.urls import Urls

urls = Urls()


@allure.epic('Банковское приложение')
@allure.feature('Аккаунт менеджера банка')
@allure.story('Удаление пользователя')
@allure.severity(allure.severity_level.NORMAL)
def test_delete_customer(pages, create_user):
    man_page = pages.manager
    cust_page = pages.cust_page
    user_data = create_user
    man_page.open(urls.APP_LOGIN_PAGE)

    with allure.step('1. Переход в интерфейс Bank Manager Login'):
        try:
            man_page.click_manager_login_button()
        except Exception as e:
            raise Exception(f'Не удалось перейти в интерфейс Bank Manager Login. Ошибка: {e}')

    with allure.step('2. Нажатие кнопки "Customers"'):
        try:
            man_page.open_customers_list_button()
            man_page.await_for_js_reaction()
            assert cust_page.get_current_url() == urls.APP_CUSTOMERS_LIST_PAGE, \
                'Неверный url страницы Customers'
        except Exception as e:
            raise Exception(f'Не удалось нажать кнопку "Customers". Ошибка: {e}')

    with allure.step('3. Поиск созданного пользователя'):
        cust_page.fill_search_field(user_data['first_name'])
        customers_first_names = cust_page.get_name_list()

    with allure.step('4. Проверка наличия созданного пользователя в списке'):
        assert user_data['first_name'] in customers_first_names, \
            'Не удалось найти созданного пользователя'

    with allure.step('5. Удаление пользователя'):
        try:
            cust_page.delete_button_click()
        except Exception as e:
            raise Exception(f'Не удалось нажать кнопку "Delete". Ошибка: {e}')

    with allure.step('6. Очистка поля поиска'):
        try:
            cust_page.clean_search_field()
        except Exception as e:
            raise Exception(f'Не удалось очистить поле поиска. Ошибка: {e}')

    with allure.step('7. Проверка отсутствия пользователя в списке'):
        customers_first_names = cust_page.get_name_list()
        assert user_data['first_name'] not in customers_first_names, \
            'Не удалось удалить пользователя'
