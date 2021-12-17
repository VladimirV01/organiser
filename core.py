"""
This is the core for the Organiser project.
"""

from datetime import datetime


class Item:
    """
    title: Title of the item
    description: Some text that describes what exactly is this item and what it is used for.
    quantity: Quantity of the item.
    category: Which category is this item from. (Electronic components, mechanics, electronic modules)
    value: Value of the component.
    """
    def __init__(self, title: str = "Default",
                 description: str = "Default",
                 quantity: int = 0,
                 category: str = "Common",
                 *args, **kwargs) -> None:

        # TODO: Add more categories
        self.__categories = {"components", "mechanics", "modules"}

        self.__title = title
        self.__description = description
        self.__quantity = quantity
        self.__category = category if category in self.__categories else None
        self.__created_date = datetime.now()
        self.__modified_date = None
        value = kwargs.get("value", None)
        datasheet = kwargs.get("datasheet", None)
        if value is not None:
            self.__value = value
        if datasheet is not None:
            self.__datasheet_path = datasheet

    def get_value(self) -> str or None:
        try:
            return self.__value
        except AttributeError:
            return None

    def set_value(self, value: str = None) -> bool:
        if value is not None:
            try:
                self.__value = value
                self.update_modified_date()
                return True
            except AttributeError:
                return False

    def update_modified_date(self) -> None:
        self.__modified_date = datetime.now()

    def set_quantity(self, quantity: int = 1) -> None:
        """This function sets the quantity of the item."""
        self.__quantity = quantity
        self.update_modified_date()

    def decrease_quantity(self, amount: int = 1) -> None:
        self.__quantity -= amount
        self.update_modified_date()

    def increase_quantity(self, amount: int = 1) -> None:
        self.__quantity += amount
        self.update_modified_date()

    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str = None) -> None:
        if title is not None:
            self.__title = title
            self.update_modified_date()

    def get_description(self) -> str:
        return self.__description

    def set_description(self, description: str = None) -> None:
        if description is not None:
            self.__description = description
            self.update_modified_date()

    def __del__(self):
        pass

    def __repr__(self):
        return f"This item is {self.__title}. \nThe quantity is {self.__quantity}.\n" \
               f"{self.__description}.\nIt was created {self.__created_date}.\n" \
               f"If is from category {self.__category}.\n"


if __name__ == "__main__":
    item = Item("Resistor", "This is a 49kOhm resistor", 2, category="Electronics", value=49)
    print(item)
    print(item.get_value())
