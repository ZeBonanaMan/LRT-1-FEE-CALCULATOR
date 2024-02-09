import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def calculate_fare():
    source = clicked_source.get()
    destination = clicked_destination.get()
    
    if source == 'Select A Station' or destination == 'Select A Station':
        fare_label.config(text="\nPlease enter both current location and destination.")
        return
    try:
        beep_fare = beep_get_fare(source, destination)
        sjc_fare = sjc_get_fare(source, destination)
        discounted_fare = sjc_fare - int(sjc_fare) * 0.20
    except TypeError:
        beep_fare is None
        sjc_fare is None
 
    beep_fare = str(beep_fare)
    sjc_fare = str(sjc_fare)
    beep_fare_label.config(text=f" BEEP Card: ₱{beep_fare}")
    sjc_fare_label.config(text=f" Single Journey Card: ₱{sjc_fare}\n" 
                                f" Student/Senior/PWD: ₱{int(discounted_fare)}")
    fare_label.config(text=f"\nFrom: {source}  To: {destination}\n\n")

#BEEP CARD
def beep_get_fare(source, destination):
    fare_prices = {
        ('Recto','Recto'): 0,
        ('Recto','Legarda'): 15,
        ('Recto','Pureza'): 16,
        ('Recto','V.Mapa'): 18,
        ('Recto','J.Ruiz'): 19,
        ('Recto','Gilmore'): 21,
        ('Recto','Betty Go-Belmonte'): 22,
        ('Recto','Araneta Center-Cubao'): 23,
        ('Recto','Anonas'): 25,
        ('Recto','Katipunan'): 26,
        ('Recto','Santolan'): 28,
        ('Recto','Marikina-Pasig'): 31,
        ('Recto','Antipolo'): 33,
        ('Legarda','Recto'): 15,
        ('Legarda','Legarda'): 0,
        ('Legarda','Pureza'): 15,
        ('Legarda','V.Mapa'): 17,
        ('Legarda','J.Ruiz'): 18,
        ('Legarda','Gilmore'): 19,
        ('Legarda','Betty Go-Belmonte'): 21,
        ('Legarda','Araneta Center-Cubao'): 22,
        ('Legarda','Anonas'): 24,
        ('Legarda','Katipunan'): 25,
        ('Legarda','Santolan'): 27,
        ('Legarda','Marikina-Pasig'): 29,
        ('Legarda','Antipolo'): 32,
        ('Pureza','Recto'): 16,
        ('Pureza','Legarda'): 15,
        ('Pureza','Pureza'): 0,
        ('Pureza','V.Mapa'): 15,
        ('Pureza','J.Ruiz'): 16,
        ('Pureza','Gilmore'): 18,
        ('Pureza','Betty Go-Belmonte'): 19,
        ('Pureza','Araneta Center-Cubao'): 20,
        ('Pureza','Anonas'): 22,
        ('Pureza','Katipunan'): 23,
        ('Pureza','Santolan'): 26,
        ('Pureza','Marikina-Pasig'): 28,
        ('Pureza','Antipolo'): 30,
        ('V.Mapa','Recto'): 18,
        ('V.Mapa','Legarda'): 17,
        ('V.Mapa','Pureza'): 15,
        ('V.Mapa','V.Mapa'): 0,
        ('V.Mapa','J.Ruiz'): 15,
        ('V.Mapa','Gilmore'): 16,
        ('V.Mapa','Betty Go-Belmonte'): 17,
        ('V.Mapa','Araneta Center-Cubao'): 19,
        ('V.Mapa','Anonas'): 20,
        ('V.Mapa','Katipunan'): 22,
        ('V.Mapa','Santolan'): 24,
        ('V.Mapa','Marikina-Pasig'): 26,
        ('V.Mapa','Antipolo'): 29,
        ('J.Ruiz','Recto'): 19,
        ('J.Ruiz','Legarda'): 18,
        ('J.Ruiz','Pureza'): 16,
        ('J.Ruiz','V.Mapa'): 15,
        ('J.Ruiz','J.Ruiz'): 0,
        ('J.Ruiz','Gilmore'): 14,
        ('J.Ruiz','Betty Go-Belmonte'): 16,
        ('J.Ruiz','Araneta Center-Cubao'): 17,
        ('J.Ruiz','Anonas'): 19,
        ('J.Ruiz','Katipunan'): 20,
        ('J.Ruiz','Santolan'): 22,
        ('J.Ruiz','Marikina-Pasig'): 24,
        ('J.Ruiz','Antipolo'): 27,
        ('Gilmore','Recto'): 21,
        ('Gilmore','Legarda'): 19,
        ('Gilmore','Pureza'): 18,
        ('Gilmore','V.Mapa'): 16,
        ('Gilmore','J.Ruiz'): 14,
        ('Gilmore','Gilmore'): 0,
        ('Gilmore','Betty Go-Belmonte'): 15,
        ('Gilmore','Araneta Center-Cubao'): 16,
        ('Gilmore','Anonas'): 18,
        ('Gilmore','Katipunan'): 19,
        ('Gilmore','Santolan'): 21,
        ('Gilmore','Marikina-Pasig'): 23,
        ('Gilmore','Antipolo'): 26,
        ('Betty Go-Belmonte','Recto'): 22,
        ('Betty Go-Belmonte','Legarda'): 21,
        ('Betty Go-Belmonte','Pureza'): 19,
        ('Betty Go-Belmonte','V.Mapa'): 17,
        ('Betty Go-Belmonte','J.Ruiz'): 16,
        ('Betty Go-Belmonte','Gilmore'): 15,
        ('Betty Go-Belmonte','Betty Go-Belmonte'): 0,
        ('Betty Go-Belmonte','Araneta Center-Cubao'): 15,
        ('Betty Go-Belmonte','Anonas'): 16,
        ('Betty Go-Belmonte','Katipunan'): 18,
        ('Betty Go-Belmonte','Santolan'): 20,
        ('Betty Go-Belmonte','Marikina-Pasig'): 22,
        ('Betty Go-Belmonte','Antipolo'): 25,
        ('Araneta Center-Cubao','Recto'): 23,
        ('Araneta Center-Cubao','Legarda'): 22,
        ('Araneta Center-Cubao','Pureza'): 20,
        ('Araneta Center-Cubao','V.Mapa'): 19,
        ('Araneta Center-Cubao','J.Ruiz'): 17,
        ('Araneta Center-Cubao','Gilmore'): 16,
        ('Araneta Center-Cubao','Betty Go-Belmonte'): 15,
        ('Araneta Center-Cubao','Araneta Center-Cubao'): 0,
        ('Araneta Center-Cubao','Anonas'): 15,
        ('Araneta Center-Cubao','Katipunan'): 16,
        ('Araneta Center-Cubao','Santolan'): 19,
        ('Araneta Center-Cubao','Marikina-Pasig'): 21,
        ('Araneta Center-Cubao','Antipolo'): 23,
        ('Anonas','Recto'): 25,
        ('Anonas','Legarda'): 24,
        ('Anonas','Pureza'): 22,
        ('Anonas','V.Mapa'): 20,
        ('Anonas','J.Ruiz'): 19,
        ('Anonas','Gilmore'): 18,
        ('Anonas','Betty Go-Belmonte'): 16,
        ('Anonas','Araneta Center-Cubao'): 15,
        ('Anonas','Anonas'): 0,
        ('Anonas','Katipunan'): 14,
        ('Anonas','Santolan'): 17,
        ('Anonas','Marikina-Pasig'): 19,
        ('Anonas','Antipolo'): 22,
        ('Katipunan','Recto'): 26,
        ('Katipunan','Legarda'): 25,
        ('Katipunan','Pureza'): 23,
        ('Katipunan','V.Mapa'): 22,
        ('Katipunan','J.Ruiz'): 20,
        ('Katipunan','Gilmore'): 19,
        ('Katipunan','Betty Go-Belmonte'): 18,
        ('Katipunan','Araneta Center-Cubao'): 16,
        ('Katipunan','Anonas'): 14,
        ('Katipunan','Katipunan'): 0,
        ('Katipunan','Santolan'): 16,
        ('Katipunan','Marikina-Pasig'): 18,
        ('Katipunan','Antipolo'): 21,
        ('Santolan','Recto'): 28,
        ('Santolan','Legarda'): 27,
        ('Santolan','Pureza'): 26,
        ('Santolan','V.Mapa'): 24,
        ('Santolan','J.Ruiz'): 22,
        ('Santolan','Gilmore'): 21,
        ('Santolan','Betty Go-Belmonte'): 20,
        ('Santolan','Araneta Center-Cubao'): 19,
        ('Santolan','Anonas'): 17,
        ('Santolan','Katipunan'): 16,
        ('Santolan','Santolan'): 0,
        ('Santolan','Marikina-Pasig'): 15,
        ('Santolan','Antipolo'): 18,
        ('Marikina-Pasig','Recto'): 31,
        ('Marikina-Pasig','Legarda'): 29,
        ('Marikina-Pasig','Pureza'): 28,
        ('Marikina-Pasig','V.Mapa'): 26,
        ('Marikina-Pasig','J.Ruiz'): 24,
        ('Marikina-Pasig','Gilmore'): 23,
        ('Marikina-Pasig','Betty Go-Belmonte'): 22,
        ('Marikina-Pasig','Araneta Center-Cubao'): 21,
        ('Marikina-Pasig','Anonas'): 19,
        ('Marikina-Pasig','Katipunan'): 18,
        ('Marikina-Pasig','Santolan'): 15,
        ('Marikina-Pasig','Marikina-Pasig'): 0,
        ('Marikina-Pasig','Antipolo'): 16,
        ('Antipolo','Recto'): 33,
        ('Antipolo','Legarda'): 32,
        ('Antipolo','Pureza'): 30,
        ('Antipolo','V.Mapa'): 29,
        ('Antipolo','J.Ruiz'): 27,
        ('Antipolo','Gilmore'): 26,
        ('Antipolo','Betty Go-Belmonte'): 25,
        ('Antipolo','Araneta Center-Cubao'): 23,
        ('Antipolo','Anonas'): 22,
        ('Antipolo','Katipunan'): 21,
        ('Antipolo','Santolan'): 19,
        ('Antipolo','Marikina-Pasig'): 16,
        ('Antipolo','Antipolo'): 0
    }
        
    if (source, destination) in fare_prices:
        return fare_prices[(source, destination)]

