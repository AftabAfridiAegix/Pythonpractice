# from tkinter import *
# from tkinter.ttk import *
# import time

# def start():
#     GB = 100
#     download= 0
#     speed = 2
#     while(download<GB):
#         time.sleep(0.05)
#         bar['value'] += (speed/GB)*100
#         download +=speed
#         x+=1
#         percent.set(str(int((download/GB)*100))+ "%")
#         text.set = (str(download))+ "/"+str(GB) + "GB completed")
#         window.update_idletasks()

#     window = Tk()

#     percent = StringVar()
#     text = StringVar()
# bar = Progressbar(window,orient=VERTICAL, Length = 300)
# bar.pack(pady = 10)

# percentLabel = Label(window, textvariable = percent).pack()

# percentLabel = Label(window, textvariable = text).pack()

# window.mainloop()


from tkinter import *
from tkinter.ttk import Progressbar
import time

def start():
    GB = 100
    download = 0
    speed = 2

    while download < GB:
        time.sleep(0.05)

        download += speed
        bar["value"] = download

        percent.set(str(int((download / GB) * 100)) + "%")
        text.set(str(download) + "/" + str(GB) + " GB completed")

        window.update()

window = Tk()
window.title("Download Progress")
window.geometry("400x250")

percent = StringVar()
text = StringVar()

bar = Progressbar(
    window,
    orient=HORIZONTAL,
    length=300,
    mode="determinate",
    maximum=100
)
bar.pack(pady=20)

percentLabel = Label(window, textvariable=percent)
percentLabel.pack()

textLabel = Label(window, textvariable=text)
textLabel.pack(pady=10)

button = Button(window, text="Start Download", command=start)
button.pack(pady=10)

window.mainloop()