import multiprocessing

class WarehouseManager:
    def __init__(self):
        self.data = {}

    def process_request(self, request):
        product, action, amount = request

        print(f"Processing request: {request}")

        if action == "receipt":
            if product in self.data:
                self.data[product] += amount
            else:
                self.data[product] = amount
        elif action == "shipment":
            if product in self.data:
                self.data[product] = max(0, self.data[product] - amount)
            else:
                print(f"Product '{product}' not found in the warehouse.")

        print(f"Updated data: {self.data}")

    # остальной код остается без изменений

def process_request_wrapper(manager, request):
    manager.process_request(request)

if __name__ == "__main__":
    manager = WarehouseManager()
    requests = [("product1", "receipt", 50), ("product2", "receipt", 100), ("product3", "receipt", 200)]

    processes = []
    for request in requests:
        p = multiprocessing.Process(target=process_request_wrapper, args=(manager, request))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
