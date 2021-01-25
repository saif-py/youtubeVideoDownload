import time
import pafy
import tkinter as tk
import sys

try:
    try:
        try:
            try:
                def button_c(i):
                    # global videoideo
                    print(i)
                    print("downloading.....")
                    i.download(quiet=True, callback=mycb)
                    print("download completed")


                def callback(event):
                    e = e1.get()
                    tk.Label(wd, text="getting video info").grid(row=0, column=2, columnspan=2)
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
                    n += 1
                    for i in video.audiostreams:
                        if n > 5:
                            ro += 1
                            n = 0
                        bi = tk.Button(wd, text=i, command=lambda i=i: button_c(i)).grid(row=ro, column=n)
                        n += 1


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

                wd.bind('<Return>', callback)
                wd.mainloop()
            except ValueError:
                print("check your provided link")
        except KeyboardInterrupt:
            print("process cancelled")
    except OSError:
        print("error: check your internet connection")
except:
    print("stopped")
