import pafy
import tkinter as tk
import sys

try:
    def button_c(i):
        print(i)
        print("downloading.....")
        i.download(quiet=True, callback=mycb)
        print("download completed")


    def downloader():
        e = e1.get()
        tk.Label(wd, text="can't get video info").grid(row=0, column=2, columnspan=2)
        button_enter.destroy()
        print(e)
        e1.delete(0, tk.END)
        video = pafy.new(e)
        tk.Label(wd, text=f"{video.title}").grid(row=0, column=2, columnspan=2)
        n = 0
        ro = 2
        for i in video.streams:
            if n > 5:
                ro += 1
                n = 0
            bi = tk.Button(wd, text=i, command=lambda i=i: button_c(i)).grid(row=ro, column=n)
            n += 1
        best = video.getbestvideo()
        b2 = tk.Button(wd, text=best, command=lambda best=i: button_c(i)).grid(row=ro, column=n)
        n = 0
        ro += 1

        for i in video.audiostreams:
            if n > 5:
                ro += 1
                n = 0
            bi = tk.Button(wd, text=i, command=lambda i=i: button_c(i)).grid(row=ro, column=n)
            n += 1


    def callback(event):
        downloader()


    def mycb(total, recvd, ratio, rate, eta):
        sys.stdout.flush()
        total = int(total) / 1000000
        recvd = int(recvd) / 1000000
        total = "{:.2f}".format(total)
        recvd = "{:.2f}".format(recvd)
        rate = "{:.2f}".format(rate)

        sys.stdout.write(f"\rtotal = {total}")
        sys.stdout.write(f"\rtotal : {total}MB   recived : {recvd}MB  ETA : {eta}sec  speed : {rate}kbps")


    wd = tk.Tk()
    wd.title('Youtube video downloader')
    tk.Label(wd, text="link:->").grid(row=0, column=0)
    e1 = tk.Entry(wd)
    e1.grid(row=0, column=1)
    button_enter = tk.Button(wd, text='enter', command=downloader)
    button_enter.grid(row=0, column=2)
    wd.bind('<Return>', callback)
    wd.mainloop()

except:
    print("stopped")
