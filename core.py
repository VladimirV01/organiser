"""
This is the core for the Organiser project.
"""

from datetime import datetime


class ComponentItem:
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
                 category: str = "Other",
                 *args, **kwargs) -> None:

        # TODO: Add more categories
        self.__categories = {"Resistors",
                             "Capacitors",
                             "Diodes",
                             "ICs",
                             "Microcontrollers",
                             "Inductors",
                             "Bipolar Transistors",
                             "FETs",
                             "Other"}

        self.__title = title
        self.__description = description
        self.__quantity = quantity
        self.__category = category if category in self.__categories else None
        self.__created_date = datetime.now()
        self.__modified_date = None

        body_package = kwargs.get("body", None)
        datasheet = kwargs.get("datasheet", None)
        img = kwargs.get("image", None)
        if datasheet is not None:
            self.__datasheet_path = datasheet
        if img is not None:
            self.__img_path = img
        if body_package is not None:
            self.__body_package = body_package

    @property
    def get_body_package(self) -> str or None:
        try:
            return self.__body_package
        except AttributeError:
            return None

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

    @property
    def get_title(self) -> str:
        return self.__title

    def set_title(self, title: str = None) -> None:
        if title is not None:
            self.__title = title
            self.update_modified_date()

    @property
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


class PassiveComponentItem(ComponentItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        multiplier = kwargs.get("multiplier", None)
        self.MULTIPLIERS = {
            "f": 1e-15,
            "p": 1e-12,
            "n": 1e-9,
            "u": 1e-6,
            "m": 1e-3,
            "k": 1e3,
            "M": 1e6,
            "G": 1e9,
            "T": 1e12
        }
        value = kwargs.get("value", None)
        if multiplier is not None and multiplier in self.MULTIPLIERS.keys():
            self.__multiplier = multiplier

        if value is not None:
            self.__value = value

    def get_value(self, numeric: bool = False) -> int or None:
        try:
            return self.__value * self.MULTIPLIERS[self.__multiplier] if numeric else self.__value
        except AttributeError:
            return None

    @property
    def get_multiplier(self) -> str or None:
        try:
            return self.__multiplier
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


class Resistor(PassiveComponentItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__measuring_unit = "Ohm"

    @property
    def get_resistor_value(self):
        return f'{self.get_value()} {self.get_multiplier}{self.__measuring_unit}'


if __name__ == "__main__":
    # item = ComponentItem("Resistor", "This is a 49kOhm resistor", 2, category="Electronics", value=49)
    # print(item)
    # print(item.get_value())
    resistor = Resistor(title="Resistor",
                        description="This is a 49kOhm resistor.",
                        quantity=10,
                        category="Resistors",
                        value=49,
                        multiplier="k")
    print(resistor)
    print(resistor.get_resistor_value)
