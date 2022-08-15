import tkinter as tk
UI_FONT=('Times',30,'bold')

# ------------functions-------------#

def output_sentiment():
    to_search=user_search.get()






# ---------------UI-------------#


# ------------image-----------#

bg_img=



win=tk.Tk()
win.title('Sentiment Classifier')
win.minsize(width=1000,height=700)

canvas=tk.Canvas(width=800,height=600)
canvas.create_text(500,100,text='Sentiment classifier',font=UI_FONT)



# -------get_input-----#

user_search=tk.Entry(width=50)
canvas.create_text(500,150,text='Enter the entity: ',font=('Ariel',20,'bold'))
canvas.create_window(500,200,window=user_search)
canvas.grid()





























win.mainloop()