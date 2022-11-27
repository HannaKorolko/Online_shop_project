from flask import Flask, render_template, request, url_for
app = Flask(__name__)

class Client:
    def __init__(self, name, email, address, order):
        self.name = name
        self.email = email
        self.address = address
        self.order = order
        
    def __repr__(self):
        return self.name + ", email: " + self.email + ", address: " + self.address + ", order: " + str(self.order)
        
class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    def __repr__(self):
        return self.name + " " + str(self.amount) + " pack by price: " + str(self.price) + "€"
    def sum_order_product(self):
        return int(self.amount)*int(self.price)

@app.route('/')
def home():
    return render_template('project_smachno.html')

@app.route('/menu/')
def menu():
    return render_template('products.html')

@app.route('/order/', methods=["GET","POST"])
def order():
    if request.method == "GET":
        return render_template('order.html')
    else:
        n_vareniki = request.form["n_vareniki"]
        n_cab_rolls = request.form["n_cab_rolls"]
        n_cheese_pancakes = request.form["n_cheese_pancakes"]
        n_pancakes_salmon = request.form["n_pancakes_salmon"]      

        order_of_client = [Product("vareniki", n_vareniki, 7), Product("cab_rolls", n_cab_rolls, 8),
                           Product("cheese_pancakes", n_cheese_pancakes, 6), Product("pancakes_salmon", n_pancakes_salmon, 8)]  
        total_order = Client(str(request.form["clientname"]), str(request.form["email"]), str(request.form["address"]), order_of_client)
        total = 0
        for i in range(len(order_of_client)):
            total += order_of_client[i].sum_order_product()
        
        return render_template('confirm_order.html', total_sum=total)

    






