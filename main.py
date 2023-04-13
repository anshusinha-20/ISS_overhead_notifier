## challenge: kanye quotes app
# """imported every class from the tkinter module"""
# from tkinter import *
#
# """imported requests module"""
# import requests
#
# """function to get quotes"""
# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#
#     data = response.json()
#     quote = data["quote"]
#
#     canvas.itemconfig(quote_text, text=quote)
#
#
# """created the window object"""
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# """created the canvas object"""
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# """created the kanye_button object"""
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
#
# """loop to keep the window open"""
# window.mainloop()

# --------------------------------------------------------------------

## day33: iss overhead notifier project

"""imported requests module"""
import requests

"""variable to store the response"""
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

"""variable to store the data"""
data = response.json()

"""iss' latitude and longitude"""
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
issPosition = (latitude, longitude)

print(issPosition)