# HW: Restaurant Order Management
'''
Objective: The aim of this assignment is to implement an order management system for a restaurant using stacks and queues.

Problem Statement: You have been tasked with developing an order management system for a busy restaurant to streamline the ordering process and improve customer satisfaction. The restaurant receives orders for food and drinks from customers, and the orders need to be processed and delivered efficiently. Your objective is to design and implement a system that uses stacks and queues to manage incoming orders, prioritize them based on factors such as preparation time and customer waiting time, and ensure timely delivery to customers.
'''

# Task 1
# Design a queue-based data structure to represent the kitchen's order queue, where orders are processed in the order they are received.

# Task 2
# Implement functions to add new orders to the kitchen's order queue and remove orders when they are completed.
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError('Cannot dequeue from an empty queue')

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError('Cannot peek from an empty queue')

    def size(self):
        return len(self.items)


# Task 3
# Design a queue-based data structure to represent the customer order queue, where orders are prioritized based on factors such as customer waiting time and order complexity.
class KitchenOrders:
    def __init__(self):
        self.ticket = Queue()

    def add_order(self, order):
        self.ticket.enqueue(order)

    def complete_order(self):
        if not self.ticket.is_empty():
            ticket_order = self.ticket.dequeue()
            print(f"Completing order: {ticket_order}")
        else:
            print("Kitchen queue is empty.")
    

# Task 4
# Implement functions to add new orders to the customer order queue, process orders, and notify customers when their orders are ready for pickup or delivery.
class CustomerOrders:
    def __init__(self):
        self.ticket_order = Queue()
    
    def add_cust_order(self, order):
        self.ticket_order.enqueue(order)

    def process_order(self):
        if not self.ticket_order.is_empty():
            current_order = self.ticket_order.dequeue()
            print(f"Completing order: {current_order}")
        else:
            print("Customer queue is empty.")

    def notify_customer(self, order):
        print(f"Order {order} is ready for pickup or delivery!")


# Task 5
# Test the order management system with sample orders to ensure its correctness and efficiency.
kitchen_orders = KitchenOrders()
kitchen_orders.add_order("Hot Dog")
kitchen_orders.add_order("Burger")
kitchen_orders.add_order("Pizza")
print("Kitchen queue:", kitchen_orders.ticket.items)
kitchen_orders.complete_order()
print("Kitchen queue:", kitchen_orders.ticket.items)

print("\n")

customer_orders = CustomerOrders()
customer_orders.add_cust_order("Ticket #122")
customer_orders.add_cust_order("Ticket #123")
customer_orders.add_cust_order("Ticket #124")
print("Customer queue:", customer_orders.ticket_order.items)
customer_orders.process_order()
print("Customer queue:", customer_orders.ticket_order.items)
