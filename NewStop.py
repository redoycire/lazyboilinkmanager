from LBbutton import *
import tkinter as tk
from tkinter import *
import os
import winsound


class HourStop(tk.Frame):
    def __init__(self, parent=None, ** kw):
        tk.Frame.__init__(self, parent, kw)
        self.grid(sticky=tk.N + tk.S + tk.E + tk.W)
        self.go = 0
        self._timenow = ''
        self.startmin = 0
        self.startsecs = 0
        self.resetmins = 0
        self.resetsecs = 0
        self.initial = 0
        self.reset_flag = 0
        self.make_win()
        Grid.rowconfigure(self, 0, weight=1)
        Grid.rowconfigure(self, 1, weight=1)
        Grid.rowconfigure(self, 2, weight=1)
        Grid.rowconfigure(self, 3, weight=1)
        Grid.rowconfigure(self, 4, weight=1)
        Grid.columnconfigure(self, 0, weight=1)
        Grid.columnconfigure(self, 1, weight=1)
        Grid.columnconfigure(self, 2, weight=1)
        Grid.columnconfigure(self, 3, weight=1)
        Grid.columnconfigure(self, 4, weight=1)
        Grid.columnconfigure(self, 5, weight=1)

    def get_page(self):
        return self

    def make_win(self):
        self.tlab = tk.Label(self, text='', background='#1E1A1A', fg='#CD1212')
        self.tlab.grid(row=1, column=0, columnspan=4, ipadx=40, ipady=15, padx=60, pady=50, sticky=tk.N+tk.S+tk.W+tk.E)
        self.tlab.config(font=('Courier', 40))
        self.tlab.config(text='00:00')
        self.update()
        self.bottom_frame = tk.Frame(self, bg='#4D648D')
        self.bottom_frame.grid(rows=4, columns=4, row=2, column=0, columnspan=3, sticky=tk.N+tk.S+tk.E+tk.W)
        Grid.rowconfigure(self.bottom_frame, 0, weight=1)
        Grid.rowconfigure(self.bottom_frame, 1, weight=1)
        Grid.rowconfigure(self.bottom_frame, 2, weight=1)
        Grid.rowconfigure(self.bottom_frame, 3, weight=1)
        Grid.rowconfigure(self.bottom_frame, 4, weight=1)
        Grid.rowconfigure(self.bottom_frame, 5, weight=1)
        Grid.columnconfigure(self.bottom_frame, 0, weight=1)
        Grid.columnconfigure(self.bottom_frame, 1, weight=1)
        Grid.columnconfigure(self.bottom_frame, 2, weight=1)
        Grid.columnconfigure(self.bottom_frame, 3, weight=1)
        Grid.columnconfigure(self.bottom_frame, 4, weight=1)
        Grid.columnconfigure(self.bottom_frame, 5, weight=1)
        self.minlab=tk.Label(self.bottom_frame, text='Minutes:', bg='#4D648D', fg='white')
        self.minlab.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W+tk.E)
        self.minlab.config(font=('Times', 10))
        self.seclab = tk.Label(self.bottom_frame, text='Seconds:', bg='#4D648D', fg='white')
        self.seclab.grid(row=2, column=1, padx=15, pady=5, sticky=tk.W+tk.E)
        self.seclab.config(font=('Times', 10))
        self.minent = tk.Entry(self.bottom_frame)
        self.minent.grid(row=3, column=0, padx=9, ipady=10, pady=15, sticky=tk.W+tk.E)
        self.minent.insert(tk.END, '0')
        self.secent = tk.Entry(self.bottom_frame)
        self.secent.grid(row=3, column=1, padx=9, ipady=10, pady=15, sticky=tk.W+tk.E)
        self.secent.insert(tk.END, '0')
        GButton(self.bottom_frame, text='Start', command=self.Gettime).grid(row=4, column=0, ipadx=6, padx=9, pady=5,
                                                                            sticky=tk.E+tk.W)
        RButton(self.bottom_frame, text='Stop', command=self.Stop).grid(row=4, column=1, ipadx=6, padx=9, pady=5,
                                                                        sticky=tk.E+tk.W)
        YButton(self.bottom_frame, text='Reset', command=self.Reset).grid(row=4, column=2, padx=9, pady=5,
                                                                          sticky=tk.E+tk.W)
        PUButton(self.bottom_frame, text='Quit', command=self.quit).grid(row=4, column=3, padx=9, pady=5,
                                                                         sticky=tk.E+tk.W)
        BButton(self.bottom_frame, text='1 Hour', command=self.Hournow).grid(row=3, column=2, padx=9,
                                                                             sticky=tk.E+tk.W)
        PButton(self.bottom_frame, text='1/2 Hour', command=self.Halfnow).grid(row=3, column=3, padx=9,
                                                                               sticky=tk.E+tk.W)

    def _update(self):
        self.update()
        self._settime()
        if self.startmin == 0 and self.startsecs == 0:
            i = 15
            while i > 0:
                i -= 1
                winsound.Beep(3000, 100)
            self.Stop()
        else:
            self.timer = self.after(1000, self._update)

    def _settime(self):
        # if self.startmin == '':
        #     self.startmin = 0
        # elif self.startsecs == '':
        #     self.startsecs = 0
        if self.startsecs > -1:
            self.startsecs -= 1
            print('subbed 1')
            self.tlab.config(text='%02d:%02d' % (self.startmin, self.startsecs))
            self.update()
        if self.startsecs == -1:
            if self.startmin == 0:
                print('end')
                self.startsecs = 0
                self.update()
                self.Stop()
            else:
                print('sec change over')
                self.startsecs = 59
                self.startmin -= 1
                self.tlab.config(text='%02d:%02d' % (self.startmin, self.startsecs))

    def Gettime(self):
        if self.startmin == '':
            self.startmin = 0
        elif self.startsecs == '':
            self.startsecs = 0
        else:
            if self.initial == 0:
                self.startmin = int(self.minent.get())
                self.startsecs = int(self.secent.get()) + 1
                self.Start()
            elif self.initial == 1:
                self.startmin = int(self.resetmins)
                self.startsecs = int(self.resetsecs)
                self.Start()
            else:
                self.startmin = self.startmin
                self.startsecs = self.startsecs
                self.Start()

    def Hournow(self):
        self.minent.delete('0', tk.END)
        self.secent.delete('0', tk.END)
        self.minent.insert(tk.END, '59')
        self.secent.insert(tk.END, '59')
        self.resetmins = int(self.minent.get())
        self.resetsecs = int(self.secent.get())
        self.go = 0
        self.initial = 1
        # self._update()
        self.update()
        self.Gettime()


    def Halfnow(self):
        self.minent.delete('0', tk.END)
        self.secent.delete('0', tk.END)
        self.minent.insert(tk.END, '30')
        self.secent.insert(tk.END, '01')
        self.resetmins = int(self.minent.get())
        self.resetsecs = int(self.secent.get())
        self.initial = 1
        self.go = 0
        # self._update()
        self.update()
        self.Gettime()

    def Start(self):
        if not self.go:
            if self.initial == 0:
                self._timenow = ('%02d:%02d' % (int(self.minent.get()), int(self.secent.get())))
                self._settime()
                self._update()
                self.go = 1
                self.initial = 1
                print('initial 0')
            elif self.initial == 1:
                print('initial 1')
                self._settime()
                self.resetmins = self.startmin
                self.resetsecs = self.startsecs
                self._timenow = ('%02d:%02d' % (self.resetmins, self.resetsecs))
                self._settime()
                self._update()
                self.initial = 1
                self.go = 1

    def Stop(self):
        print(self.startmin)
        print(self.startsecs)
        print(self.resetmins)
        print(self.resetsecs)
        if self.go:
            self.after_cancel(self.timer)
            self.update()
            self.go = 0
            self.initial = 0
        else:
            pass

    def Reset(self):
        self.minent.delete('0', tk.END)
        self.secent.delete('0', tk.END)
        self.startmin = self.resetmins
        self.startsecs = self.resetsecs
        self.update()
        self.minent.insert(tk.END, self.resetmins)
        self.secent.insert(tk.END, self.resetsecs)

        if self.go:
            self.tlab.config(text='%02d:%02d' % (self.resetmins, self.resetsecs))
            self.update()
            self.after_cancel(self.timer)
            self.go = 0
        else:
            self.tlab.config(text='%02d:%02d' % (self.resetmins, self.resetsecs))
            self.update()
            self.after_cancel(self.timer)


def Tmain():
    root = tk.Toplevel()
    sw = HourStop(root)
    imgicon = tk.PhotoImage(file=os.path.join('pics/', 'stop.gif'))
    root.tk.call('wm', 'iconphoto', root, imgicon)
    root.wm_title('Hour Timer')
    sw.bind('<Return>', (lambda _: HourStop.Gettime))
    sw.grid(rows=5, columns=5, sticky=tk.N + tk.S + tk.E + tk.W)
    sw.config(bg='#1E1A1A')
    Grid.rowconfigure(root, 0, weight=1)
    Grid.rowconfigure(root, 1, weight=1)
    Grid.rowconfigure(root, 2, weight=1)
    Grid.rowconfigure(root, 3, weight=1)
    Grid.rowconfigure(root, 4, weight=1)
    Grid.columnconfigure(root, 0, weight=1)
    Grid.columnconfigure(root, 1, weight=1)
    Grid.columnconfigure(root, 2, weight=1)
    Grid.columnconfigure(root, 3, weight=1)
    Grid.columnconfigure(root, 4, weight=1)
    Grid.columnconfigure(root, 4, weight=1)
    root.mainloop()


if __name__ == '__main__':
        Tmain()
