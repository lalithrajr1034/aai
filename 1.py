from langflow.custom import Component
from langflow.io import MessageTextInput, Output
from langflow.schema.message import Message


class ThermostatReflexAgent(Component):
    display_name = "Thermostat Reflex Agent"
    description = "Simple reflex agent using temperature and humidity."
    icon = "thermometer"
    name = "ThermostatReflexAgent"
    inputs = [
        MessageTextInput(
            name="temperature",
            display_name="Temperature (°C)",
            info="Enter room temperature in Celsius",
            value="26"
        ),
        MessageTextInput(
            name="humidity",
            display_name="Humidity (%)",
            info="Enter room humidity percentage",
            value="75"
        ),
    ]
    outputs = [
        Output(
            display_name="Response",
            name="response",
            method="make_decision"
        ),
    ]

    def make_decision(self) -> Message:
        try:
            temperature = float(self.temperature)
            humidity = float(self.humidity)

        except ValueError:
            return Message(
                text="Invalid input. Please enter numeric values for temperature and humidity."
            )

        if temperature < 20:
            action = "Heating ON"
        elif temperature > 28:
            action = "Cooling ON"
        elif humidity > 70 and temperature >= 25:
            action = "Cooling ON"
        else:
            action = "System OFF / Room Comfortable"

        result = (
            f"Temperature: {temperature} °C\n"
            f"Humidity: {humidity} %\n"
            f"Action: {action}"
        )

        self.status = result
        return Message(text=result)