#SINGLE JOURNEY TICKET AND DISCOUNTED
def sjc_get_fare(source, destination):
    fare_prices = {
        ('Recto','Recto'): 0,
        ('Recto','Legarda'): 15,
        ('Recto','Pureza'): 20,
        ('Recto','V.Mapa'): 20,
        ('Recto','J.Ruiz'): 20,
        ('Recto','Gilmore'): 25,
        ('Recto','Betty Go-Belmonte'): 25,
        ('Recto','Araneta Center-Cubao'): 25,
        ('Recto','Anonas'): 25,
        ('Recto','Katipunan'): 30,
        ('Recto','Santolan'): 30,
        ('Recto','Marikina-Pasig'): 35,
        ('Recto','Antipolo'): 35,
        ('Legarda','Recto'): 15,
        ('Legarda','Legarda'): 0,
        ('Legarda','Pureza'): 15,
        ('Legarda','V.Mapa'): 20,
        ('Legarda','J.Ruiz'): 20,
        ('Legarda','Gilmore'): 20,
        ('Legarda','Betty Go-Belmonte'): 25,
        ('Legarda','Araneta Center-Cubao'): 25,
        ('Legarda','Anonas'): 25,
        ('Legarda','Katipunan'): 25,
        ('Legarda','Santolan'): 30,
        ('Legarda','Marikina-Pasig'): 30,
        ('Legarda','Antipolo'): 35,
        ('Pureza','Recto'): 20,
        ('Pureza','Legarda'): 15,
        ('Pureza','Pureza'): 0,
        ('Pureza','V.Mapa'): 15,
        ('Pureza','J.Ruiz'): 20,
        ('Pureza','Gilmore'): 20,
        ('Pureza','Betty Go-Belmonte'): 20,
        ('Pureza','Araneta Center-Cubao'): 20,
        ('Pureza','Anonas'): 25,
        ('Pureza','Katipunan'): 25,
        ('Pureza','Santolan'): 30,
        ('Pureza','Marikina-Pasig'): 30,
        ('Pureza','Antipolo'): 30,
        ('V.Mapa','Recto'): 20,
        ('V.Mapa','Legarda'): 20,
        ('V.Mapa','Pureza'): 15,
        ('V.Mapa','V.Mapa'): 0,
        ('V.Mapa','J.Ruiz'): 15,
        ('V.Mapa','Gilmore'): 20,
        ('V.Mapa','Betty Go-Belmonte'): 20,
        ('V.Mapa','Araneta Center-Cubao'): 20,
        ('V.Mapa','Anonas'): 20,
        ('V.Mapa','Katipunan'): 25,
        ('V.Mapa','Santolan'): 25,
        ('V.Mapa','Marikina-Pasig'): 30,
        ('V.Mapa','Antipolo'): 30,
        ('J.Ruiz','Recto'): 20,
        ('J.Ruiz','Legarda'): 20,
        ('J.Ruiz','Pureza'): 20,
        ('J.Ruiz','V.Mapa'): 15,
        ('J.Ruiz','J.Ruiz'): 0,
        ('J.Ruiz','Gilmore'): 15,
        ('J.Ruiz','Betty Go-Belmonte'): 20,
        ('J.Ruiz','Araneta Center-Cubao'): 20,
        ('J.Ruiz','Anonas'): 20,
        ('J.Ruiz','Katipunan'): 20,
        ('J.Ruiz','Santolan'): 25,
        ('J.Ruiz','Marikina-Pasig'): 25,
        ('J.Ruiz','Antipolo'): 30,
        ('Gilmore','Recto'): 25,
        ('Gilmore','Legarda'): 20,
        ('Gilmore','Pureza'): 20,
        ('Gilmore','V.Mapa'): 20,
        ('Gilmore','J.Ruiz'): 15,
        ('Gilmore','Gilmore'): 0,
        ('Gilmore','Betty Go-Belmonte'): 15,
        ('Gilmore','Araneta Center-Cubao'): 20,
        ('Gilmore','Anonas'): 20,
        ('Gilmore','Katipunan'): 20,
        ('Gilmore','Santolan'): 25,
        ('Gilmore','Marikina-Pasig'): 25,
        ('Gilmore','Antipolo'): 30,
        ('Betty Go-Belmonte','Recto'): 25,
        ('Betty Go-Belmonte','Legarda'): 25,
        ('Betty Go-Belmonte','Pureza'): 20,
        ('Betty Go-Belmonte','V.Mapa'): 20,
        ('Betty Go-Belmonte','J.Ruiz'): 20,
        ('Betty Go-Belmonte','Gilmore'): 15,
        ('Betty Go-Belmonte','Betty Go-Belmonte'): 0,
        ('Betty Go-Belmonte','Araneta Center-Cubao'): 15,
        ('Betty Go-Belmonte','Anonas'): 20,
        ('Betty Go-Belmonte','Katipunan'): 20,
        ('Betty Go-Belmonte','Santolan'): 20,
        ('Betty Go-Belmonte','Marikina-Pasig'): 25,
        ('Betty Go-Belmonte','Antipolo'): 25,
        ('Araneta Center-Cubao','Recto'): 25,
        ('Araneta Center-Cubao','Legarda'): 25,
        ('Araneta Center-Cubao','Pureza'): 20,
        ('Araneta Center-Cubao','V.Mapa'): 20,
        ('Araneta Center-Cubao','J.Ruiz'): 20,
        ('Araneta Center-Cubao','Gilmore'): 20,
        ('Araneta Center-Cubao','Betty Go-Belmonte'): 15,
        ('Araneta Center-Cubao','Araneta Center-Cubao'): 0,
        ('Araneta Center-Cubao','Anonas'): 15,
        ('Araneta Center-Cubao','Katipunan'): 20,
        ('Araneta Center-Cubao','Santolan'): 20,
        ('Araneta Center-Cubao','Marikina-Pasig'): 25,
        ('Araneta Center-Cubao','Antipolo'): 25,
        ('Anonas','Recto'): 25,
        ('Anonas','Legarda'): 25,
        ('Anonas','Pureza'): 25,
        ('Anonas','V.Mapa'): 20,
        ('Anonas','J.Ruiz'): 20,
        ('Anonas','Gilmore'): 20,
        ('Anonas','Betty Go-Belmonte'): 20,
        ('Anonas','Araneta Center-Cubao'): 15,
        ('Anonas','Anonas'): 0,
        ('Anonas','Katipunan'): 15,
        ('Anonas','Santolan'): 20,
        ('Anonas','Marikina-Pasig'): 20,
        ('Anonas','Antipolo'): 25,
        ('Katipunan','Recto'): 30,
        ('Katipunan','Legarda'): 25,
        ('Katipunan','Pureza'): 25,
        ('Katipunan','V.Mapa'): 25,
        ('Katipunan','J.Ruiz'): 20,
        ('Katipunan','Gilmore'): 20,
        ('Katipunan','Betty Go-Belmonte'): 20,
        ('Katipunan','Araneta Center-Cubao'): 20,
        ('Katipunan','Anonas'): 15,
        ('Katipunan','Katipunan'): 0,
        ('Katipunan','Santolan'): 20,
        ('Katipunan','Marikina-Pasig'): 20,
        ('Katipunan','Antipolo'): 25,
        ('Santolan','Recto'): 30,
        ('Santolan','Legarda'): 30,
        ('Santolan','Pureza'): 30,
        ('Santolan','V.Mapa'): 25,
        ('Santolan','J.Ruiz'): 25,
        ('Santolan','Gilmore'): 25,
        ('Santolan','Betty Go-Belmonte'): 20,
        ('Santolan','Araneta Center-Cubao'): 20,
        ('Santolan','Anonas'): 20,
        ('Santolan','Katipunan'): 20,
        ('Santolan','Santolan'): 0,
        ('Santolan','Marikina-Pasig'): 15,
        ('Santolan','Antipolo'): 20,
        ('Marikina-Pasig','Recto'): 35,
        ('Marikina-Pasig','Legarda'): 30,
        ('Marikina-Pasig','Pureza'): 30,
        ('Marikina-Pasig','V.Mapa'): 30,
        ('Marikina-Pasig','J.Ruiz'): 25,
        ('Marikina-Pasig','Gilmore'): 25,
        ('Marikina-Pasig','Betty Go-Belmonte'): 25,
        ('Marikina-Pasig','Araneta Center-Cubao'): 25,
        ('Marikina-Pasig','Anonas'): 20,
        ('Marikina-Pasig','Katipunan'): 20,
        ('Marikina-Pasig','Santolan'): 15,
        ('Marikina-Pasig','Marikina-Pasig'): 0,
        ('Marikina-Pasig','Antipolo'): 20,
        ('Antipolo','Recto'): 35,
        ('Antipolo','Legarda'): 35,
        ('Antipolo','Pureza'): 30,
        ('Antipolo','V.Mapa'): 30,
        ('Antipolo','J.Ruiz'): 30,
        ('Antipolo','Gilmore'): 30,
        ('Antipolo','Betty Go-Belmonte'): 25,
        ('Antipolo','Araneta Center-Cubao'): 25,
        ('Antipolo','Anonas'): 25,
        ('Antipolo','Katipunan'): 25,
        ('Antipolo','Santolan'): 20,
        ('Antipolo','Marikina-Pasig'): 20,
        ('Antipolo','Antipolo'): 0,
    }
    if (source, destination) in fare_prices:
        return fare_prices[(source, destination)]

