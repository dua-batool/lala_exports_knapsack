from pathlib import Path
from tkinter import *
from tkinter import messagebox
import math
import tkinter as tk
from tkinter import ttk
from fpdf import FPDF
import pdfkit
import random
import os
import textwrap

#defining class for the receipt maker
class export_knapsack:
    def __init__ (self,root):
        self.root = root
        self.thelist = []

        # main structure
        self.root.geometry('1530x700+0+0')        # size of the structure
        self.root.title('KNAPSACK PROBLEM')       # title
        bg_colour = "#104E8B"                     # background colour
        title = Label(self.root, text="LALA EXPORTS", bd=12, relief=SUNKEN,
        font=("times new roman", 30, "bold"), pady=2).pack(fill=X)

        # defining furniture:
        self.sofa = IntVar()
        self.dining_table = IntVar()
        self.dining_chairs = IntVar()
        self.computer_desk = IntVar()
        self.bookcase = IntVar()
        self.armchair = IntVar()
        self.mirror = IntVar()
        self.dressing_table = IntVar()
        self.cupboard = IntVar()
        self.baby_cradle = IntVar()
        self.bench = IntVar()
        self.dresser = IntVar()

        # price and taxes
        self.Furniture_price = StringVar()
        self.Furniture_weight = StringVar()
        self.Furniture_tax = StringVar()

        #customer details
        self.name = StringVar()
        self.phone_no = StringVar()
        self.shipment_no = StringVar()

        # assigning random value for shipment number
        x = random.randint(1,100)
        self.shipment_no.set(str(x))

        # frame customer details
        # main frame
        F1 = LabelFrame(self.root, bd=10, relief=SUNKEN, text="Customer Details", font=("times new roman", 15, "bold"), fg='lightskyblue', bg=bg_colour )
        F1.place(x=0, y=80, relwidth=1)

        # customer name label and entry box
        name_lbl = Label(F1, text="Customer Name", font=("times new roman", 18,
        'bold'), bg=bg_colour, fg='white').grid(row=0, column=0, padx=20, pady=5)
        name_txt = Entry(F1,width=15, font="arial 15",bd=7,textvariable=self.name,relief=SUNKEN).grid(row=0, column=1, pady=5,
        padx=10)

        # customer phone number label and entry box
        phone_lbl = Label(F1, text="Phone No", font=("times new roman", 18,
        'bold'), bg=bg_colour, fg='white').grid(row=0, column=2, padx=20, pady=5)
        phone_txt = Entry(F1, width=15, font="arial 15",textvariable=self.phone_no,
        bd=7, relief=SUNKEN).grid(row=0, column=3, pady=5, padx=10)

        # shipment number label and entry box
        shipment_lbl = Label(F1, text="Shipment Number", font=("times new roman",
        18, 'bold'), bg=bg_colour, fg='white').grid(row=0, column=4, padx=20, pady=5)
        shipment_txt = Entry(F1, width=15, font="arial 15",
        bd=7,textvariable=self.shipment_no, relief=SUNKEN).grid(row=0, column=5, pady=5,
        padx=10)

        # frame Furniture
        F2 = LabelFrame(self.root, bd=10, relief=SUNKEN, text="Furniture",
        font=("times new roman", 15, "bold"),fg='lightskyblue',bg=bg_colour)
        F2.place(x=0, y=180, width=380,height=380)

        # sofa label and entry box
        bath_lbl=Label(F2,text ='3-Seat Sofa Set',font=('times new roman',15,'bold'),bg=bg_colour,fg='white').grid(row=0,column=0,padx=10,pady=10,sticky='w')
        bath_txt=Entry(F2,width=10,textvariable=self.sofa,font=('times new roman',15,'bold'),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        # dining room table label and entry box
        dining_table_lbl = Label(F2, text='Dining Room Table', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='white').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        dining_table_txt = Entry(F2, width=10,textvariable=self.dining_table, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=1, column=1,padx=10, pady=10)

        # dining chairs label and entry box
        dining_chairs_lbl = Label(F2, text='Dining Chairs', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='white').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        dining_chairs_txt = Entry(F2, width=10,textvariable=self.dining_chairs, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=2, column=1, padx=10, pady=10)

        # computer_desk label and entry
        computer_desk_lbl = Label(F2, text='Computer Desk', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='white').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        computer_desk_txt = Entry(F2, width=10,textvariable=self.computer_desk, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=3, column=1, padx=10, pady=10)

        # bookcase label and entry box
        bookcase_lbl = Label(F2, text='Book Case (large)', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='white').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        bookcase_text = Entry(F2, width=10, textvariable=self.bookcase, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=4, column=1, padx=10, pady=10)

        # armchair label and entry box
        armchair_lbl = Label(F2, text='Arm Chair', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='white').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        armchair_txt = Entry(F2, width=10,textvariable=self.armchair, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1,padx=10, pady=10)

        # frame Furniture
        F3 = LabelFrame(self.root, bd=10, relief=SUNKEN, text="Furniture",
        font=("times new roman",15,"bold"),fg='lightskyblue', bg=bg_colour)
        F3.place(x=380, y=180, width=375, height=380)

        # mirror label and entry box
        mirror_lbl = Label(F3, text='Mirror', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='white').grid(row=0, column=0, padx=10, pady=10, sticky='w')
        mirror_txt = Entry(F3, width=10,textvariable=self.mirror, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=0, column=1,padx=10, pady=10)

        # baby_cradle label and entry box
        baby_cradle_lbl = Label(F3, text='Baby Cradle', font=('times new roman', 15, 'bold'), bg=bg_colour, fg='white').grid(row=1, column=0, padx=10, pady=10, sticky='w')
        baby_cradle_txt = Entry(F3, width=10,textvariable=self.baby_cradle, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        # bench label and entry box
        bench_lbl = Label(F3, text='Bench', font=('times new roman', 15, 'bold'), bg=bg_colour,fg='white').grid(row=2, column=0, padx=10, pady=10, sticky='w')
        bench_txt = Entry(F3, width=10,textvariable=self.bench, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        # cupboard label and entry box
        flour_lbl = Label(F3, text='Cupboard', font=('times new roman', 15, 'bold'), bg=bg_colour,fg='white').grid(row=3, column=0, padx=10, pady=10, sticky='w')
        flour_txt = Entry(F3, width=10,textvariable=self.cupboard, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        # dressing_table label and entry box
        dressing_table_lbl = Label(F3, text='Dressing Table', font=('times new roman', 15, 'bold'), bg=bg_colour,fg='white').grid(row=4, column=0, padx=10, pady=10, sticky='w')
        dressing_table_txt = Entry(F3, width=10,textvariable=self.dressing_table, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=4,column=1, padx=10,pady=10)

        # dresser label and entry box
        dresser_lbl = Label(F3, text='Dresser', font=('times new roman', 15, 'bold'), bg=bg_colour,fg='white').grid(row=5, column=0, padx=10, pady=10, sticky='w')
        dresser_txt = Entry(F3, width=10,textvariable=self.dresser, font=('times new roman', 15, 'bold'), bd=5, relief=SUNKEN).grid(row=5, column=1, padx=10, pady=10)

        # temp list
        F5 = LabelFrame(self.root, bd=10, relief=SUNKEN)
        F5.place(x=760, y=180, width=380, height=380)

        # list title
        receipt_title = Label(F5,text = 'List of Items selected',font="arial 15 bold",bd=7,relief=SUNKEN).pack(fill=X)
        scroll_y = Scrollbar(F5,orient = VERTICAL)
        self.txtarea = Text(F5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txtarea.yview)
        self.txtarea.pack(fill = BOTH, expand = 1)

        # total and tax area
        F6 = LabelFrame(self.root, bd=10, relief=SUNKEN, text="Total", font=("times new roman", 15, "bold"),fg='lightskyblue',bg=bg_colour)
        F6.place(x=0, y=560, relwidth=1, height=140)

        # total price Furniture
        m1_lbl = Label(F6,text='Total Furniture Price',font=('times new roman',14,'bold'),bg=bg_colour,fg="white").grid(row=0,column=0,padx=20,pady=1,sticky='w')
        m1_txt = Entry(F6,width=18,font="arial 10 bold",textvariable=self.Furniture_price,bd=8,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        # total weight Furniture
        m2_lbl = Label(F6, text='Total Furniture Weight', font=('times new roman', 14, 'bold'), bg=bg_colour,fg="white").grid(row=1, column=0, padx=20, pady=1, sticky='w')
        m2_txt = Entry(F6, width=18, font="arial 10 bold",textvariable=self.Furniture_weight, bd=8, relief=SUNKEN).grid(row=1, column=1, padx=10, pady=1)

        # Furniture tax
        c1_lbl = Label(F6, text='Furniture Tax', font=('times new roman', 14, 'bold'), bg=bg_colour, fg="white").grid(row=0, column=2, padx=20, pady=1, sticky='w')
        c1_txt = Entry(F6, width=18, font="arial 10 bold", bd=8,textvariable=self.Furniture_tax, relief=SUNKEN).grid(row=0, column=3, padx=10, pady=1)

        # buttons
        btn_frame =Frame(F6,bd=7,relief=SUNKEN)
        btn_frame.place(x=750,width=700,height=105)

        # total button
        total_btn = Button(btn_frame,command=self.total,text='Total',bg='red',fg='white',pady=15,width= 10,bd=2,font="arial 15 bold").grid(row=0,column=0,padx=20,pady=5)

        # generate list button
        g_btn = Button(btn_frame, text='Generate\nList',command=self.temp_receipt_area, bg='red', fg='white', pady=5, width=10, bd=2, font="arial 15 bold").grid(row=0, column=1, padx=20, pady=5)

        # generate final list button
        o_btn = Button(btn_frame, text='Generate\nFinal List',command=self.main_receipt_area, bg='green', fg='white', pady=5, width=10, bd=2, font="arial 15 bold").grid(row=0, column=2, padx=20, pady=5)

        # generate PDF button
        p_btn = Button(btn_frame, text='Generate\nPDF',command=self.export_pdf, bg='green', fg='white', pady=5, width=10, bd=2, font="arial 15 bold").grid(row=0, column=3, padx=20, pady=5)

        #final LIST OF ITEMS
        # Final List
        F9 = LabelFrame(self.root, bd=10, relief=SUNKEN)
        F9.place(x=1160, y=180, width=380, height=380)

        # List title
        receipt_titl = Label(F9,text='EXPORT INVOICE',font="arial 15 bold",bd=7,relief=SUNKEN).pack(fill=X)
        scroll_yy = Scrollbar(F9,orient=VERTICAL)
        self.text_main=Text(F9,yscrollcommand=scroll_yy.set)
        scroll_yy.pack(side=RIGHT,fill=Y)
        scroll_yy.config(command=self.text_main.yview)
        self.text_main.pack(fill=BOTH,expand =1)

    # defining function for total cost
    def total(self):
        # defining price and calculating its cost
        self.c_s_p= self.sofa.get() * 40000
        self.c_fc_p= self.dining_table.get() * 100000
        self.c_fw_p= self.dining_chairs.get() * 18000
        self.c_bookcase_p= self.bookcase.get() * 18000
        self.c_g_p= self.computer_desk.get() * 20000
        self.c_l_p= self.armchair.get() * 50000
        self.g_r_p = self.mirror.get() * 20000
        self.g_baby_cradle_p = self.baby_cradle.get() * 25000
        self.g_l_p = self.bench.get() * 25000
        self.g_f_p = self.cupboard.get() * 110000
        self.g_s_p = self.dressing_table.get() * 35000
        self.g_st_p = self.dresser.get() * 60000

        # computing total value for Furniture
        if self.c_s_p >= 0 and self.c_fc_p >= 0 and self.c_fw_p >= 0 and self.c_bookcase_p >=0 and self.c_g_p >= 0 and self.c_l_p >= 0:
            self.total_cosmetic_price = float(
            self.c_s_p+
            self.c_fc_p+
            self.c_fw_p+
            self.c_bookcase_p+
            self.c_g_p+self.g_r_p+
            self.g_baby_cradle_p+
            self.g_l_p+
            self.g_f_p+
            self.g_s_p+
            self.g_st_p+
            self.c_l_p
            )
        else:
            messagebox.showerror("Error", "Quantity should be a positive integer")

        # setting furniture total and tax
        self.Furniture_price.set("Rs. "+str(self.total_cosmetic_price))
        self.c_tax=round((self.total_cosmetic_price * 0.07),2)
        self.Furniture_tax.set("Rs. "+str(self.c_tax))

        #defining weight and calculating its total weight
        self.c_s_w= self.sofa.get() * 200
        self.c_fc_w= self.dining_table.get() * 250
        self.c_fw_w= self.dining_chairs.get() * 60
        self.c_bookcase_w= self.bookcase.get() * 240
        self.c_g_w= self.computer_desk.get() * 180
        self.c_l_w= self.armchair.get() * 140
        self.g_r_w = self.mirror.get() * 150
        self.g_baby_cradle_w = self.baby_cradle.get() * 140
        self.g_l_w = self.bench.get() * 180
        self.g_f_w = self.cupboard.get() * 580
        self.g_s_w = self.dressing_table.get() * 200
        self.g_st_w = self.dresser.get() * 450

        #computing total weight for all furniture
        self.total_Furniture_weight = float(
            self.c_s_w+
            self.c_fc_w+
            self.c_fw_w+
            self.c_bookcase_w+
            self.c_g_w+
            self.c_l_w+
            self.g_r_w+
            self.g_baby_cradle_w+
            self.g_l_w+
            self.g_f_w+
            self.g_s_w+
            self.g_st_w
        )
        self.Furniture_weight.set(str(self.total_Furniture_weight)+ ' kg')
        self.total_weight = round(float(self.total_Furniture_weight))                   #computing total weight
        self.total_shipment = round(float(self.total_cosmetic_price+ self.c_tax),3)     # computing total shipment

    # generating orignal list of items
    def temp_receipt(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END, "\tWelcome to lala exports\n")
        self.txtarea.insert(END, "\tWeight limit = 20,000 KG\n")
        self.txtarea.insert(END, f"\nHere is your selected list of items ")
        self.txtarea.insert(END, "\n==========================================")
        self.txtarea.insert(END, "\nProducts\t\tQTY\tWeight \tPrice ")
        self.txtarea.insert(END, "\n==========================================")

    # Exporting PDF function
    def export_pdf(self):
        input_filename = 'receipt.txt'
        output_filename = 'output.pdf'
        self.file = open(input_filename)
        text = self.file.read()
        self.file.close()
        self.text_to_pdf(text, output_filename)

    # generating revised list of items
    def main_receipt(self):
        self.file = open("receipt.txt", "w")
        self.text_main.delete('1.0',END)
        self.text_main.insert(END, "\tWelcome to lala exports\n")
        self.file.write("\tWelcome to lala exports\n")
        self.text_main.insert(END, "\tWeight limit = 20,000 KG\n")
        self.file.write("\tWeight limit = 20,000 KG\n")
        self.text_main.insert(END, "\nHere is your revised list of items\n")
        self.file.write("\nHere is your revised list of items\n")
        self.text_main.insert(END, f"\nshipment Number: {self.shipment_no.get()} ")
        self.file.write(f"\nshipment Number: {self.shipment_no.get()} ")
        self.text_main.insert(END, f"\nCustomer Name: {self.name.get()}")
        self.file.write(f"\nCustomer Name: {self.name.get()}")
        self.text_main.insert(END, f"\nPhone Number: {self.phone_no.get()}")
        self.file.write(f"\nPhone Number: {self.phone_no.get()}")
        self.text_main.insert(END, "\n==========================================")
        self.file.write("\n=========================================================")
        self.text_main.insert(END, "\nProducts\t\tQTY\tWeight \tPrice ")
        self.file.write("\nProducts\t\tQTY\tWeight \tPrice ")
        self.text_main.insert(END, "\n==========================================")
        self.file.write("\n=========================================================")

    # helper functions for heap sort
    def left(self, i):
        return 2 * i + 1
    
    def right(self, i):
        return 2 * i + 2
    
    def max_heapify(self, A,n,i):
        l = self.left(i)
        r = self.right(i)
        if l < n and A[l] < A[i]:
            largest = l
        else:
            largest = i
        if r < n and A[r] < A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(A,n, largest)

    # heap sort
    def build_max_heap(self, A):
        n = len(A)
        for i in range(n, -1,-1):
            self.max_heapify(A,n, i)
        for i in range(n-1,0,-1):
            A[0],A[i]=A[i],A[0]
            self.max_heapify(A,i,0)

    # knapsack implementation
    def knapsack(self,lst, max):
        self.bag = []
        self.total_price = 0
        self.max_weight = 0
        for i in range(len(lst)):
            if lst[i][2] <= max:
                self.bag.append(lst[i][-1])
                self.total_price += lst[i][1]
                self.max_weight += lst[i][2]
                max -= lst[i][2]
            else:
                continue

    # function for list of items area
    def temp_receipt_area(self):
        if self.name.get()== "" or self.phone_no.get()=="":
            messagebox.showerror("Error","Customer Details not found") # receipt will not generate if customer details are not found
        elif self.Furniture_price.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Selected") # receipt will not generate if products are not found
        else:
            self.temp_receipt()

            # checking every item for printing on list of items
            if self.sofa.get() > 0:
                self.thelist.append([round(self.c_s_p/self.c_s_w), self.c_s_p, self.c_s_w, "Sofa Set"])
                self.txtarea.insert(END, f"\nSofa Set\t\t{self.sofa.get()}\t{self.c_s_w}\t{self.c_s_p}")
            if self.dining_table.get() > 0:
                self.thelist.append([round(self.c_fc_p/self.c_fc_w), self.c_fc_p, self.c_fc_w, "Dining Table"])
                self.txtarea.insert(END, f"\nDining Table\t\t{self.dining_table.get()}\t{self.c_fc_w}\t{self.c_fc_p}")
            if self.dining_chairs.get() > 0:
                self.thelist.append([round(self.c_fw_p/self.c_fw_w), self.c_fw_p, self.c_fw_w, "Dining Chairs"])
                self.txtarea.insert(END, f"\nDining Chairs\t\t{self.dining_chairs.get()}\t{self.c_fw_w}\t{self.c_fw_p}")
            if self.bookcase.get() > 0:
                self.thelist.append([round(self.c_bookcase_p/self.c_bookcase_w), self.c_bookcase_p, self.c_bookcase_w, "Book Case"])
                self.txtarea.insert(END, f"\nBook Case\t\t{self.bookcase.get()}\t{self.c_bookcase_w}\t{self.c_bookcase_p}")
            if self.computer_desk.get() > 0:
                self.thelist.append([round(self.c_g_p/self.c_g_w), self.c_g_p, self.c_g_w, "Computer Desk"])
                self.txtarea.insert(END, f"\nComputer Desk\t\t{self.computer_desk.get()}\t{self.c_g_w}\t{self.c_g_p}")
            if self.armchair.get() > 0:
                self.thelist.append([round(self.c_l_p/self.c_l_w), self.c_l_p, self.c_l_w, "Arm Chair"])
                self.txtarea.insert(END, f"\nArm Chair\t\t{self.armchair.get()}\t{self.c_l_w}\t{self.c_l_p}")
            if self.mirror.get() > 0:
                self.thelist.append([round(self.g_r_p/self.g_r_w), self.g_r_p, self.g_r_w, "Mirror"])
                self.txtarea.insert(END, f"\nMirror\t\t{self.mirror.get()}\t{self.g_r_w}\t{self.g_r_p}")
            if self.baby_cradle.get() > 0:
                self.thelist.append([round(self.g_baby_cradle_p/self.g_baby_cradle_w), self.g_baby_cradle_p, self.g_baby_cradle_w, "Baby Cradle"])
                self.txtarea.insert(END, f"\nBaby Cradle\t\t{self.baby_cradle.get()}\t{self.g_baby_cradle_w}\t{self.g_baby_cradle_p}")
            if self.bench.get() > 0:
                self.thelist.append([round(self.g_l_p/self.g_l_w), self.g_l_p, self.g_l_w, "Self bench"])
                self.txtarea.insert(END, f"\nBench\t\t{self.bench.get()}\t{self.g_l_w}\t{self.g_l_p}")
            if self.cupboard.get() > 0:
                self.thelist.append([round(self.g_f_p/self.g_f_w), self.g_f_p,self.g_f_w, "Cupboard"])
                self.txtarea.insert(END, f"\nCupboard\t\t{self.cupboard.get()}\t{self.g_f_w}\t{self.g_f_p}")
            if self.dressing_table.get() > 0:
                self.thelist.append([round(self.g_s_p/self.g_s_w), self.g_s_p,self.g_s_w, "Dressing table"])
                self.txtarea.insert(END, f"\nDressing Table\t\t{self.dressing_table.get()}\t{self.g_s_w}\t{self.g_s_p}")
            if self.dresser.get() > 0:
                self.thelist.append([round(self.g_st_p/self.g_st_w), self.g_st_p, self.g_st_w, "Dresser"])
                self.txtarea.insert(END, f"\nDresser\t\t{self.dresser.get()}\t{self.g_st_w}\t{self.g_st_p}")
            self.txtarea.insert(END, "\n------------------------------------------")
            
            if self.Furniture_tax.get() != 'Rs. 0.0':
                self.total_tax = round(float (self.c_tax),3)
                self.txtarea.insert(END, f"\nTotal Tax on items\t\t\t Rs:{self.total_tax} ")

            self.txtarea.insert(END, f"\nTotal Value of items: \t\t\t Rs:{self.total_shipment} ")
            self.txtarea.insert(END, f"\nTotal Weight of items: \t\t\t{self.total_weight} KG ")
            self.txtarea.insert(END, "\n------------------------------------------\n")
            self.txtarea.insert(END, "\nThank you for choosing lala exports.")
            self.txtarea.insert(END, "\n------------------------------------------")

    # function for final list of items area
    def main_receipt_area(self):
        self.main_receipt()
        self.build_max_heap(self.thelist)
        self.knapsack(self.thelist,20000)
        for item in self.bag:
            if item == "Sofa Set":
                self.text_main.insert(END, f"\nSofa Set\t\t{self.sofa.get()}\t{self.c_s_w}\t{self.c_s_p}")
                self.file.write(f"\nSofa Set\t\t{self.sofa.get()}\t{self.c_s_w}\t{self.c_s_p}")
            elif item == "Dining Table":
                self.text_main.insert(END, f"\nDining Table\t\t{self.dining_table.get()}\t{self.c_fc_w}\t{self.c_fc_p}")
                self.file.write(f"\nDining Table\t\t{self.dining_table.get()}\t{self.c_fc_w}\t{self.c_fc_p}")
            elif item == "Dining Chairs":
                self.text_main.insert(END, f"\nDining Chairs\t\t{self.dining_chairs.get()}\t{self.c_fw_w}\t{self.c_fw_p}")
                self.file.write(f"\nDining Chairs\t\t{self.dining_chairs.get()}\t{self.c_fw_w}\t{self.c_fw_p}")
            elif item == "Book Case":
                self.text_main.insert(END, f"\nBook Case\t\t{self.bookcase.get()}\t{self.c_bookcase_w}\t{self.c_bookcase_p}")
                self.file.write(f"\nBook Case\t\t{self.bookcase.get()}\t{self.c_bookcase_w}\t{self.c_bookcase_p}")
            elif item == "Computer Desk":
                self.text_main.insert(END, f"\nComputer Desk\t\t{self.computer_desk.get()}\t{self.c_g_w}\t{self.c_g_p}")
                self.file.write(f"\nComputer Desk\t\t{self.computer_desk.get()}\t{self.c_g_w}\t{self.c_g_p}")
            elif item == "Arm Chair":
                self.text_main.insert(END, f"\nArm Chair\t\t{self.armchair.get()}\t{self.c_l_w}\t{self.c_l_p}")
                self.file.write(f"\nArm Chair\t\t{self.armchair.get()}\t{self.c_l_w}\t{self.c_l_p}")
            elif item == "Mirror":
                self.text_main.insert(END, f"\nMirror\t\t{self.mirror.get()}\t{self.g_r_w}\t{self.g_r_p}")
                self.file.write(f"\nMirror\t\t{self.mirror.get()}\t{self.g_r_w}\t{self.g_r_p}")
            elif item == "Baby Cradle":
                self.text_main.insert(END, f"\nBaby Cradle\t\t{self.baby_cradle.get()}\t{self.g_baby_cradle_w}\t{self.g_baby_cradle_p}")
                self.file.write(f"\nBaby Cradle\t\t{self.baby_cradle.get()}\t{self.g_baby_cradle_w}\t{self.g_baby_cradle_p}")
            elif item == "Bench":
                self.text_main.insert(END, f"\nBench\t\t{self.bench.get()}\t{self.g_l_w}\t{self.g_l_p}")
                self.file.write(f"\nBench\t\t{self.bench.get()}\t{self.g_l_w}\t{self.g_l_p}")
            elif item == "Cupboard":
                self.text_main.insert(END, f"\nCupboard\t\t{self.cupboard.get()}\t{self.g_f_w}\t{self.g_f_p}")
                self.file.write(f"\nCupboard\t\t{self.cupboard.get()}\t{self.g_f_w}\t{self.g_f_p}")
            elif item == "Dressing Table":
                self.text_main.insert(END, f"\nDressing Table\t\t{self.dressing_table.get()}\t{self.g_s_w}\t{self.g_s_p}")
                self.file.write(f"\nDressing Table\t\t{self.dressing_table.get()}\t{self.g_s_w}\t{self.g_s_p}")
            elif item == "Dresser":
                self.text_main.insert(END, f"\nDresser\t\t{self.dresser.get()}\t{self.g_st_w}\t{self.g_st_p}")
                self.file.write(f"\nDresser \t\t{self.dresser.get()}\t{self.g_st_w}\t{self.g_st_p}")

        self.text_main.insert(END, "\n------------------------------------------\n")
        self.file.write("\n--------------------------------------------------------\n")
        print(self.text_main.get('1.0', END))

        if self.Furniture_tax.get() != 'Rs. 0.0':
            self.total_tax = round(float (self.c_tax),3)
            self.text_main.insert(END, f"\nTotal Tax on items\t\t\t Rs:{self.total_tax} ")
            self.file.write(f"\nTotal Tax on items\t\t\t Rs:{self.total_tax}")
            
        self.text_main.insert(END, f"\nTotal Value of items: \t\t\t Rs:{self.total_price} ")
        self.file.write(f"\nTotal Value of items: \t\t\t Rs:{self.total_price} ")
        self.text_main.insert(END, f"\nTotal Weight of items: \t\t\t{self.max_weight} KG ")
        self.file.write(f"\nTotal Weight of items: \t\t\t {self.max_weight} KG ")
        self.text_main.insert(END, "\n------------------------------------------\n")
        self.file.write("\n--------------------------------------------------------\n")
        self.text_main.insert(END, "\nThank you for choosing lala exports.")
        self.file.write("\nThank you for choosing lala exports.")
        self.text_main.insert(END, "\n------------------------------------------")
        self.file.write("\n--------------------------------------------------------")
        self.file.close()

    def text_to_pdf(self, text, filename):
        print("pdf generated")
        a4_width_mm = 210
        pt_to_mm = 0.35
        fontsize_pt = 10
        fontsize_mm = fontsize_pt * pt_to_mm
        margin_bottom_mm = 10
        character_width_mm = 7 * pt_to_mm
        width_text = a4_width_mm / character_width_mm
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.set_auto_page_break(True, margin=margin_bottom_mm)
        pdf.add_page()
        pdf.set_font(family='Courier', size=fontsize_pt)
        splitted = text.split('\n')
        for line in splitted:
            lines = textwrap.wrap(line, width_text)
            if len(lines) == 0:
                pdf.ln()
            for wrap in lines:
                pdf.cell(0, fontsize_mm, wrap, ln=1)
        pdf.output(filename, 'F')

# calling the class
root = Tk()
obj = export_knapsack(root)
root.mainloop()