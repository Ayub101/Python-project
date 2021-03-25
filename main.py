from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import webScarpper as wb
import webbrowser as google
import traceback
import os
import voice_search as vs
import time as tm



#--------------------------global function----------------------------------#

#global list to store all searches
lis_of_sear = []
#global list to store all the links of website
lis_of_link = []
#global variable of none type
dt = None
# call func for main result frame of searches
def call(name):
    lis_of_sear.append(name)
    global dt
    if dt is not None:
        #destroy previous search
        dt.detr()
    # take result list from getlis and call search result frame
    dt = product(t, getlis(name))
# use to visit website
# call by visit site button

def visit_link(i):
    #open the website in default Browser
    google.open_new(lis_of_link[i])
    print(lis_of_link)
    print(i)
    #increament i value
    # restart i button with 0 in list ends
#deleting all images
def freeup():
    for i in range(0,7):
        try:
            os.remove(str(i)+".jpg")
        except:
            break
#make Dynamic Button
def mkButton(p,frame):
    return Button(frame, text="Visit site",font=("times new roman ",8,"bold")
                  ,activebackground="yellow", command=lambda: visit_link(p))

#get list of the product
def getlis(na):
   try:
       #making object of web scraping
        wa = wb.webScrapper()
        try:
            #delete the image from directory
            wa.delete()
        except:
            print(" ")
        link = wa.get(na)
        lis = wa.scrapgog(link["Google"])
        wa.download()
        if type(lis)==None:
            raise EXCEPTION("NOT THERE")
        return lis
   except ConnectionResetError as c:
       return "NOT CONNECTED"

   except :
       return "NOT FOUND"

def for_back(command,name,obj):

    global dt
    global back_count
    global forward_count
    if command == "back" and dt is not None:
        if (lis_of_sear.index(name)-1) < 0:
            return
        dt.detr()
        try:
            pr = lis_of_sear[lis_of_sear.index(name)-1]
        except :
            pr = lis_of_sear[0]

        obj.putinSearch(pr)
        try:
            dt = product(t,getlis(pr))
        finally:
            return
    if command == "forward" and dt is not None:
        if (lis_of_sear.index(name)+1) >= len(lis_of_sear):
            return
        dt.detr()
        pr = lis_of_sear[lis_of_sear.index(name)+1]
        obj.putinSearch(pr)
        try:
            dt = product(t, getlis(pr))
        finally:
            return
    return
def imagebutton(frame,p):
    return Button(frame,command=lambda :[show(p)])

#currently working on it
def show(ig):
    #print(.jpg")
    img = Image.open("back.png")
    img = img.resize((300,190),Image.ANTIALIAS)
    img=ImageTk.PhotoImage(img)
    im=Tk()
    im.title("Image")
    im.geometry("152x200")
    can = Canvas(im, width=152,height=200,bg="red")
    #labe =Label(im,image=ig)
    #labe.image=ig
    #labe.pack()
    can.create_image(0,0,image=img,anchor="nw")
    can.pack()

#voice function return take the search from microphone
def voice():
    v = vs.voice_search()
    return v.asist()
#------------------------------------class of frames--------------------------#


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

                                            # HEADER = LOGINPAGE

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

class header():
    # making a top frame
    def __init__(self, t):
        #giving tittle a
        t.title("SKARS Smart Shopping")
        # giving background black color
        t.configure(bg="#000000")
        #giving size to tk window
        t.geometry("990x550")

