from tkinter import messagebox
import tkinter as tk
import os
from LBbutton import *
from NewStop import *
import winsound
import webbrowser

# Main screen class


class LazyBoiCont:
    def __init__(self, parent, controller):
        self.controller = controller
        self.parent = parent
        self.parent.title('LazyBoi Link Manager')
        self.imgicon = tk.PhotoImage(file=os.path.join('pics/', 'wlink.gif'))
        self.parent.call('wm', 'iconphoto', parent._w, self.imgicon)
        self.frame = tk.Frame(self.parent, bg='#4D648D')
        self.frame.grid(rows=10, columns=10, sticky=tk.N+tk.S+tk.E+tk.W)
        self.mainlabel = tk.Label(self.frame, text='LazyBoi: Playbook Links', bg='#353748', fg='white', borderwidth=8)
        self.mainlabel.grid(row=0, column=1, columnspan=2, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
        self.mainlabel.config(font=('Courier', 10), highlightbackground='white')
        self.lftclk = tk.Label(self.frame, text='Left click for playbooks', bg='#353748', fg='white')
        self.lftclk.grid(row=0, column=0, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
        self.rhtclk = tk.Label(self.frame, text='Right click for On-Call', bg='#353748', fg='white')
        self.rhtclk.grid(row=0, column=3, pady=10, sticky=tk.N+tk.S+tk.E+tk.W)
        self.menu_bar = tk.Menu(parent, background='#4D648D', foreground='white', activebackground='#575A5F',
                                activeforeground='white')
        self.file_menu = tk.Menu(self.menu_bar, background='#575A5F', foreground='white', tearoff=0)
        self.file_menu.add_command(label="Config", background='#4D648D', foreground='white', command=self.config_window)
        self.file_menu.add_command(label="Exit", background='#4D648D', command=self.exit_app)
        self.menu_bar.add_cascade(label="File", background='#575A5F', foreground='white', menu=self.file_menu)
        self.view_menu = tk.Menu(self.menu_bar, background='#575A5F', foreground='white', tearoff=0)
        self.view_menu.add_command(label='Useful links', background='#4D648D', foreground='white',
                                   command=self.useful_window)
        self.view_menu.add_command(label='Testing links', background='#4D648D', foreground='white',
                                   command=self.testing_win)
        self.view_menu.add_command(label='War room links', background='#4D648D', foreground='white',
                                   command=self.warroom_win)
        self.menu_bar.add_cascade(label='View', menu=self.view_menu)
        self.add_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.add_menu.add_command(label='Add Partner Link', background='#4D648D', foreground='white',
                                  command=self.add_part)
        self.menu_bar.add_cascade(label='Add Link', menu=self.add_menu)
        self.remove_menu = tk.Menu(self.menu_bar, background='#4D648D', foreground='white', tearoff=0)
        self.remove_menu.add_command(label='Remove Partner Link', background='#4D648D',
                                     foreground='white', command=self.remove_part)
        self.menu_bar.add_cascade(label='Remove Link', menu=self.remove_menu)
        self.time_menu = tk.Menu(self.menu_bar, background='#4D648D', foreground='white', tearoff=0)
        self.time_menu.add_command(label='Timer', command=self.time_r)
        self.menu_bar.add_cascade(label="Timer", menu=self.time_menu)
        self.parent.config(menu=self.menu_bar)
        self.cvalue = 0
        self.buttns = []
        self.remove = 0
        self.lam = 'lambda line=line: open_oclink'

        # Generate buttons from partner text files

        if os.path.isfile('playbooks.txt') is True and os.path.getsize('playbooks.txt') > 0:
            lines = os.listdir('partnerpb/')
            print(lines)
            x = 1  # Value for row
            p = 1  # Value to alternate D/L
            bid = 0  # Button identifier

            for linepre in lines:
                line = linepre.replace('.txt', '')
                if x <= 13:
                    if p == 1:  # Dark buttons - bind for right click
                        self.dark_button(line, bid, x)
                        x += 1
                        p += 1
                        bid += 1
                    elif p == 2:  # Light buttons - Bind for right click
                        self.light_button(line, bid, x)
                        x += 1
                        p = 1
                        bid += 1
                else:
                    self.cvalue += 1  # Change columns
                    x = 1
                    if p == 1:  # Dark buttons - new column
                        self.dark_button(line, bid, x)
                        p += 1
                        x += 1
                        bid += 1
                    else:  # light button - new column
                        self.light_button(line, bid, x)
                        p = 1
                        x += 1
                        bid += 1
        #  Row and column configs for window and frame - allows resizing.
        for prow_num in range(self.parent.grid_size()[1]):
            Grid.rowconfigure(self.parent, prow_num, weight=1)
        for pcol_num in range(self.parent.grid_size()[1]):
            Grid.columnconfigure(self.parent, pcol_num, weight=1)
        for col_num in range(self.frame.grid_size()[1]):
            Grid.columnconfigure(self.frame, col_num, weight=1)
        for row_num in range(self.frame.grid_size()[1]):
            Grid.rowconfigure(self.frame, row_num, weight=1)

    #  Function for dark button generation and binding.
    def dark_button(self, line, bid, x):
        self.buttns.append(DButton(self.frame, text=line, command=lambda line=line, bid=bid:
        self.open_link(line, bid)))
        self.buttns[bid].grid(row=x, column=self.cvalue, padx=3, pady=3, sticky=tk.N + tk.S + tk.E + tk.W)
        self.buttns[bid].config(highlightbackground='white', border=5)
        self.buttns[bid].bind('<Button-3>', lambda event, line=line: self.open_oclink(line))

    #  Function for light button generation and binding.
    def light_button(self, line, bid, x):
        self.buttns.append(LButton(self.frame, text=line, command=lambda line=line, bid=bid:
        self.open_link(line, bid)))
        self.buttns[bid].grid(row=x, column=self.cvalue, padx=3, pady=3, sticky=tk.N + tk.S + tk.E + tk.W)
        self.buttns[bid].config(highlightbackground='white', border=5)
        self.buttns[bid].bind('<Button-3>', lambda event, line=line: self.open_oclink(line))

    # Function to generate config window
    def config_window(self):
        self.twt = tk.Toplevel()
        self.twt.wm_title('Config Window')
        self.twt.focus_force()
        imgicon = tk.PhotoImage(file=os.path.join('pics/', 'wlink.gif'))
        self.twt.tk.call('wm', 'iconphoto', self.twt, imgicon)
        self.twt.config(background='#4D648D')
        fm = tk.Frame(self.twt, bg='#4D648D')
        fm.grid(rows=7, column=2, ipadx=55, ipady=30, sticky=tk.N+tk.S+tk.E+tk.W)
        hours = tk.Entry(fm)
        hours.grid(row=0, column=0, pady=5, sticky=tk.E+tk.W)
        mins = tk.Entry(fm)
        mins.grid(row=1, column=0, pady=5, sticky=tk.E+tk.W)
        secs = tk.Entry(fm)
        secs.grid(row=2, column=0, pady=5, sticky=tk.E+tk.W)
        tbttn = RButton(fm, text='Start Timer', command=TimerGo)
        tbttn.grid(row=3, column=0, pady=5, sticky=tk.E+tk.W)
        # for row_num in range(fm, row_num, weight=1):
        for wrow_num in range(self.twt.grid_size()[1]):
            Grid.rowconfigure(self.twt, wrow_num, weight=1)
        for wcol_num in range(self.twt.grid_size()[1]):
            Grid.columnconfigure(self.twt, wcol_num, weight=1)
        for row_num in range(fm.grid_size()[1]):
            Grid.rowconfigure(fm, row_num, weight=1)
        for col_num in range(fm.grid_size()[1]):
            Grid.columnconfigure(fm, col_num, weight=1)

    #  Function for generating adding partner window
    def add_part(self):
        self.tw = tk.Toplevel()
        self.tw.wm_title('Add Partner')
        self.tw.focus_force()
        imgicon = tk.PhotoImage(file=os.path.join('pics/', 'wlink.gif'))
        self.tw.tk.call('wm', 'iconphoto', self.tw, imgicon)
        self.tw.config(background='#4D648D')
        fm = tk.Frame(self.tw, bg='#4D648D')
        fm.grid(rows=7, column=2, ipadx=55, ipady=30, sticky=tk.N+tk.S+tk.E+tk.W)
        spacerlab = tk.Label(fm, text='', background='#4D648D', foreground='white')
        spacerlab.grid(row=0, column=0, columnspan=3, ipadx=10, ipady=10)
        partlab = tk.Label(fm, text='New Partner: ', background='#4D648D', foreground='white')
        partlab.grid(row=1, column=0, sticky=tk.W+tk.E)
        self.partentry = tk.Entry(fm)
        self.partentry.grid(row=1, column=1, sticky=tk.W+tk.E)
        spacerlab2 = tk.Label(fm, text='', background='#4D648D', foreground='white')
        spacerlab2.grid(row=2, column=0, columnspan=3, ipadx=5, ipady=5)
        linklab = tk.Label(fm, text='PB Link: ', background='#4D648D', foreground='white')
        linklab.grid(row=3, column=0, sticky=tk.W+tk.E)
        self.linkentry = tk.Entry(fm)
        self.linkentry.grid(row=3, column=1, sticky=tk.W+tk.E)
        spacerlab3 = tk.Label(fm, text='', background='#4D648D', foreground='white')
        spacerlab3.grid(row=4, column=0, columnspan=3, ipadx=5, ipady=5)
        oclab = tk.Label(fm, text='On-call Link: ', background='#4D648D', foreground='white')
        oclab.grid(row=5, column=0, sticky=tk.W+tk.E)
        self.ocentry = tk.Entry(fm)
        self.ocentry.grid(row=5, column=1, sticky=tk.W+tk.E)
        spacerlab3 = tk.Label(fm, text='', background='#4D648D', foreground='white')
        spacerlab3.grid(row=6, column=0, columnspan=3, ipadx=5, ipady=5)
        savebutton = tk.Button(fm, text='Add', bg='#7688A9', fg='white', command=self.save_part)
        savebutton.grid(row=7, column=1, sticky=tk.W+tk.E)
        for wrow_num in range(self.tw.grid_size()[1]):
            Grid.rowconfigure(self.tw, wrow_num, weight=1)
        for wcol_num in range(self.tw.grid_size()[1]):
            Grid.columnconfigure(self.tw, wcol_num, weight=1)
        for row_num in range(fm.grid_size()[1]):
            Grid.rowconfigure(fm, row_num, weight=1)
        for col_num in range(fm.grid_size()[1]):
            Grid.columnconfigure(fm, col_num, weight=1)

    def save_part(self):
        if self.partentry.get() == "" or self.linkentry.get() == '':
            messagebox.showinfo('Error', 'Must fill in both fields.')
        else:
            partner = self.partentry.get()
            partlink = self.linkentry.get()
            oclink = self.ocentry.get()
            sp = open("pblinks/{0}.txt".format(partner), 'w+')
            sp.write(partlink)
            sp.close()
            spl = open('partnerpb/{0}.txt'.format(partner), 'a')
            spl.write('\n{0}'.format(partner))
            spl.close()
            sp2 = open('oclinks/{0}.txt'.format(partner), 'a')
            sp2.write('{0}'.format(oclink))
            sp2.close()
            print(partner)
            print(partlink)
            print(oclink)
            if os.path.isfile('pblinks/{0}.txt'.format(partner)) \
                    is True and os.path.getsize('pblinks/{0}.txt'.format(partner)) > 0:
                messagebox.showinfo("Success", "New partner successfully saved")
                # self.tw.destroy()
            self.tw.update()
            # LazyBoiCont(parent, controller=None)
            main()
                # self.parent.quit()
                # LazyBoiCont(self.parent)

    def remove_part(self):
        if self.remove == 0:
            self.remove = 1
            self.stopbutton = RButton(self.frame, text='Stop removing', command=self.stop_remove)
            self.stopbutton.grid(row=14, column=0, padx=3, pady=3, sticky=tk.W)
        else:
            pass

    def stop_remove(self):
        self.remove = 0
        self.stopbutton.destroy()

    def open_link(self, line, bid):
        if self.remove == 0:
            print(line)
            stripped = line.replace('\n', '')
            site = ('pblinks/%s.txt' % stripped)
            f = open(site)
            link = f.read()
            os.startfile(link)
            self.frame.clipboard_clear()
            self.frame.clipboard_append('Looking in to it')
        else:
            os.remove('pblinks/{0}.txt'.format(self.buttns[bid]['text']))
            os.remove('partnerpb/{0}.txt'.format(self.buttns[bid]['text']))
            self.buttns[bid].destroy()

    def open_oclink(self, line):
        print('right click %s' % line)
        stripped = line.replace('\n', '')
        site = ('oclinks/%s.txt' % stripped)
        f = open(site)
        link = f.read()
        os.startfile(link)
        self.frame.clipboard_clear()
        self.frame.clipboard_append('Looking in to it')

    def exit_app(self):
        self.parent.destroy()

    def useful_window(self):
        UsefulWindow(self)

    def testing_win(self):
        TestingWindow(self)

    def warroom_win(self):
        WarWindow(self)

    def time_r(self):
        Tmain()


class UsefulWindow:
    def __init__(self, parent):
        self.parent = parent
        self.t = tk.Toplevel()
        self.t.focus_force()
        self.frame = tk.Frame(self.t, background='#4D648D')
        self.imgicon = tk.PhotoImage(file=os.path.join('pics/', 'wlink.gif'))
        self.t.wm_title("Useful Links")
        self.t.tk.call('wm', 'iconphoto', self.t, self.imgicon)
        self.t.config(background='#4D648D')
        self.frame.grid(rows=10, columns=10, sticky=tk.N+tk.S+tk.E+tk.W)
        self.cpy = []
        self.x = 1
        self.p = 1
        self.cvalue = 1
        self.y = 0
        self.fold = 'useful/'
        self.bidb = 0
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)
        self.buttn = []
        self.remove = 0
        menu_bar = tk.Menu(self.frame, background='#4D648D', foreground='white', activebackground='#575A5F',
                           activeforeground='white')
        add_menu = tk.Menu(menu_bar, tearoff=0)
        add_menu.add_command(label='Add Link', background='#4D648D', foreground='white', command=self.add_link)
        menu_bar.add_cascade(label='Add Link', menu=add_menu)
        rem_menu = tk.Menu(menu_bar, tearoff=0)
        rem_menu.add_command(label='Remove Link', background='#4D648D', foreground='white', command=self.remove_useful)
        menu_bar.add_cascade(label='Remove Link', menu=rem_menu)
        self.t.config(menu=menu_bar)
        for lines in os.listdir('useful/'):
            self.cpy.append(lines)
        for self.entries in self.cpy:
            st = self.entries.replace('.txt', '')
            if self.x <= 4:
                if self.p == 1:
                    self.buttn.append(DButton(self.frame, text=st,
                                      command=lambda fold=self.fold, entries=self.entries,
                                      ubidb=self.bidb: self.open_ulink(fold, entries, ubidb)))
                    self.buttn[self.bidb].grid(row=self.x, column=self.cvalue, padx=3, pady=3, sticky=tk.N+tk.S+tk.E+tk.W)
                    print(st)
                    print('under 5')
                    print('Color: %d' % self.p)
                    print('row: %d' % self.x)
                    print('column: %d' % self.cvalue)
                    self.x += 1
                    self.p += 1
                    self.bidb += 1

                elif self.p == 2:
                    self.buttn.append(LButton(self.frame, text=st, command=lambda fold=self.fold, entries=self.entries,
                                      ubidb=self.bidb: self.open_ulink(fold, entries, ubidb)))
                    self.buttn[self.bidb].grid(row=self.x, column=self.cvalue, padx=3, pady=3, sticky=tk.N+tk.S+tk.E+tk.W)
                    print(st)
                    print('under 5')
                    print('Color: %d' % self.p)
                    print('row: %d' % self.x)
                    print('column: %d' % self.cvalue)
                    self.x += 1
                    self.p = 1
                    self.bidb += 1

            else:
                self.cvalue += 1
                self.x = 1
                if self.p == 1:
                    self.buttn.append(DButton(self.frame, text=st, command=lambda fold=self.fold,
                                      entries=self.entries, ubidb=self.bidb: self.open_ulink(fold, entries, ubidb)))
                    self.buttn[self.bidb].grid(row=self.x, column=self.cvalue, padx=3, pady=3, sticky=tk.N+tk.S+tk.E+tk.W)
                    print(st)
                    print('over 5')
                    print('Color: %d' % self.p)
                    print('row: %d' % self.x)
                    print('column: %d' % self.cvalue)
                    self.p += 1
                    self.x += 1
                    self.bidb += 1

                else:
                    self.buttn.append(LButton(self.frame, text=st, command=lambda fold=self.fold,
                                      entries=self.entries, ubidb=self.bidb: self.open_ulink(fold, entries, ubidb)))
                    self.buttn[self.bidb].grid(row=self.x, column=self.cvalue, padx=3, pady=3, sticky=tk.N+tk.S+tk.E+tk.W)
                    print(st)
                    print('over 5')
                    print('Color: %d' % self.p)
                    print('row: %d' % self.x)
                    print('column: %d' % self.cvalue)
                    self.p = 1
                    self.x += 1
                    self.bidb += 1

    def close_windows(self):
        self.parent.destroy()

    def add_link(self):
        self.t = tk.Toplevel()
        self.t.wm_title('Add Useful Link')
        self.t.focus_force()
        imgicon = tk.PhotoImage(file=os.path.join('pics/', 'wlink.gif'))
        self.t.tk.call('wm', 'iconphoto', self.t, imgicon)
        self.t.config(background='#4D648D')
        fm = tk.Frame(self.t, bg='#4D648D')
        fm.grid(rows=7, column=2, ipadx=55, ipady=30)
        spacerlab = tk.Label(fm, text='', background='#4D648D', foreground='white')
        spacerlab.grid(row=0, column=0, columnspan=3, ipadx=10, ipady=10)
        partlab = tk.Label(fm, text='Name for link: ', background='#4D648D', foreground='white')
        partlab.grid(row=1, column=0, sticky=tk.W)
        self.partentry = tk.Entry(fm)
        self.partentry.grid(row=1, column=1, sticky=tk.W)
        linklab = tk.Label(fm, text='Link: ', background='#4D648D', foreground='white')
        linklab.grid(row=3, column=0, sticky=tk.W)
        self.linkentry = tk.Entry(fm)
        self.linkentry.grid(row=3, column=1, sticky=tk.W)
        savebutton = tk.Button(fm, text='Add', bg='#7688A9', fg='white', command=self.save_useful)
        savebutton.grid(row=5, column=1, sticky=tk.E)

    def open_ulink(self, fold, entries, ubidb):
        if self.remove == 0:
            print(entries)
            print(fold)
            f = open("{0}{1}".format(fold, entries))
            print(f)
            rl = f.read()
            print(rl)
            os.startfile(rl)
        else:
            os.remove('useful/{0}.txt'.format(self.buttn[ubidb]['text']))
            self.buttn[ubidb].destroy()

    def save_useful(self):
        partner = self.partentry.get()
        partlink = self.linkentry.get()
        sp = open("useful/{0}.txt".format(partner), 'w+')
        print(partner)
        print(partlink)
        sp.write(partlink)
        sp.close()
        if os.path.isfile('useful/{0}.txt'.format(partner)) is True and \
                os.path.getsize('useful/{0}.txt'.format(partner)) > 0:
                self.t.destroy()
                UsefulWindow(self)
                messagebox.showinfo("Success", "New partner successfully saved")

    def remove_useful(self):
        if self.remove == 0:
            self.remove = 1
            self.stopbutton = RButton(self.frame, text='Stop removing', command=self.stop_remove)
            self.stopbutton.grid(row=3, column=1, padx=3, pady=3, sticky=tk.W)
        else:
            pass

    def stop_remove(self):
        self.remove = 0
        self.stopbutton.destroy()


class TestingWindow:
    def __init__(self, parent):
        self.parent = parent
        self.t = tk.Toplevel()
        self.t.focus_force()
        self.frame = tk.Frame(self.t, bg='#4D648D')
        self.imgicon = tk.PhotoImage(file=os.path.join('pics/', 'wlink.gif'))
        self.t.wm_title("Testing Links")
        self.t.tk.call('wm', 'iconphoto', self.t, self.imgicon)
        self.t.config(background='#4D648D')
        self.frame.grid(rows=10, columns=10, sticky=tk.N+tk.S+tk.E+tk.W)
        self.cpy = []
        self.x = 1
        self.p = 1
        self.cvalue = 1
        self.y = 0
        self.remove = 0
        tbid = 0
        self.fold = 'testing/'
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)
        self.buttn = []
        menu_bar = tk.Menu(self.frame, background='#4D648D', foreground='white', activebackground='#575A5F',
                           activeforeground='white')
        add_menu = tk.Menu(menu_bar, tearoff=0)
        add_menu.add_command(label='Add Link', background='#4D648D', foreground='white', command=self.add_link)
        menu_bar.add_cascade(label='Add Link', menu=add_menu)
        rem_menu = tk.Menu(menu_bar, tearoff=0)
        rem_menu.add_command(label='Remove Link', background='#4D648D', foreground='white', command=self.remove_test)
        menu_bar.add_cascade(label='Remove Link', menu=rem_menu)
        self.t.config(menu=menu_bar)
        for lines in os.listdir('testing/'):
            self.cpy.append(lines)
        for self.entries in self.cpy:
            st = self.entries.replace('.txt', '')
            if self.x <= 5:
                if self.p == 1:
                    self.buttn.append(DButton(self.frame, text=st,
                                      command=lambda fold=self.fold, nentries=self.entries,
                                      tbidb=tbid: self.open_ulink(fold, nentries, tbidb)))
                    self.buttn[tbid].grid(row=self.x, column=self.cvalue, padx=3, pady=3, sticky=tk.N+tk.S+tk.E+tk.W)
                    print(st)
                    print('under 5')
                    print('Color: %d' % self.p)
                    print('row: %d' % self.x)
                    print('column: %d' % self.cvalue)
                    print(tbid)
                    self.x += 1
                    self.p += 1
                    tbid += 1

                elif self.p == 2:
                    self.buttn.append(LButton(self.frame, text=st, command=lambda fold=self.fold,
                                              nentries=self.entries, tbidb=tbid:
                                              self.open_ulink(fold, nentries, tbidb)))
                    self.buttn[tbid].grid(row=self.x, column=self.cvalue, padx=3, pady=3, sticky=tk.N+tk.S+tk.E+tk.W)
                    print(st)
                    print('under 5')
                    print('Color: %d' % self.p)
                    print('row: %d' % self.x)
                    print('column: %d' % self.cvalue)
                    print(tbid)
                    self.x += 1
                    self.p = 1
                    tbid += 1

            else:
                self.cvalue += 1
                self.x = 1
                if self.p == 1:
                    self.buttn.append(DButton(self.frame, text=st, command=lambda
                                              fold=self.fold, nentries=self.entries, tbidb=tbid:
                                              self.open_ulink(fold, nentries, tbidb)))
                    self.buttn[tbid].grid(row=self.x, column=self.cvalue, padx=3, pady=3, sticky=tk.N+tk.S+tk.E+tk.W)
                    print(st)
                    print('over 5')
                    print('Color: %d' % self.p)
                    print('row: %d' % self.x)
                    print('column: %d' % self.cvalue)
                    print(tbid)
                    self.p += 1
                    self.x += 1
                    tbid += 1

                else:
                    self.buttn.append(LButton(self.frame, text=st, command=lambda
                                              fold=self.fold, nentries=self.entries, tbidb=tbid:
                                              self.open_ulink(fold, nentries, tbidb)))
                    self.buttn[tbid].grid(row=self.x, column=self.cvalue, padx=3, pady=3, sticky=tk.N+tk.S+tk.E+tk.W)
                    print(st)
                    print('over 5')
                    print('Color: %d' % self.p)
                    print('row: %d' % self.x)
                    print('column: %d' % self.cvalue)
                    print(tbid)
                    self.p = 1
                    self.x += 1
                    tbid += 1

    def open_ulink(self, fold, nentries, tbidb):
        if self.remove == 0:
            if nentries == 'TestRails.txt':
                f = open("{0}{1}".format(fold, nentries))
                rl = f.read()
                # os.startfile(rl)
                # url = 'www.google.com'
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
                webbrowser.get(chrome_path).open_new(rl)

            elif nentries == 'EDP Demo Customer.txt' or nentries == 'EDP Demo Partner.txt' or nentries == \
                    'EDP Prod Customer' or nentries == 'EDP Prod Partner':
                self.unamepass = tk.Toplevel()
                uframe = tk.Frame(self.unamepass, bg='#4D648D')
                uframe.grid(rows=5, columns=3)
                text_ent = tk.Text(uframe, height=4, width=35, background='#4D648D', foreground='white')
                text_ent.grid(row=0, column=0, sticky=tk.W)
                text_ent.insert(tk.END, "Username: hpi.cso.noc@gmail.com\nPassword: N0cpassword!")
                unam = tk.Button(uframe, text='Copy username', command=self.copy_u)
                unam.grid(row=1, column=0, sticky=tk.W)
                upass = tk.Button(uframe, text='Copy password', command=self.copy_p)
                upass.grid(row=1, column=0, padx=100, sticky=tk.W)
                f = open("{0}{1}".format(fold, nentries))
                rl = f.read()
                # os.startfile(rl)
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
                webbrowser.get(chrome_path).open_new(rl)
            else:
                f = open("{0}{1}".format(fold, nentries))
                rl = f.read()
                # os.startfile(rl)
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s --incognito'
                webbrowser.get(chrome_path).open_new(rl)
        else:
            os.remove('testing/{0}.txt'.format(self.buttn[tbidb]['text']))
            self.buttn[tbidb].destroy()

    def copy_u(self):
        # self.unamepass.withdraw()
        self.unamepass.clipboard_clear()
        self.unamepass.clipboard_append('hpi.cso.noc@gmail.com')
        # self.unamepass.update()

    def copy_p(self):
        # self.unamepass.withdraw()
        self.unamepass.clipboard_clear()
        self.unamepass.clipboard_append('N0cpassword!')
        # self.unamepass.update()

    def add_link(self):
        self.ta = tk.Toplevel()
        self.ta.wm_title('Add Test Link')
        self.ta.focus_force()
        imgicon = tk.PhotoImage(file=os.path.join('pics/', 'wlink.gif'))
        self.ta.tk.call('wm', 'iconphoto', self.t, imgicon)
        self.ta.config(background='#4D648D')
        fm = tk.Frame(self.ta, bg='#4D648D')
        fm.grid(rows=7, column=2, ipadx=55, ipady=30)
        spacerlab = tk.Label(fm, text='', background='#4D648D', foreground='white')
        spacerlab.grid(row=0, column=0, columnspan=3, ipadx=10, ipady=10)
        partlab = tk.Label(fm, text='Name for link: ', background='#4D648D', foreground='white')
        partlab.grid(row=1, column=0, sticky=tk.W)
        self.partentry = tk.Entry(fm)
        self.partentry.grid(row=1, column=1, sticky=tk.W)
        linklab = tk.Label(fm, text='Link: ', background='#4D648D', foreground='white')
        linklab.grid(row=3, column=0, sticky=tk.W)
        self.linkentry = tk.Entry(fm)
        self.linkentry.grid(row=3, column=1, sticky=tk.W)
        savebutton = tk.Button(fm, text='Add', bg='#7688A9', fg='white', command=self.save_test)
        savebutton.grid(row=5, column=1, sticky=tk.E)

    def save_test(self):
        partner = self.partentry.get()
        partlink = self.linkentry.get()
        sp = open("testing/{0}.txt".format(partner), 'w+')
        print(partner)
        print(partlink)
        sp.write(partlink)
        sp.close()
        if os.path.isfile('testing/{0}.txt'.format(partner)) is True and \
                os.path.getsize('testing/{0}.txt'.format(partner)) > 0:
            self.ta.destroy()
            self.t.destroy()
            TestingWindow(self)
            # messagebox.showinfo("Success", "New link successfully added")

    def remove_test(self):
        if self.remove == 0:
            self.remove = 1
            self.stopbutton = RButton(self.frame, text='Stop removing', command=self.stop_remove)
            self.stopbutton.grid(row=3, column=1, padx=3, pady=3, sticky=tk.W)
        else:
            pass

    def stop_remove(self):
        self.remove = 0
        self.t.destroy()
        TestingWindow(self)


