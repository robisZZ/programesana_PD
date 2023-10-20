class Product:
    def __init__(self, name='prece', quantity=0, category='detaLa', price=0.0):
        self.product_name = name
        self.amount = quantity
        self.category = category
        self.unit_price = price

    def display_info(self, number):
        print(f'{number}. Produkta nosaukums: {self.product_name}, Pieejamais daudzums: {self.amount}, Kategorija: {self.category}, Cena: {self.unit_price}')

    def sell(self, sold_quantity):
        if self.amount >= sold_quantity:
            self.amount -= sold_quantity
        else:
            self.amount = 0

    def deliver(self, delivered_quantity):
        self.amount += delivered_quantity

    def get_quantity_and_price(self):
        return self.amount, self.unit_price

    def change_name(self, new_name):
        self.product_name = new_name

    def change_quantity(self, new_quantity):
        self.amount = new_quantity

    def change_category(self, new_category):
        self.category = new_category

    def change_price(self, new_price):
        self.unit_price = float(new_price)

    def is_name_match(self, name_to_check):
        if self.product_name == name_to_check:
            return 'yes'


class Computer(Product):
    def __init__(self, quantity, category, price, manufacturer):
        super().__init__("Dators", quantity, category, price)
        self.manufacturer = manufacturer

    def display_info(self, number):
        print(f'{number}. Ražotājs: {self.manufacturer} {self.product_name}, Pieejamais daudzums: {self.amount}, Kategorija: {self.category}, Cena: {self.unit_price}')


class StoreManager:
    def __init__(self):
        self.products = []
        self.total_earnings = 0.00

    def add_product(self, product):
        self.products.append(product)

    def sell_product(self, product_name, sold_quantity):
        for product in self.products:
            if product.is_name_match(product_name) == 'yes':
                sold, earnings = product.sell(sold_quantity)
                self.total_earnings += earnings
                print(f"Pārdoti {sold} produkti '{product.product_name}', ienākumi: {earnings:.2f} EUR")
                return

    def deliver_product(self, product_name, delivered_quantity):
        for product in self.products:
            if product.is_name_match(product_name) == 'yes':
                product.deliver(delivered_quantity)
                print(f"Produkti '{product.product_name}' daudzums ir atjaunināts!")

    def display_products(self):
        for i, product in enumerate(self.products):
            product.display_info(i)

    def display_earnings(self):
        print(f"Kopējie ienākumi: {self.total_earnings:.2f} EUR")


if __name__ == '__main__':
    manager = StoreManager()

    while True:
        print("\nIzvēlieties darbību:")
        print("1. Pievienot produktu")
        print("2. Pārdot produktus")
        print("3. Piegādāt produktus")
        print("4. Parādīt produktus")
        print("5. Beigt")

        choice = input("Ievadiet izvēles numuru: ")

        if choice == '1':
            name = input("Ievadiet produkta nosaukumu: ")
            category = input("Ievadiet kategoriju (detaLa/programmatūra): ")
            quantity = int(input("Ievadiet produkta daudzumu: "))
            price = float(input("Ievadiet produkta cenu: "))
            if category.lower() == 'detaļa':
                product = Product(name, quantity, category, price)
            elif category.lower() == 'programmatūra':
                product = Computer(quantity, category, price, input("Ievadiet ražotāju: "))
            manager.add_product(product)

        elif choice == '2':
            name = input("Ievadiet produkta nosaukumu, ko vēlaties pārdot: ")
            amount = int(input("Ievadiet daudzumu, ko vēlaties pārdot: "))
            manager.sell_product(name, amount)

        elif choice == '3':
            name = input("Ievadiet produkta nosaukumu, ko vēlaties piegādāt: ")
            amount = int(input("Ievadiet daudzumu, ko vēlaties piegādāt: "))
            manager.deliver_product(name, amount)

        elif choice == '4':
            manager.display_products()
            manager.display_earnings()

        elif choice == '5':
            break

        else:
            print("Nepareiza izvēle, lūdzu, ievadiet pareizu izvēles numuru.")
