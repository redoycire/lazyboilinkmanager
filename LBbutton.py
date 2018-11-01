from tkinter import *


class DButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = '#353748'
        self['fg'] = 'white'
        self['height'] = 2
        self['width'] = 15
        self['relief'] = 'sunken'
        self['activebackground'] = '#4D648D'
        self['activeforeground'] = 'white'
        self['font'] = ('Courier', 9)


class LButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = '#7688A9'
        self['fg'] = 'black'
        self['height'] = 2
        self['width'] = 15
        self['relief'] = 'raised'
        self['activebackground'] = '#353748'
        self['activeforeground'] = 'white'
        self['font'] = ('Courier', 9)


class RButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = '#9B1818'
        self['fg'] = 'white'
        self['height'] = 2
        self['width'] = 15
        self['relief'] = 'raised'
        self['activebackground'] = '#710000'
        self['activeforeground'] = 'white'
        # self['font'] = ('Courier', 10)


class GButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = '#30A63F'
        self['fg'] = 'white'
        self['height'] = 2
        self['width'] = 15
        self['relief'] = 'raised'
        self['activebackground'] = '#148F23'
        self['activeforeground'] = 'white'
        # self['font'] = ('Courier', 10)


class YButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = '#CC6E12'
        self['fg'] = 'white'
        self['height'] = 2
        self['width'] = 15
        self['relief'] = 'raised'
        self['activebackground'] = '#A25203'
        self['activeforeground'] = 'white'
        # self['font'] = ('Courier', 10)
        # 919100  676700


class BButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = '#7083A4'
        self['fg'] = 'white'
        self['height'] = 2
        self['width'] = 15
        self['relief'] = 'raised'
        self['activebackground'] = '#485F87'
        self['activeforeground'] = 'white'
        # self['font'] = ('Courier', 10)


class PButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = '#E37E85'
        self['fg'] = 'white'
        self['height'] = 2
        self['width'] = 15
        self['relief'] = 'raised'
        self['activebackground'] = '#B9464E'
        self['activeforeground'] = 'white'
        # self['font'] = ('Courier', 10)


class PUButton(Button):

    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)
        self['bg'] = '#754C7F'
        self['fg'] = 'white'
        self['height'] = 2
        self['width'] = 15
        self['relief'] = 'raised'
        self['activebackground'] = '#5D3267'
        self['activeforeground'] = 'white'
        # self['font'] = ('Courier', 10)



