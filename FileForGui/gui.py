from tkinter import *
import Sentiment as st

gui = Tk()

gui.geometry("1000x631")
gui.title("Sentiment Detector")
gui.iconbitmap("D:\\Mini_project\\SentimentalAnalysis\\FileForGui\\emotions.ico")
# Add image file
bg = PhotoImage(file = "D:\\Mini_project\\SentimentalAnalysis\\FileForGui\\SentimentAnalysis.png")

# Create Canvas
canvas1 = Canvas( gui, width = 400,height = 400)

canvas1.pack(fill = "both", expand = True)

# Display image
canvas1.create_image( 0, 0, image = bg ,anchor = "nw")

frame = LabelFrame(gui,text = "          Welcome to Sentiment Analysis     \n     \U0001f642\U0001f641\U0001f642\U0001f641\U0001f642\U0001f641\U0001f642\U0001f641\U0001f642\U0001f641\U0001f642\U0001f641\U0001f642\U0001f641",font = "lucida 20",bg="light yellow",borderwidth=0,padx=10,pady=10)
#frame.pack(padx=10,pady=10)
frameCanvas = canvas1.create_window( 230, 50, anchor = "nw", window = frame)
  
enterText = Label(frame, text = "Enter Text ",font = "lucida 13",bg = "light green",borderwidth=20)

textArea = Text(frame, height = 6, width = 40, font = "lucida 15",borderwidth=4)

# lable for Sentiment
sentiment_Label = Label(frame, text = "Sentiment of the text ",font = "lucida 13",borderwidth=10,bg = "light green")

sentiment_text = Text(frame, height = 1, width = 18, font = "lucida 15",borderwidth=4)
sentiment_text.configure(state='disabled')

def checkSentimental():
    # sample text for sentimental Analysis 
    SampleText = textArea.get("1.0", "end-1c")
    result = st.Detector(SampleText)
    #sentiment_text.insert(INSERT,result)
    sentiment_text.configure(state='normal')
    sentiment_text.insert(INSERT,result)
    sentiment_text.configure(state='disabled')
    

def clearAll() :
    sentiment_text.configure(state='normal')  
    # deleting the content from the text box 
    sentiment_text.delete("1.0", END);
    # whole content of text area  is deleted
    textArea.delete("1.0", END);
    sentiment_text.configure(state='disabled')


# BUTTONS for checking ,clear , Exit 
check = Button(frame, text = "Check Sentiment",font ="15", fg = "Black",bg = "yellow",borderwidth=4,command=checkSentimental)
clear = Button(frame, text = "Clear",font="16" ,fg = "Black",bg = "Yellow",borderwidth=4, command = clearAll)
#Exit = Button(frame, text = "Exit", fg = "Red", font ="15",command = exit,borderwidth=4)



# Display all content in tk
enterText.grid(row = 1, column = 2)
    
textArea.grid(row = 2, column = 2, padx = 40, pady=10,sticky = W)
    
check.grid(row = 3, column = 2,pady=10)
    
sentiment_Label.grid(row = 4, column = 2)
    
sentiment_text.grid(row = 5, column = 2, padx = 160, pady = 10,sticky = W)
    
clear.grid(row =12, column = 2,pady= 10)
    
#Exit.grid(row = 13, column = 2)


gui.mainloop()