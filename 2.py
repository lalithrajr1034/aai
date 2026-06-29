import requests
from langflow.custom import Component
from langflow.io import MessageTextInput, Output
from langflow.schema import Data


class CurrencyConverterTool(Component):
    display_name = "Currency Converter Tool"
    description = "Converts currency using live exchange rates."
    icon = "coins"
    name = "CurrencyConverterTool"
    inputs = [
        MessageTextInput(
            name="query",
            display_name="Conversion Request",
            info="Use format: 100 USD INR",
            tool_mode=True,
        ),
    ]
    outputs = [
        Output(
            display_name="Result",
            name="result",
            method="convert_currency",
        ),
    ]

    def convert_currency(self) -> Data:
        try:
            parts = self.query.upper().split()
            amount = parts[0]
            base = parts[1]
            target = parts[2]
            url = (
                f"https://api.frankfurter.dev/v1/latest"
                f"?base={base}&symbols={target}"
            )
            response = requests.get(url)
            data = response.json()
            rate = data["rates"][target]
            converted = float(amount) * rate
            result = (
                f"{amount} {base} = "
                f"{converted:.2f} {target}"
            )

            return Data(value={"result": result})

        except:
            return Data(value={"result": "Use format: 100 USD INR"})
