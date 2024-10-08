class WeatherDay:
    def __init__(self, date, max_temp, min_temp, condition, condition_icon, humidity):
        self.date = date
        self.max_temp = max_temp
        self.min_temp = min_temp
        self.condition = condition
        self.condition_icon = condition_icon  # Add this attribute
        self.humidity = humidity

    def __str__(self):
        return (f"Date: {self.date}\n"
                f"Max Temp: {self.max_temp} °C\n"
                f"Min Temp: {self.min_temp} °C\n"
                f"Condition: {self.condition}\n"
                f"Humidity: {self.humidity}%\n")

    def to_dict(self):
        """Optional: Converts the instance data to a dictionary."""
        return {
            'date': self.date,
            'max_temp': self.max_temp,
            'min_temp': self.min_temp,
            'condition': self.condition,
            'humidity': self.humidity
        }
