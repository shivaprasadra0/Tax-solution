class Item:
    def __init__(self, quantity, name, price, imported=False):
        self.quantity = quantity
        self.name = name
        self.price = price
        self.imported = imported
        self.tax_rate = self._calculate_tax_rate()
        self.tax_amount = self._calculate_tax_amount()
        self.total_price = price + self.tax_amount

    def _calculate_tax_rate(self):
        tax_rate = 0.0
        if not any(exempt_item in self.name.lower() for exempt_item in ["book", "chocolate", "pill", "food", "medical"]):
            tax_rate = 0.1
        if self.imported:
            tax_rate += 0.05
            
        return tax_rate
    
    def _calculate_tax_amount(self):
        raw_tax = self.price * self.tax_rate
        return round(raw_tax * 20) / 20 if raw_tax % 0.05 == 0 else ((int(raw_tax * 20) + 1) / 20)

    def __str__(self):
        return f"{self.quantity} {self.name}: {self.total_price:.2f}"


class Receipt:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def get_total_taxes(self):
        return sum(item.tax_amount for item in self.items)
    
    def get_total_price(self):
        return sum(item.total_price for item in self.items)
    
    def print_receipt(self):
        for item in self.items:
            print(item)
        print(f"Sales Taxes: {self.get_total_taxes():.2f}")
        print(f"Total: {self.get_total_price():.2f}")


def parse_input(input_text):
    receipt = Receipt()
    
    for line in input_text.strip().split('\n'):
        if not line.strip():
            continue
            
        parts = line.strip().split(' at ')
        quantity_and_name = parts[0]
        price = float(parts[1])
        
        quantity = int(quantity_and_name.split(' ')[0])
        
        name = ' '.join(quantity_and_name.split(' ')[1:])
        
        imported = 'imported' in name.lower()
        
        receipt.add_item(Item(quantity, name, price, imported))
    
    return receipt


def process_inputs():
    input1 = """1 book at 12.49
                1 music CD at 14.99
                1 chocolate bar at 0.85"""

    input2 = """1 imported box of chocolates at 10.00
                1 imported bottle of perfume at 47.50"""

    input3 = """1 imported bottle of perfume at 27.99
                1 bottle of perfume at 18.99
                1 packet of headache pills at 9.75
                1 box of imported chocolates at 11.25"""

    print("Output 1:")
    parse_input(input1).print_receipt()
    print()
    
    print("Output 2:")
    parse_input(input2).print_receipt()
    print()
    
    print("Output 3:")
    parse_input(input3).print_receipt()


if __name__ == "__main__":
    process_inputs()