#previous code

        #top = Frame(t,relief="groove",bd=3)
        #top.config(bg="#2b0092")
        #lab = Label(top, image=bg,relief="groove")
        #lab.pack(side=LEFT,fill="y")
        #name = Label(top,text="SKARS Smart Shopping",font="Arial 38 bold")
        #cname.config(bg="#2b0092",foreground="#ffc770")
        #name.pack(side=LEFT,fill="x",padx=20)
        #top.pack(side=TOP,fill="x")

        #calling login frame
        self.login(t,bg)

    def login(self,t,bg):
        #making a parent frame in which mess and login frame will be pack
                # Creating a message Frame
        #messfr = Frame(bframe,bd=5,bg="#d48352")
        #save = Label(messfr,text="We help you to save money",font="Arial 30 bold",relief="groove",bd=3,bg="#56b6d8")
        #save.pack()

        # using global variable canvas in method
        global canvas
        # creating a login Frame
        bframe = Frame(t, relief="groove", bd=3)
        # resizing image use in button
        #--------------------------------------------------------------------#
        goog = Image.open("googlebut1.jpg")
        goog = goog.resize((250,50),Image.ANTIALIAS)
        goog = ImageTk.PhotoImage(goog)
        log = Image.open("login.jpg")
        log = log.resize((250, 50), Image.ANTIALIAS)
        log = ImageTk.PhotoImage(log)
        #--------------------------------------------------------------------#
        loginfr = Frame(bframe,bg="#e7f7d0",bd=0)
        head = Label(loginfr,text="LOGIN",font="Arial 20 bold",bg="#e7f7d0")
        email = Label(loginfr,text="LOGIN ID:",font="Arial 12 bold",bg="#e7f7d0")
        emid = Entry(loginfr, width=30,bg="#e7f7d0",relief="groove",font="Arial 12 ",bd=2,justify=LEFT)
        paswd = Label(loginfr, text="PASSWORD:",font="Arial 12 bold",bg="#e7f7d0",bd=2)
        password = Entry(loginfr, width=30,bg="#e7f7d0",font="Arial 12 bold",relief="groove",bd=2,show="*")
        #using image as button
        logbtn = Button(loginfr,image=log,bd=0
                       ,command=lambda:[bframe.destroy(),self.enter(t)])
        logbtn.image = log  # -> anchor to image
        createbtn = Button(loginfr, image=goog,bd=0
                         ,command=lambda: [bframe.destroy(),self.enter(t)])
        createbtn.image=goog # -> anchor to image
        # an Empty label to create space or to skip a line using pack
        space = Label(loginfr,text="")

        head.grid(row=0,column=1,columnspan=3,pady=4)
        space.grid(row=1)
        email.grid(row=2,column=2,sticky="w",pady=2,padx=2)
        emid.grid(row=3,column=2,sticky="ew",pady=2,padx=2)
        paswd.grid(row=4,column=2,sticky="w",pady=2,padx=2)
        password.grid(row=5,column=2,sticky="ew",pady=3,padx=2)
        logbtn.grid(row=6,column=2,columnspan=3,pady=5)
        createbtn.grid(row=7,column=2,columnspan=3,pady=5)

        #messfr.pack(side=TOP,fill="x")
        loginfr.pack(fill="y")
        #adding bframe  in canvas
        canvas.create_window(150,120, anchor="nw", window=bframe)
        #bframe.pack(fill=BOTH)

    def enter(self,t):
        # login Button will call this and destroy ist frame
        rside = optionbar(t)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

                                                # OPTION BAR = SEARCHBAR

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

