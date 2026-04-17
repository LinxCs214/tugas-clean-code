class OrderProcessor:
    DISCOUNT_RATES = {
        "PROMO10": 0.1
    }

    def calculate_total(self, items):
        return sum(item['price'] for item in items)

    def apply_discount(self, total, promo_code):
        discount_rate = self.DISCOUNT_RATES.get(promo_code, 0)
        return total * (1 - discount_rate)

    def save_order_to_file(self, total, filename="orders.txt"):
        with open(filename, "a") as file:
            file.write(f"Order Total: {total}\n")

    def process(self, items, promo_code=None):
        total = self.calculate_total(items)
        total_after_discount = self.apply_discount(total, promo_code)
        
        self.save_order_to_file(total_after_discount)
        return total_after_discount
    
if __name__ == "__main__":
    processor = OrderProcessor()
    
    # Data contoh (list item belanja)
    data_belanja = [
        {'name': 'Buku', 'price': 50000},
        {'name': 'Pena', 'price': 10000}
    ]
    
    # Jalankan prosesnya
    hasil = processor.process(data_belanja, "PROMO10")
    
    # Cetak ke layar agar terlihat hasilnya
    print(f"Transaksi berhasil! Total akhir: {hasil}")
