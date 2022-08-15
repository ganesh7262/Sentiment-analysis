import tkinter as tk
UI_FONT=('Times',30,'bold')
# ------------------twitter setup----------#





# ------------functions-------------#

def output_sentiment():
    to_search=user_search.get()



def create_out_window():
    out_txt=tk.Text(width=70,height=20,state=tk.DISABLED)
    to_print=user_search.get()
    canvas.create_window(400,400,window=out_txt)
    out_txt.insert(tk.END,f'{to_print}')



# ---------------UI-------------#




root=tk.Tk()
root.resizable(0,0)
root.title('Sentiment Classifier')

# ------------image-----------#
bg_img=tk.PhotoImage(file=r'C:\Users\ganes\OneDrive\Documents\GitHub\Sentment-analysis\BERT sentiment analysis\images\final.png')


canvas=tk.Canvas(width=800,height=600)
canvas.create_image(400,300,image=bg_img)
canvas.create_text(400,50,text='Sentiment classifier',font=UI_FONT,fill='white')



# -------get_input-----#

user_search=tk.Entry(width=40)
input_text=canvas.create_text(200,120,text='Enter the Entity: ',font=('MS Serif',20,'bold'),fill='white')
canvas.create_window(430,120,window=user_search)
canvas.grid()

search_button=tk.Button(text='Search',command=create_out_window)
search_button.place(x=560,y=107)






























root.mainloop()