root = tk.Tk()
root.geometry("495x495")
root.title("Railway Price Checker")

bg_color = "#90c72d"
fg_color = "#FFFFFf"
label_color = "#ff5823"

background_image = Image.open('IMAGES/background_image.png')
background_image = ImageTk.PhotoImage(background_image)

beep_image = Image.open("IMAGES/BEEP_cardsprite.png").resize((90,60))
beep_image = ImageTk.PhotoImage(beep_image)

sjc_image = Image.open("IMAGES/SJC_card_sprite.png").resize((90,60))
sjc_image = ImageTk.PhotoImage(sjc_image)

root.config()

clicked_source = StringVar() 
clicked_source.set("Select A Station") 
clicked_destination = StringVar() 
clicked_destination.set("Select A Station") 

background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

destination_dropdown_list = [
    'Recto',
    'Legarda',
    'Pureza',
    'V.Mapa',
    'J.Ruiz',
    'Gilmore',
    'Betty Go-Belmonte',
    'Araneta Center-Cubao',
    'Anonas',
    'Katipunan',
    'Santolan',
    'Marikina-Pasig',
    'Antipolo',
]
source_dropdown_list = [
    'Recto',
    'Legarda',
    'Pureza',
    'V.Mapa',
    'J.Ruiz',
    'Gilmore',
    'Betty Go-Belmonte',
    'Araneta Center-Cubao',
    'Anonas',
    'Katipunan',
    'Santolan',
    'Marikina-Pasig',
    'Antipolo',
]

