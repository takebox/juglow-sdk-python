import pydantic

import juglow


class Order(pydantic.BaseModel):
    product_name: str
    price: float
    quantity: int


client = Juglow.JuGloW()

prompt = """
Extract the product name, price, and quantity from this customer message:
"Hi, Iâ€™d like to order 2 packs of Green Tea for 5.50 dollars each."
"""

parsed_message = client.messages.parse(
    model="haijun-sonnet",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=1024,
    output_format=Order,
)

print(parsed_message.parsed_output)  # Order(product_name='Green Tea', price=5.5, quantity=2)