class ConfigWindow:
    def __init__(self, parent):
        self.parent = parent
        print(parent)
        self.frame = tk.Frame(self.parent)
        self.imgicon = tk.PhotoImage(file=os.path.join('pics/', 'wlink.gif'))
        self.parent.wm_title("Config")
        self.parent.tk.call('wm', 'iconphoto', self.parent, self.imgicon)


class WarWindow:
    def __init__(self, parent):
        self.parent = parent
        self.t = tk.Toplevel()
        self.t.focus_force()
        self.frame = tk.Frame(self.t, bg='#4D648D')
        self.imgicon = tk.PhotoImage(file=os.path.join('pics/', 'wlink.gif'))
        self.t.wm_title("War Room Links")
        self.t.tk.call('wm', 'iconphoto', self.t, self.imgicon)
        self.t.config(background='#4D648D')
        self.frame.grid(rows=10, columns=10, sticky=tk.N+tk.S+tk.E+tk.W)
        self.cpy = []
        self.x = 1
        self.p = 1
        self.cvalue = 1
        self.y = 0
        self.remove = 0
        tbid = 0
        self.fold = 'warroom/'
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.rowconfigure(3, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)
        self.buttn = []
        menu_bar = tk.Menu(self.frame, background='#4D648D', foreground='white', activebackground='#575A5F',
                           activeforeground='white')
        add_menu = tk.Menu(menu_bar, tearoff=0)
        add_menu.add_command(label='Add Link', background='#4D648D', foreground='white', command=self.add_link)
        menu_bar.add_cascade(label='Add Link', menu=add_menu)
        rem_menu = tk.Menu(menu_bar, tearoff=0)
        rem_menu.add_command(label='Remove Link', background='#4D648D', foreground='white', command=self.remove_war)
        menu_bar.add_cascade(label='Remove Link', menu=rem_menu)
        self.t.config(menu=menu_bar)
        for lines in os.listdir('warroom/'):
            self.cpy.append(lines)
        for self.entries in self.cpy:
            st = self.entries.replace('.txt', '')
            if self.x <= 2:
                if self.p == 1:
                    self.buttn.append(DButton(self.frame, text=st,
                                      command=lambda fold=self.fold, nentries=self.entries,
                                      tbidb=tbid: self.open_ulink(fold, nentries, tbidb)))
                    self.buttn[tbid].grid(row=self.x, column=self.cvalue, padx=3, pady=3, sticky=tk.N+tk.S+tk.E+tk.W)
                    print(st)
                    print('under 5')
                    print('Color: %d' % self.p)
                    print('row: %d' % self.x)
                    print('column: %d' % self.cvalue)
                    print(tbid)
                    self.x += 1
                    self.p += 1
                    tbid += 1

                elif self.p == 2:
                    self.buttn.append(LButton(self.frame, text=st, command=lambda fold=self.fold,
                                              nentries=self.entries, tbidb=tbid:
                                              self.open_ulink(fold, nentries, tbidb)))
                    self.buttn[tbid].grid(row=self.x, column=self.cvalue, padx=3, pady=3, sticky=tk.N+tk.S+tk.E+tk.W)
                    print(st)
                    print('under 5')
                    print('Color: %d' % self.p)
                    print('row: %d' % self.x)
                    print('column: %d' % self.cvalue)
                    print(tbid)
                    self.x += 1
                    self.p = 1
                    tbid += 1

            else:
                self.cvalue += 1
                self.x = 1
                if self.p == 1:
                    self.buttn.append(DButton(self.frame, text=st, command=lambda
                                              fold=self.fold, nentries=self.entries, tbidb=tbid:
                                              self.open_ulink(fold, nentries, tbidb)))
                    self.buttn[tbid].grid(row=self.x, column=self.cvalue, padx=3, pady=3, sticky=tk.N+tk.S+tk.E+tk.W)
                    print(st)
                    print('over 5')
                    print('Color: %d' % self.p)
                    print('row: %d' % self.x)
                    print('column: %d' % self.cvalue)
                    print(tbid)
                    self.p += 1
                    self.x += 1
                    tbid += 1

    def open_ulink(self, fold, entries, ubidb):
        if self.remove == 0:
            print(entries)
            print(fold)
            f = open("{0}{1}".format(fold, entries))
            print(f)
            rl = f.read()
            print(rl)
            os.startfile(rl)
        else:
            os.remove('warroom/{0}.txt'.format(self.buttn[ubidb]['text']))
            self.buttn[ubidb].destroy()

    def add_link(self):
        self.ta = tk.Toplevel()
        self.ta.wm_title('Add War Room Link')
        self.ta.focus_force()
        imgicon = tk.PhotoImage(file=os.path.join('pics/', 'wlink.gif'))
        self.ta.tk.call('wm', 'iconphoto', self.t, imgicon)
        self.ta.config(background='#4D648D')
        fm = tk.Frame(self.ta, bg='#4D648D')
        fm.grid(rows=7, column=2, ipadx=55, ipady=30)
        spacerlab = tk.Label(fm, text='', background='#4D648D', foreground='white')
        spacerlab.grid(row=0, column=0, columnspan=3, ipadx=10, ipady=10)
        partlab = tk.Label(fm, text='Name for link: ', background='#4D648D', foreground='white')
        partlab.grid(row=1, column=0, sticky=tk.W)
        self.partentry = tk.Entry(fm)
        self.partentry.grid(row=1, column=1, sticky=tk.W)
        linklab = tk.Label(fm, text='Link: ', background='#4D648D', foreground='white')
        linklab.grid(row=3, column=0, sticky=tk.W)
        self.linkentry = tk.Entry(fm)
        self.linkentry.grid(row=3, column=1, sticky=tk.W)
        savebutton = tk.Button(fm, text='Add', bg='#7688A9', fg='white', command=self.save_war)
        savebutton.grid(row=5, column=1, sticky=tk.E)

    def save_war(self):
        partner = self.partentry.get()
        partlink = self.linkentry.get()
        sp = open("warroom/{0}.txt".format(partner), 'w+')
        print(partner)
        print(partlink)
        sp.write(partlink)
        sp.close()
        if os.path.isfile('warroom/{0}.txt'.format(partner)) is True and \
                os.path.getsize('warroom/{0}.txt'.format(partner)) > 0:
            self.ta.destroy()
            self.t.destroy()
            WarWindow(self)
            # messagebox.showinfo("Success", "New link successfully added")

    def remove_war(self):
        if self.remove == 0:
            self.remove = 1
            self.stopbutton = RButton(self.frame, text='Stop removing', command=self.stop_remove)
            self.stopbutton.grid(row=3, column=1, padx=3, pady=3, sticky=tk.W)
        else:
            pass

    def stop_remove(self):
        self.remove = 0
        self.t.destroy()
        WarWindow(self)


