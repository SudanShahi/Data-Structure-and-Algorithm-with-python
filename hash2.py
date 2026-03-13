class InventoryHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def set_item(self, sku, name, quantity):
        index = self._hash(sku)
        bucket = self.table[index]

        for i, item in enumerate(bucket):
            if item["sku"] == sku:
                bucket[i] = {"sku": sku, "name": name, "quantity": quantity}
                return

        bucket.append({"sku": sku, "name": name, "quantity": quantity})

    def get_item(self, sku):
        index = self._hash(sku)
        bucket = self.table[index]

        for item in bucket:
            if item["sku"] == sku:
                return item

        return None

    def remove_item(self, sku):
        index = self._hash(sku)
        bucket = self.table[index]

        for i, item in enumerate(bucket):
            if item["sku"] == sku:
                bucket.pop(i)
                return True

        return False

    def print_table(self):
        print("\n=== Inventory Hash Table ===")
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")


inv = InventoryHashTable(size=7)
inv.set_item("A101", "USB Cable", 25)
inv.set_item("B205", "Keyboard", 12)
inv.set_item("C333", "Mouse", 18)
inv.set_item("A101", "USB Cable", 30)
inv.print_table()
print("Search B205:", inv.get_item("B205"))
print("Remove C333:", inv.remove_item("C333"))
inv.print_table()