from selenium.webdriver.common.by import By


class DndLocators:
    FRAME_LOCATOR = (By.XPATH, '//iframe[@src="droppable/default.html"]')
    TEXT_BEFORE = (By.XPATH, '//div[@id="droppable"]/p[normalize-space()="Drop here"]')
    TEXT_AFTER = (By.XPATH, '//div[@id="droppable"]/p[normalize-space()="Dropped!"]')
    DRAGGABLE = (By.XPATH, '//div[@id="draggable"]')
    DROPPABLE = (By.XPATH, '//div[@id="droppable"]')
