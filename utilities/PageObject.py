import pytest


@pytest.mark.usefixtures("setup")
class PageObject:
    # region getter
    def _get_element(self, *args):
        return self.driver.find_element(*args)

    def _get_elements(self, *args):
        return self.driver.find_elements(*args)

    def _get_element_text(self, *args):
        items = self._get_elements(*args)
        _menu_list = []
        for item in items:
            _menu_list.append(item.text.strip())
        return _menu_list
