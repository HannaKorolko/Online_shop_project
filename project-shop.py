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

    def totalCostProduct(self):
        if self.amount == "":
            self.amount = "0" 
        return int(self.amount)*int(self.price) 

def totalCostOrder(order):
    total = 0
    for i in range(len(order)):
        total += order[i].totalCostProduct() 
    return total      


@app.route('/')
def home():
    return render_template('project-shop.html')

@app.route('/menu/')
def menu():
    return render_template('products.html')

@app.route('/order/', methods=["GET","POST"])
def order():
    if request.method == "GET":
        return render_template('order.html')
    else: 
        menuOfshop = [Product("vareniki", request.form["nvareniki"], 7),
                            Product("cab_rolls", request.form["ncabrolls"], 8),
                            Product("cheese-pancakes", request.form["ncheesepancakes"], 6), 
                            Product("pancakes-salmon", request.form["npancakessalmon"], 8)]  
            
        clientsOrder = Client(str(request.form["clientname"]), str(request.form["email"]), str(request.form["address"]), menuOfshop)

        textOforder = ""
        for i in range(len(menuOfshop)):
            if menuOfshop[i].amount != "0" and menuOfshop[i].amount !="":
                nameOfproduct = menuOfshop[i].name
                while len(nameOfproduct) < 22:
                    nameOfproduct += "_" 
                textOforder += f'{nameOfproduct} : {int(menuOfshop[i].amount)} pack '   

        textHead = "Order not confirmed!"    
        discount = 0
        totalSum = totalCostOrder(menuOfshop)

        if totalSum == 0:
            messageNotDeliv = messageNotDeliv2 = textAddress = ""  
            deliveryInclud = 0
            textConfirm = "You didn't order anything."
        else:    
            if totalSum >= 20:
                discountSum = round(totalSum*0.95, 2)
                discount =  round(totalSum - discountSum, 2)
                totalSum = discountSum

            deliveryInclud = totalSum + 5

            if deliveryInclud < 15:
                textConfirm = f'{clientsOrder.name}, you ordered:'
                messageNotDeliv = "Your order is less than 15€,"
                messageNotDeliv2 = "please add more so we can deliver it."
                textAddress = ""            
            else:
                textHead = "Thanks for your order!"
                messageNotDeliv = messageNotDeliv2 = "" 
                textConfirm = f"""{clientsOrder.name}, an email has been sent to {clientsOrder.email}
                                with a confirmation and the invoice for your order:"""   
                textAddress = f'Order will be delivered to {clientsOrder.address}.'
        variables = {"textHead" : textHead, "textConfirm" : textConfirm, "address" : textAddress, 
                    "textOfOrder" : textOforder,  "totalSum" : totalSum, "deliveryInclud" : deliveryInclud, 
                    "discount" : discount, "messageNotDeliv" : messageNotDeliv, "messageNotDeliv2" : messageNotDeliv2}   
        return render_template('confirm-order.html', **variables)



            

          
    

        









             

    