#optionbar have both search and right side frame
class optionbar():
    def __init__(self,t):
        #using canvas global variable
        global canvas
        # destroying old canvas
        canvas.pack_forget()

        #making new background
        #-----------------------------------------------------#

        #resizing iamge use in background
        second = Image.open("high.jpg")
        second = second.resize((990,550),Image.ANTIALIAS)
        second = ImageTk.PhotoImage(second)
        #making background
        canvas = Canvas(parent, width=992, height=700,scrollregion=(0,0,1000,1000),bg="#131d20")
        canvas.image = second
        canvas.create_image(0, 0, image=second, anchor="nw")
        #making scrollbar
        scroll = Scrollbar(parent, command=canvas.yview)
        #adding it to canvas
        canvas.config(yscrollcommand=scroll.set)
        scroll.pack(fill="y",side=RIGHT)
        canvas.pack(fill=BOTH, expand=True)

        #-----------------------------------------------------#

        # making a search bar
        self.search = Frame(canvas,bd=0)
        self.upframwe = Frame(self.search,bg="#dabf00")
        self.downframe = Frame(self.search,bg="#dabf00")
        # search.config(bg="#e4d2fc", bd=5)
        self.search.config(bg="#dabf00", bd=3)
        imag= Image.open("smart.png")
        imag = imag.resize((70,50),Image.ANTIALIAS)
        imag =ImageTk.PhotoImage(imag)
        icon = Label(self.search,image=imag)
        icon.image=imag
        icon.grid(row=0,column=0,rowspan=2)

        #makind Serachbox
        self.ent = Entry(self.downframe, width=70,relief=GROOVE,bd=3 ,font=("times new roman ",12,"bold"))
        #making search button
        self.b = Button(self.downframe, text="search",relief="groove", command=lambda: [lis_of_link.clear(),call(str(self.ent.get()))],bd=3
                        ,activebackground="yellow",font=("Arial",10,"bold"))
        # binding Enter key with search button button
        t.bind('<Return>', lambda event=None:[self.b.invoke()])

        #---------------------------------------------------------------------------------#
        #making forward and back button
        self.back = Button(self.downframe, text=" < ",relief="groove"
                            ,command=lambda: [for_back("back",str(self.ent.get()),self)],bd=3
                           ,activebackground="yellow",font=("Arial",10,"bold"))
        
        #binding ctrl+b key with back button
        t.bind("<Control-Key-b>", lambda event=None: [for_back("back",str(self.ent.get().replace("b","")),self)])

        self.frwd = Button(self.downframe, text=" > ",relief="groove"
                            ,command=lambda: [for_back("forward",str(self.ent.get()),self)],bd=3,activebackground="yellow",font=("Arial",10,"bold"))

        #binding ctrl+f key with forward button
        t.bind("<Control-Key-f>", lambda event=None: [for_back("forward",str(self.ent.get()).replace("f",""),self)]
        
               #making home button
        try:
            self.home = Button(self.downframe, text="Home",relief="groove", command=lambda: [dt.btm.destroy(),self.putinSearch(""),freeup()],bd=3
                        ,activebackground="yellow",font=("Arial",10,"bold"))
            
            #binding home key with home button
            t.bind("<Home>",lambda event=None: [dt.btm.destroy(),self.putinSearch(""),freeup()])
        
         except AttributeError:
            print(" ")
        #making a voice search button
        mic=Image.open("mic.png")
        mic= mic.resize((20,20),Image.ANTIALIAS)
        mic=ImageTk.PhotoImage(mic)
        self.speech = Button(self.downframe,image=mic,bg="white",bd=0,command=lambda:[lis_of_link.clear(),self.micsearch()])
        self.speech.image=mic
        # ----------------------------------------------------------------------------------#

        self.back.pack(side=LEFT,fill="y",padx=4)
        self.frwd.pack(side=LEFT,fill="y",padx=4)
        self.home.pack(side=LEFT, fill="y", padx=4)
        self.home.config(width=7)
        self.ent.pack(side=LEFT, padx=3)
        self.speech.pack(side=LEFT, padx=2)
        self.b.pack(side=LEFT,padx=3)

        #self.search.pack(side=TOP, fill="x")
        self.upframwe.grid(row=1,column=2)
        self.downframe.grid(row=0,column=2,sticky="nw",padx=5)

        #adding searchbar to canvas
        self.search_frame = canvas.create_window(3,5, anchor="nw", window=self.search)

        #making right side menu bar   currently not used
        rside = Frame(canvas,relief=GROOVE)
        rside.config(bg="#7e7ec4",bd=3)
        b1 = Button(rside, relief="groove",text="Appliance", width=20, command=lambda: [lis_of_link.clear(),self.putinSearch("Appliances"), call("Appliances")])
        b2 = Button(rside, relief="groove", text="Mobile", command=lambda: [lis_of_link.clear(),self.putinSearch("Mobile"), call("Mobile")])
        b3 = Button(rside, relief="groove", text="Head phones", command=lambda: [lis_of_link.clear(),self.putinSearch("Head Phones"), call("Head phones")])
        b3.pack(fill="x", padx=2, pady=3)
        b2.pack(fill="x", padx=2, pady=3)
        b1.pack(fill="x", padx=2, pady=3)
        #canvas.create_window(40,50, anchor="nw", window=rside)
        #rside.pack(side=LEFT, fill="y")

#putinsearch method put the text of button in right side panel in search bar
    def putinSearch(self,txt):
        st = StringVar(t, value=txt)
        self.ent.config(textvariable=st)

#find the voice search
    def micsearch(self):
        pro = voice()
        call(pro)
        self.putinSearch(pro)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

                               #product class=make frame of all product present on website

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
# product class makes the frame of searches on window
class product():
    def __init__(self,master,lis):

        self.btm = Frame(canvas,width=550)
        fnt=["Arial 10 bold", "Arial 13 bold", "Arial 10 "]

        #==========================================================================================#

        try:

            #se=["#bab2de","#a0d0c4","#aca25a","#baacbc","#dad3d9","#a0d0c4"]

            # if not in the lis then it will raise type error
            if "NOT" in lis:
                # after error clear lia
                raise TypeError()
            #-------------------------------------------------#
            #for making object of % frames
            l = []
            for i in range(0, 7):
                self.la = Frame(self.btm, bg="#131d20")
                l.append(self.la)
                lis_of_link.append(lis[i]["link"])
                i += 1
            #--------------------------------------------------#

            #calling img function to show image of all product
            img = self.image()

            #==================================================================================#
            for p in range(0, 7):
                self.lab = imagebutton(l[p],img[p])
                self.lab.image = img[p]  # this is anchor image object to label
                self.lab.config(image=img[p])
                self.lanam = Label(l[p],text=lis[p].get("name"),fg="white",wraplength=600, bg='#131d20',font=fnt[0])
                self.laprice = Label(l[p],text=lis[p].get("price"),fg="white", bg='#131d20',font=fnt[1])
                self.laadd = Label(l[p], text=lis[p].get("address"),fg="white", bg='#131d20',font=fnt[2])
                self.btframe = Frame(self.btm,bg='#131d20')
                self.wish = Button(self.btframe, text="+ Wishlist",font=("times new roman ",8,"bold"),activebackground="yellow",command=lambda:[print(p)])
                self.visit = mkButton(p,self.btframe)
                self.lab.grid(row=0, column=0, sticky="ns", rowspan=2)
                self.lanam.grid(row=0, column=1)
                self.laprice.grid(row=1, column=1)
                self.laadd.grid(row=1, column=2)
                self.wish.pack(side=RIGHT,fill="x",padx=5,pady=3)
                self.visit.pack(side=RIGHT,fill="x",padx=5,pady=3)
                l[p].pack(side=TOP, fill="x", pady=1)
                self.btframe.pack(fill="x")
                p += 1
            #self.btm.place(x=50,y=100,relwidth=0.9)
            #create a window
            self.can_frame =canvas.create_window(10,70, anchor="nw", window=self.btm,tags="self.btm")
            #canvas.itemconfig("self.btm",hieght=500,width=900)
            #canvas.bind('<Configure>', self.FrameWidth)
            #to expand btm frame on canvas
            self.FrameWidth()
            #to set the size of canvas wrt btm frame
            self.btm.bind("<Configure>", self.OnFrameConfigure)
            # to bind MouseWhell for scrolling canvas
            t.bind("<MouseWheel>",self._on_mousewheel)



        except BaseException as e:
            if "NOT" not in lis:
                lis = "ERROR"
                print(e)
                print(traceback.format_exc())
            self.la = Label(self.btm,text=lis,font="Arial 22 bold")
            self.la['background']='#856ff8'
            self.la.pack(fill="x")
            #self.btm.pack(fill="x")
            canvas.create_window(50, 70, anchor="nw", window=self.btm)

        #===============================================================================================#

#destroy the search frame
    def detr(self):
        self.btm.destroy()

#put product in wish list
    def fin(self,wi):
        print(wi)

#making object of image
    def image(self):
        img=[]
        for i in range(0,7):
            im = Image.open( str(i)+".jpg")
            im = im.resize((70,65), Image.ANTIALIAS)
            im = ImageTk.PhotoImage(im)
            img.append(im)
        return img
#function to stick frame on all side of canvas
    def FrameWidth(self):
        canvas.itemconfig(self.can_frame, width=canvas.winfo_width()-10)
#function to change size of canvas wrt to btm frame
    def OnFrameConfigure(self, event):
        canvas.configure(scrollregion=canvas.bbox("all"))
              
#function to add event listener of mouse wheel on canvas to scroll canvas
    def _on_mousewheel(self, event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")



#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#

t = Tk()
parent=Frame(t)
#image = Image.open(str(1)+".jpg")
# The (450, 350) is (height, width)
#b= PhotoImage(file="resize.png")
#img= Label(t,image=b)
#resizing image by using PIL
image = Image.open('new.jpg')
image = image.resize((990,550), Image.ANTIALIAS)
#image = image.resize((100, 69), Image.ANTIALIAS)
bg = ImageTk.PhotoImage(image)
# making canvas and adding image in back ground
canvas = Canvas(parent, width=990, height=600,bg="black")
canvas.pack(fill=BOTH, expand=True)
canvas.image=bg  #-->ANCHOR TAG FOR IMAGE
canvas.create_image(0, 0, image=bg, anchor="nw")
#creating text on background image
canvas.create_text(300, 40, text="We help you to save money",fill="White",font="Times 20 bold")
canvas.create_text(800, 75, text="SKARS", fill="black", font="Arial 25 bold")
#calling making obj of header
parent.pack(fill=BOTH)
h = header(t)
#voice()


t.mainloop()


