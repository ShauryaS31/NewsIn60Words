import requests #to fetch data from the api 
from tkinter import *
from urllib.request import urlopen
from PIL import ImageTk, Image
import io
import webbrowser


class NewsApp:

    def __init__(self):   #constructor 

        #Step 1: fetch data from api 
        self.data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=609d98a65ceb4ea397524ef50128775d").json()
        
        #Step 2: initial load Gui
        self.load_gui() #iska kam hai gui ko load karna
        

        #step 3: load the list of news item
        self.load_news_item(0)
        
    def load_gui(self):
        self.root = Tk()
        self.root.geometry("350x600")
        self.root.resizable(0,0) # we dont want the window to be resized
        self.root.title("Inshorts")
        self.root.configure(background='white')

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def load_news_item(self, index):
    # Clear the screen for the next news item
        self.clear()


        #image- also import urlope from urllib.request
        # you have to find the image url from urlToImage in the same jason file 
        
        try:
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)

        
        except:
            img_url = 'https://www.hhireb.com/wp-content/uploads/2019/08/default-no-img.jpg'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350,250))
            photo = ImageTk.PhotoImage(im)

        label = Label(self.root, image=photo)
        label.pack()


        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='white',fg='black',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',18))

        details = Label(self.root, text=self.data['articles'][index]['description'], bg='White', fg='black', wraplength=350,justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        frame = Frame(self.root, bg ="white")
        frame.pack(expand=True,fill=BOTH)
        

        if index !=0:
            prev_button = Button(frame,text="Prev", width=16, height=3, command=lambda : self.load_news_item(index - 1))
            prev_button.pack(side=LEFT)

        read = Button(frame,text="Read More", width=16, height=3, command=lambda : self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)


        if index != len(self.data["articles"]) -1:
            next_button = Button(frame,text="Next", width=16,height=3, command=lambda : self.load_news_item(index + 1))
            next_button.pack(side=LEFT)

        self.root.mainloop()


    def open_link(self, url):
        webbrowser.open(url)



obj = NewsApp()