import allure
from faker import Faker

from data.locators.registration_page_locators import RegistrationPageLocators as loc
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    EXPECTED_TEXTS = {
        'page_title': 'Registration Form',
        'success_message': 'User registered successfully!'
    }

    def __init__(self, browser):
        super().__init__(browser)
        self.fake = Faker()

    def fill_complete_registration_form(self):
        with allure.step("Заполнение полей формы регистрации"):
            user_data = self._generate_user_data()

            self.fill_field(loc.FIRST_NAME_FIELD, user_data['first_name'])
            self.fill_field(loc.LAST_NAME_FIELD, user_data['last_name'])
            self.fill_field(loc.EMAIL_FIELD, user_data['email'])
            self.fill_field(loc.PASSWORD_FIELD, user_data['password'])
            self.select_hobby_sports()
            self.select_gender()
            self.fill_about_yourself_with_longest_hobby()

    def _generate_user_data(self):
        """Генерируем данные пользователя"""
        return {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
            'password': self.fake.password()
        }

    def select_hobby_sports(self):
        with allure.step("Включение чекбокса хобби 'Sports'"):
            try:
                self.click_element(loc.HOBBY_SPORTS)
            except Exception as e:
                raise Exception(f"Ошибка при включении чекбокса хобби 'Sports': {e}")

    def select_gender(self):
        with allure.step("Выбор пола"):
            try:
                self.click_element(loc.GENDER_FIELD)
                self.click_element(loc.GENDER_MALE)
            except Exception as e:
                raise Exception(f"Ошибка при выборе пола: {e}")

    def _get_available_hobbies(self):
        """Получаем уникальные тексты хобби через labels"""
        try:
            labels = self.find_elements_(*loc.HOBBY_LABELS)

            return list({
                label.text.strip().split()[0]
                for label in labels
                if label.text.strip() and any(char.isalpha() for char in label.text)
            })

        except Exception as e:
            raise Exception(f"Ошибка при поиске labels: {e}")

    def _find_longest_hobby_word(self):
        """
        Ищем самое длинное слово из списка хобби
        """
        hobbies = self._get_available_hobbies()
        try:
            longest_word = max(hobbies, key=len)
            return longest_word

        except Exception as e:
            raise Exception(f"Ошибка при поиске самого длинного слова: {e}")

    def fill_about_yourself_with_longest_hobby(self):
        with allure.step("Заполнение поля About Yourself"):
            longest_hobby = self._find_longest_hobby_word()
            about_text = f"Самое длинное слово из предложенных хобби - {longest_hobby}"
            try:
                self.fill_field(loc.ABOUT_FIELD, about_text)

            except Exception as e:
                raise Exception(f"Ошибка при заполнении поля About Yourself: {e}")

    def click_register_button(self):
        with allure.step("Нажимаем на кнопку 'Submit'"):
            try:
                self.click_element(loc.SAMPLE_FORM_BUTTON)
            except Exception as e:
                raise Exception(f"Ошибка при нажатии на кнопку 'Submit': {e}")

    def verify_success_message(self):
        with allure.step("Проверка сообщения об успешной регистрации"):
            success_element = self.find_element(loc.SUCCESS_MESSAGE)
            actual_text = self.get_text(success_element)
            expected_text = self.EXPECTED_TEXTS['success_message']

            assert actual_text == expected_text, \
                f"Неверное сообщение об успехе. Ожидалось: '{expected_text}', Получено: '{actual_text}'"

            return True
