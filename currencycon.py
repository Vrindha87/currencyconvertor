import tkinter as tk
from tkinter import *
from tkinter import ttk
from datetime import datetime
import requests
from PIL import ImageTk, Image
from tkinter import messagebox


root = tk.Tk()
root.geometry("600x270")
root.title("Currency Convertor")
root.iconbitmap('C:\\Users\\91994\\Downloads\\icon.ico')
root.maxsize(600, 270)
root.minsize(600, 270)


image = Image.open('C:\\Users\\91994\\Downloads\\currency.png')
zoom = 0.5
pixels_x, pixels_y = tuple([int(zoom * x) for x in image.size])
img = ImageTk.PhotoImage(image.resize((pixels_x, pixels_y)))
panel = Label(root, image=img)
panel.place(x=190, y=35)


def show_data():
    try:
        amount = E1.get()
        from_currency = c1.get()
        to_currency = c2.get()

        if not amount:
            messagebox.showerror("Currency Convertor", "Please fill in the amount")
            return

        if not to_currency:
            messagebox.showerror("Currency Convertor", "Please choose a currency")
            return

        amount = float(amount)
        
        url = f'https://v6.exchangerate-api.com/v6/your key/latest/USD'
        response = requests.get(url)
        data = response.json()

        
        if data['result'] != 'success':
            messagebox.showerror("Currency Convertor", "Failed to retrieve data from the API")
            return

        
        exchange_rate = data['conversion_rates'][to_currency]
        converted_amount = exchange_rate * amount

    
        E2.delete(0, 'end')
        E2.insert(0, converted_amount)

        
        text.insert('end', f'{amount} {from_currency} equals {converted_amount} {to_currency}\n\nLast Updated: {datetime.now()}\n')

    except ValueError:
        messagebox.showerror("Currency Convertor", "Please enter a valid number for the amount")
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Currency Convertor", f"Network error: {e}")


def clear():
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    text.delete(1.0, 'end')


l1 = Label(root, text="USD Currency Convertor Using Python", font=('verdana', '10', 'bold'))
l1.place(x=150, y=15)

amt = Label(root, text="Amount", font=('roboto', 10, 'bold'))
amt.place(x=20, y=15)
E1 = Entry(root, width=20, borderwidth=1, font=('roboto', 10, 'bold'))
E1.place(x=20, y=40)

c1 = tk.StringVar()
c2 = tk.StringVar()


currencychoose1 = ttk.Combobox(root, width=20, textvariable=c1, state='readonly', font=('verdana', 10, 'bold'))
currencychoose1['values'] = ('USD',)
currencychoose1.place(x=300, y=40)
currencychoose1.current(0)

E2 = Entry(root, width=20, borderwidth=1, font=('roboto', 10, 'bold'))
E2.place(x=20, y=80)


currencychoose2 = ttk.Combobox(root, width=20, textvariable=c2, state='readonly', font=('verdana', 10, 'bold'))
currencychoose2['values'] = ('ALL', 'AFN', 'ARS', 'AWG', 'AUD', 'AZN', 'BSD', 'BBD', 'BYN', 'BZD', 'BMD', 'BOB', 
                             'BAM', 'BWP', 'BGN', 'BND', 'KHR', 'CAD', 'KYD', 'CLP', 'CNY', 'COP', 'CRC', 'HRK', 
                             'CUP', 'CZK', 'DKK', 'DOP', 'XCD', 'EGP', 'SVC', 'EUR', 'FKP', 'FJD', 'GHS', 'GIP', 
                             'GTQ', 'GGP', 'GYD', 'HNL', 'HKD', 'HUF', 'ISK', 'INR', 'IDR', 'IRR', 'IMP', 'ILS', 
                             'JMD', 'JPY', 'KZT', 'KPW', 'KRW', 'KGS', 'LAK', 'LBP', 'LRD', 'MKD', 'MYR', 'MUR', 
                             'MXN', 'MNT', 'MZN', 'NAD', 'NPR', 'ANG', 'NZD', 'NIO', 'NGN', 'NOK', 'OMR', 'PKR', 
                             'PAB', 'PYG', 'PEN', 'PHP', 'PLN', 'QAR', 'RON', 'RUB', 'SHP', 'SAR', 'RSD', 'SCR', 
                             'SGD', 'SBD', 'SOS', 'ZAR', 'LKR', 'SEK', 'CHF', 'SRD', 'SYP', 'TWD', 'THB', 'TTD', 
                             'TRY', 'TVD', 'UAH', 'GBP', 'UYU', 'UZS', 'VEF', 'VND', 'YER', 'ZWD')
currencychoose2.place(x=300, y=80)

text = Text(root, height=7, width=52, font=('verdana', 10, 'bold'))
text.place(x=100, y=120)


B = Button(root, text="Search", command=show_data, font=('verdana', 10, 'bold'), borderwidth=2, bg="red", fg="white")
B.place(x=20, y=120)

clear_btn = Button(root, text="Clear", command=clear, font=('verdana', 10, 'bold'), borderwidth=2, bg="blue", fg="white")
clear_btn.place(x=20, y=170)

root.mainloop()
