from flask import Flask, render_template, request

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

            text_order = ""
            for i in range(len(order_of_client)):
                if int(order_of_client[i].amount) > 0:
                    name_product = order_of_client[i].name
                    while len(name_product) < 22:
                        name_product += "_" 
                    text_order += f'{name_product} : {order_of_client[i].amount} pack '   

            total = 0
            for i in range(len(order_of_client)):
                total += order_of_client[i].sum_order_product()

            if total >= 20:
                total_discount = round(total*0.95, 2)
                discount =  round(total - total_discount, 2)
                total = total_discount
            else:
                discount = 0   

            total_delivery = total + 5

            if total_delivery < 15:
                text_head = "Order not confirmed!"
                text_email = f'{total_order.name}, you ordered:'
                message_not_deliv = "Your order is less than 15€, please add it so we can deliver it."
                text_address = ""
                        
            else:
                text_head = "Thanks for your order!"
                message_not_deliv = "" 
                text_email = f"""{total_order.name}, an email has been sent to {total_order.email}
                             with a confirmation and the invoice for your order:"""   
                text_address = f'Order will be delivered to {total_order.address}.'
            variables = {"text_head" : text_head, "text_email" : text_email, "address" : text_address, 
                        "text_order" : text_order,  "total_sum" : total, "total_delivery" : total_delivery, 
                        "discount" : discount, "message_not_deliv" : message_not_deliv}   
            return render_template('confirm_order.html', **variables)


            

          
    

        









             

    