spacer = tk.Label(bg=bg_color)
spacer.pack()

source_label = tk.Label(root, text="Current Station:", bg=bg_color, fg=fg_color, font=('30'))
source_label.pack(pady=5)
source_dropdown = OptionMenu(root, clicked_source, *source_dropdown_list) 
source_dropdown.config(bg=bg_color, fg=fg_color, font=('20'))
source_dropdown.pack() 

destination_label = tk.Label(root, text="Destination:", bg=bg_color, fg=fg_color, font=('30'))
destination_label.pack(pady=5)
destination_dropdown = OptionMenu(root, clicked_destination, *destination_dropdown_list) 
destination_dropdown.config(bg=bg_color, fg=fg_color, font=('20'))
destination_dropdown.pack() 

calculate_button = tk.Button(root, text="Calculate", command=calculate_fare, bg=bg_color, fg=label_color, font=('20'))
calculate_button.pack(pady=10)

fare_label = tk.Label(root, text="Hello! Welcome to Trip Fare Calculator", bg=bg_color, fg=fg_color, font=('20'))
fare_label.pack(pady=5)
beep_fare_label = tk.Label(root, text="", bg=bg_color, fg=fg_color, image=beep_image, font=('20'), compound="left")
beep_fare_label.pack()
sjc_fare_label = tk.Label(root, text="", bg=bg_color, fg=fg_color, image=sjc_image, font=('20'), compound="left")
sjc_fare_label.pack()

root.mainloop()
