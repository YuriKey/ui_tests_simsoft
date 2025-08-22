import allure

from data.urls import Urls

urls = Urls()


@allure.epic('Банковское приложение')
@allure.feature('Аккаунт менеджера банка')
@allure.story('Добавление нового пользователя')
@allure.severity(allure.severity_level.CRITICAL)
def test_add_new_customer(pages):
    man_page = pages.manager
    exp_text = man_page.EXPECTED_TEXTS
    man_page.open(urls.APP_LOGIN_PAGE)

    with allure.step('1. Проверка открытия интерфейса Bank Manager Login'):
        man_page.click_manager_login_button()
        man_page.await_for_js_reaction()
        assert man_page.get_current_url() == urls.APP_MANAGER_PAGE, \
            'Неверный URL страницы менеджера банка'
        assert man_page.get_title() == exp_text['page_title'], \
            'Неверный заголовок страницы регистрации'

    with allure.step('2. Нажатие на кнопку Add Customer'):
        man_page.click_new_customer_button()
        man_page.await_for_js_reaction()
        assert man_page.get_current_url() == urls.APP_ADD_CUSTOMER_PAGE, \
            'Неверный URL страницы добавления покупателя'

    with allure.step('3. Заполнение формы добавления покупателя'):
        man_page.fill_new_customer_form()
        man_page.await_for_js_reaction()

    with allure.step('4. Проверка появления всплывающего окна с подтверждением'):
        man_page.click_submit_button()
        alert = man_page.switch_to_alert()
        actual_text = alert.text
        man_page.accept_alert()
        assert actual_text.startswith(exp_text['alert_text']), \
            'Неверный текст всплывающего окна'
