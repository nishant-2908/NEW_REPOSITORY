class Quantity:
    def __init__(
        self, name: str, prefix: str, conversion_to_si: float, si_to_unit: float
    ):
        self.name = name
        self.prefix = prefix
        self.conversion_to_si = conversion_to_si
        self.si_to_unit = si_to_unit


# Defining a list to convert the quantities
converters = [
    "Length",
    "Weight",
    "Area",
    "Temperature",
    "Volume",
    "Time",
    "Power",
    "Speed",
    "Pressure",
]


# Defining a list to store the units for each quantity

length = [
    Quantity("meter", "m", 1, 1),
    Quantity("kilometer", "km", 1000, 0.001),
    Quantity("centimeter", "cm", 0.01, 100),
    Quantity("millimeter", "mm", 0.001, 1000),
    Quantity("feet", "ft", 0.3048, 3.2808399),
    Quantity("yard", "yd", 0.9144, 1.0936133),
    Quantity("inch", "in", 0.0254, 39.3700787),
    Quantity("mile", "mi", 1609.344, 0.000621371),
]

weight = [
    Quantity("kilogram", "kg", 1, 1),
    Quantity("gram", "g", 0.001, 1000),
    Quantity("pounds", "lbs", 0.45359237, 2.20462262),
    Quantity("ounce", "oz", 0.0283495231, 35.2739619),
    Quantity("metric ton", "t", 1000, 0.001),
]

area = [
    Quantity("square meter", "m²", 1, 1),
    Quantity("square kilometer", "km²", 1000000, 0.000001),
    Quantity("square centimeter", "cm²", 0.0001, 10000),
    Quantity("square millimeter", "mm²", 0.000001, 1000000),
    Quantity("square feet", "ft²", 0.09290304, 10.7639104),
    Quantity("square yard", "yd²", 0.83612736, 1.19599005),
    Quantity("square inch", "in²", 0.00064516, 1550.00310001),
    Quantity("acre", "ac", 4046.8564224, 0.0002471053),
]

temperature = [
    Quantity("celsius", "°C", 1, 1),
    Quantity("fahrenheit", "°F", (5 / 9), (9 / 5)),
    Quantity("kelvin", "K", 1, 1),
]

volume = [
    Quantity("liter", "L", 0.001, 1000),
    Quantity("milliliter", "mL", 0.000001, 1000000),
    Quantity("cubic meter", "m³", 1, 1),
    Quantity("cubic centimeter", "cm³", 0.000001, 1000000),
    Quantity("cubic millimeter", "mm³", 0.000000001, 1000000000),
    Quantity("fluid ounce", "fl oz", 0.00002957353, 33.8140227),
    Quantity("cup", "cup", 0.0002365882, 4.22675169),
    Quantity("pint", "pt", 0.0004731765, 2.11337585),
    Quantity("quart", "qt", 0.0009463529, 1.05668792),
    Quantity("gallon", "gal", 0.003785412, 0.26417205),
]

time = [
    Quantity("second", "s", 1, 1),
    Quantity("minute", "min", 60, 0.0166667),
    Quantity("hour", "h", 3600, 0.000277778),
    Quantity("day", "d", 86400, 0.0000115741),
    Quantity("week", "wk", 604800, 0.0000016534),
    Quantity("month", "mo", 2629800, 0.0000003802),
    Quantity("year", "yr", 31557600, 0.0000000317),
]

power = [
    Quantity("watt", "W", 1, 1),
    Quantity("kilowatt", "kW", 1000, 0.001),
    Quantity("horsepower", "hp", 745.699871, 0.001341022),
]

speed = [
    Quantity("meter per second", "m/s", 1, 1),
    Quantity("kilometer per hour", "km/h", 0.277777778, 3.6),
    Quantity("mile per hour", "mph", 0.44704, 2.23693629),
    Quantity("foot per second", "ft/s", 0.3048, 3.28084),
]

pressure = [
    Quantity("pascal", "Pa", 1, 1),
    Quantity("kilopascal", "kPa", 1000, 0.001),
    Quantity("pound-force per square inch", "psi", 6894.757, 0.0001450377),
    Quantity("atmosphere", "atm", 101325, 0.00000986923),
    Quantity("millimeter of mercury", "mmHg", 133.322, 0.0075),
]
