from tkinter import *
root = Tk()
root.title("SuperhardIsn'tit")
root.geometry("4000x4000")





moths = ["Jan","Feb","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec"]

pythonpo = [10,1100,8,9,50,90000,180,130,82,94,510,900000]

q1 = Label(root)

q1["text"] = str(moths)

q2 = Label(root)

q2["text"] = str(pythonpo)

q3 = Label(root)

q4 = Label(root)

def max12():
    maxin = max(pythonpo)
    mapro = pythonpo.index(maxin)
    #print(mapro)

    month = moths[mapro]
    q3["text"]="The Unlucky Max Profit is " + str(maxin) + " In The UNMonth of " + str(month)

    #print("The Unlucky Max Profit is " + str(maxin) + " In The UNMonth of " + str(month))



def unmin():
    maiin = min(pythonpo)
    mipro = pythonpo.index(maiin)
    #print(mipro)

    monthi = moths[mipro]
    q4["text"]="The Unlucky Min Profit is " + str(maiin) + " In The UNMonth of " + str(monthi)

    #print("The Unlucky Min Profit is " + str(maiin) + " In The UNMonth of " + str(monthi))
    
    
q5 = Button(root,text = "Hey this Button is in a q5 var",command = max12)

q6 = Button(root,text = "Hey this Button is in a q6 var", command = unmin)

    
q1.place(relx = 0.5 , rely = 0.1,anchor = CENTER)
q2.place(relx = 0.5 , rely = 0.2,anchor = CENTER)
q3.place(relx = 0.5 , rely = 0.4,anchor = CENTER)
q4.place(relx = 0.5 , rely = 0.6,anchor = CENTER)
q5.place(relx = 0.5 , rely = 0.3,anchor = CENTER)
q6.place(relx = 0.5 , rely = 0.5,anchor = CENTER)

root.mainloop()
