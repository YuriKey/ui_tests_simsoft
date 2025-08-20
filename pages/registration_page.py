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
        """
        Заполнить все поля формы регистрации
        """
        user_data = self._generate_user_data()

        self.fill_field(loc.FIRST_NAME_FIELD, user_data['first_name'])
        self.fill_field(loc.LAST_NAME_FIELD, user_data['last_name'])
        self.fill_field(loc.EMAIL_FIELD, user_data['email'])
        self.fill_field(loc.PASSWORD_FIELD, user_data['password'])
        self.select_hobby_sports()
        self.select_gender()
        self.fill_about_yourself_with_longest_hobby()

    def _generate_user_data(self):
        """
        Генерация данных для регистрации
        """
        return {
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'email': self.fake.email(),
            'password': self.fake.password()
        }

    def select_hobby_sports(self):
        """
        Выбрать хобби Sports
        """
        self.click_element(loc.HOBBY_SPORTS)

    def select_gender(self):
        self.click_element(loc.GENDER_FIELD)
        self.click_element(loc.GENDER_MALE)

    @allure.step("Получить список всех доступных хобби")
    def get_available_hobbies(self):
        hobbies = []
        try:
            hobbies_elements = self.browser.find_elements(*loc.ALL_HOBBIES)

            for hobby_element in hobbies_elements:
                try:
                    hobby_value = hobby_element.get_attribute("value")
                    if hobby_value:
                        hobbies.append(hobby_value)
                except Exception as e:
                    raise Exception(f"Ошибка при получении значения хобби: {e}")

        except Exception as e:
            raise Exception(f"Ошибка при поиске элементов хобби: {e}")

        return hobbies

    def get_hobby_labels_text(self):
        """Получаем тексты хобби через labels"""
        labels_text = []
        try:
            labels = self.browser.find_elements(*loc.HOBBY_LABELS)

            for label in labels:
                try:
                    label_text = label.text.strip()

                    if label_text and any(char.isalpha() for char in label_text):
                        clean_text = label_text.replace('\n', ' ').replace('\r', ' ').strip()

                        if ' ' in clean_text:
                            clean_text = clean_text.split(' ')[0]

                        if clean_text and clean_text not in labels_text:
                            labels_text.append(clean_text)

                except Exception as e:
                    raise Exception(f"Ошибка при обработке label: {e}")

        except Exception as e:
            raise Exception(f"Ошибка при поиске labels: {e}")

        return labels_text

    def find_longest_hobby_word(self):
        try:
            hobbies = self.get_available_hobbies()

            if not hobbies:
                hobbies = self.get_hobby_labels_text()

            longest_word = max(hobbies, key=len)

            return longest_word

        except Exception as e:
            raise Exception(f"Ошибка при поиске самого длинного слова: {e}")

    def click_register_button(self):
        """
        Нажать кнопку Register
        """
        self.click_element(loc.SAMPLE_FORM_BUTTON)

    def verify_success_message(self):
        """
        Проверить сообщение об успешной регистрации
        """
        success_element = self.wait.until(
            lambda driver: driver.find_element(*loc.SUCCESS_MESSAGE),
            message="Сообщение об успешной регистрации не появилось"
        )

        actual_text = self.get_text(success_element)
        expected_text = self.EXPECTED_TEXTS['success_message']

        assert actual_text == expected_text, \
            f"Неверное сообщение об успехе. Ожидалось: '{expected_text}', Получено: '{actual_text}'"

        return True

    @allure.step("Заполнить поле About Yourself с самым длинным словом из хобби")
    def fill_about_yourself_with_longest_hobby(self):
        try:
            longest_hobby = self.find_longest_hobby_word()

            about_text = f"Самое длинное слово из предложенных хобби - {longest_hobby}"

            self.fill_field(loc.ABOUT_FIELD, about_text)

            return about_text

        except Exception as e:
            raise Exception(f"Ошибка при заполнении поля About Yourself: {e}")
