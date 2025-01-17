from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

root = Tk()
root.geometry("800x600")
root.title("Encapsulation")
root.configure(bg='orange2')
class Fruit:
    def __init__(self, fruit, quantity):
        self.fruit = fruit
        self.quantity = int(quantity)
        self.__cost = 250

    def __calculateCost(self):
        totalCost = self.quantity * self.__cost
        print(totalCost)
        label_show_amount["text"] = "Total Cost: ₹" + str(totalCost)
        if self.fruit == "Apple":
            calories = 52 * self.quantity
            fruit_image["image"]=apple
        elif self.fruit == "Mango":
            calories = 60 * self.quantity
            fruit_image["image"]=mango
        elif self.fruit == "Orange":
            calories = 65 * self.quantity
            fruit_image["image"]=orange
        # print(calories)

        label_show_quantity["text"] = "x" + str(self.quantity)+ " = " + str(calories)

    def getCost(self):
        self.__calculateCost()


def orderFruit():
    fruit = fruit_dropdown.get()
    quantity = input_quantity.get()
    print(fruit, quantity)
    obj1 = Fruit(fruit, quantity)
    obj1.getCost()


label_heading = Label(root, text="Juice Center", bg="orange2", font=("Sylfaen", 18, "bold", "italic"))
label_heading.place(relx=0.05, rely=0.1, anchor= W)

juice = ImageTk.PhotoImage(Image.open("logo.png"))
juice_image = Label(root, image=juice, bg="orange2")
juice_image.place(relx=0.2, rely=0.4, anchor=CENTER)

apple = ImageTk.PhotoImage(Image.open("apple_img.png"))
mango = ImageTk.PhotoImage(Image.open("mango_img.png"))
orange = ImageTk.PhotoImage(Image.open("orange.png"))

fruit_image = Label(root, bg="orange2")
fruit_image.place(relx=0.75, rely=0.8, anchor=CENTER)

label_name = Label(root, text="Select fruit", bg="orange2", font=("bahnschrift light", 15))
label_name.place(relx=0.96, rely=0.2, anchor=E)

fruit_list = ["Apple", "Mango", "Orange"]
fruit_dropdown = ttk.Combobox(root, state="readonly", values=fruit_list, justify="right")
fruit_dropdown.place(relx=0.95, rely=0.25, anchor= E)

input_quantity = Entry(root, font=("bahnschrift light", 15))
input_quantity.place(relx=0.95, rely=0.4, anchor= E)

label_quantity = Label(root, text="Enter Quantity", bg="orange2", font=("Bahnschrift light", 15))
label_quantity.place(relx=0.96, rely=0.35, anchor= E)

label_show_amount = Label(root, bg="orange2", font=("bahschrift light", 12))
label_show_amount.place(relx=0.95, rely=0.7, anchor=E)
label_show_quantity = Label(root, bg="orange2", font=("bahschrift light", 12))
label_show_quantity.place(relx=0.95, rely=0.8, anchor=E)

button = Button(root, text="Total Cost", command=orderFruit)
button.place(relx=0.95, rely=0.5, anchor=E)

root.mainloop()