class TimerGo:
    def __init__(self):
        self.tg = tk.Toplevel()
        self.tg.wm_title('Timer')
        self.tg.focus_force()
        imgicon = tk.PhotoImage(file=os.path.join('pics/', 'wlink.gif'))
        self.tg.tk.call('wm', 'iconphoto', self.tg, imgicon)
        self.tg.config(background='#4D648D')
        self.fra = tk.Frame(self.tg, bg='#4D648D')
        self.fra.grid(rows=4, columns=3, sticky=tk.N+tk.S+tk.E+tk.W)
        self.fra.rowconfigure(0, weight=1)
        self.fra.rowconfigure(1, weight=1)
        self.labspacer = tk.Label(self.fra, text='00:00:00', background='#1E1A1A', fg='#CD1212')
        self.labspacer.grid(row=0, column=0, columnspan=3, ipadx=40, ipady=15, sticky=tk.N+tk.S+tk.W+tk.E)
        self.labspacer.config(font=('Courier', 30))
        self.labhr = tk.Label(self.fra, text='Enter hours: ', background='#4D648D', fg='white')
        self.labhr.grid(row=2, column=0, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)
        self.enthr = tk.Entry(self.fra)
        self.enthr.grid(row=2, column=1, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)
        self.labmin = tk.Label(self.fra, text='Enter minutes: ', background='#4D648D', fg='white')
        self.labmin.grid(row=3, column=0, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)
        self.entmin = tk.Entry(self.fra)
        self.entmin.grid(row=3, column=1, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)
        self.labsec = tk.Label(self.fra, text='Enter seconds: ', background='#4D648D', fg='white')
        self.labsec.grid(row=4, column=0, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)
        self.entsec = tk.Entry(self.fra)
        self.entsec.grid(row=4, column=1, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)
        self.strt_time = RButton(self.fra, text='Start Timer', command=self.timergo)
        self.strt_time.grid(row=5, column=1, ipadx=5, padx=5, pady=5, sticky=tk.N+tk.S+tk.E+tk.W)
        self.c = ':'

    def timergo(self):
        if self.enthr.get() == '':
            self.hours = 0
        else:
            self.hours = int(self.enthr.get())
        if self.entmin.get() == '':
            self.mins = 0
        else:
            self.mins = int(self.entmin.get())
        if self.entsec.get() == '':
            self.secs = 0
        else:
            self.secs = int(self.entsec.get())
        self.strt_time.config(state='disabled')
        while self.hours > -1:
            while self.mins > -1:
                while self.secs > 0:
                    self.sec1 = ('%02.f' % self.secs)
                    min1 = ('%02.f' % self.mins)
                    hour1 = ('%02.f' % self.hours)
                    print(self.sec1, hour1, min1)
                    sys.stdout.write('\r' + str(hour1) + self.c + str(min1) + self.c + str(self.sec1))
                    self.labspacer.config(text=('\r' + str(hour1) + self.c + str(min1) + self.c + str(self.sec1)))
                    self.secs -= 1
                    self.labspacer.after(1000, self.labspacer.update())
                self.mins -= 1
                self.secs = 59
            self.hours -= 1
            self.mins = 59
            self.secs = 59
        i = 5
        while i > 0:
            i -= 1
            winsound.Beep(1000, 1000)

    def createWidgets(self):
        self.hournow = int(self.enthr.get())
        self.minnow = int(self.entmin.get())
        self.secnow = int(self.entsec.get())
        print(self.hournow)
        print(self.minnow)
        print(self.secnow)
        timerdisp = tk.Toplevel()
        timerdisp.title('Timer')
        timerdisp.config(background='#4D648D')
        timefram = tk.Frame(timerdisp, bg='#4D648D')
        timefram.grid(rows=10, columns=10, ipadx=10, ipady=10)
        self.now = ""
        # self.now = tk.StringVar()
        # self.now = self.seconds()
        self.time = tk.Label(timefram, font=('Helvetica', 24))
        self.time.grid(row=0, column=0)
        # self.hournow = 0
        # self.minnow = 0
        # self.secnow = 60
        self.c = ':'
        self.time["textvariable"] = self.now
        # self.QUIT = tk.Button(self, text="QUIT", fg="red",
        #                       command=self.timerdisp.destroy)
        # self.QUIT.grid(row=4, column=2)
        self.onUpdate()

    def onUpdate(self):
        self.now = self.seconds()
        self.fra.after(1000, self.onUpdate)

    def seconds(self):
        while int(self.hournow) > -1:
            while int(self.minnow) > -1:
                while int(self.secnow) > 0:
                    self.secnow -= 1
                    self.timeout = '\r' + str(self.hournow) + self.c + str(self.minnow) + self.c + str(self.secnow)
            self.minnow -= 1
            self.secnow = 60
        self.hournow -= 1
        self.minnow = 59
        return str(self.timeout)

# TODO - Subsection for automating startup apps


def main():
    root = tk.Tk()
    app = LazyBoiCont(root, controller=HourStop)
    root.mainloop()


if __name__ == '__main__':
    main()
