# Based on tutorial on TKinter at codemy.com at
# https://www.youtube.com/playlist?list=PLCC34OHNcOtoC6GglhF3ncJ5rLwQrLGnV
# and contributions from Microsoft's Copilot

# Import everything from tkinter
from tkinter import *

# Import Image Library
from PIL import ImageTk,Image

#Create the main interface
root = Tk()

#Title the Main App Interface
root.title('EVENUE')
root.iconbitmap('thumbnail_PNG_image.ico')

# Set a phone-like window size and prevent arbitrary resizing for predictable layout
PHONE_WIDTH = 360
# reduce overall height per request
PHONE_HEIGHT = 640
root.geometry(f"{PHONE_WIDTH}x{PHONE_HEIGHT}")
root.resizable(False, False)

# Resize the PNG to exactly the phone window dimensions so it spans the entire app
try:
    # Pillow 9.1+ moved ANTIALIAS under Resampling; pick LANCZOS compatibly.
    try:
        resample_filter = Image.Resampling.LANCZOS
    except AttributeError:
        resample_filter = Image.LANCZOS

    _img = Image.open("thumbnail_PNG_image.png")
    _img = _img.resize((PHONE_WIDTH, PHONE_HEIGHT), resample_filter)
    my_img = ImageTk.PhotoImage(_img)
except Exception:
    # Fallback to original image if resizing fails; attempt to at least fit width
    _img = Image.open("thumbnail_PNG_image.png")
    try:
        _img.thumbnail((PHONE_WIDTH, PHONE_HEIGHT), resample_filter)
    except Exception:
        _img.thumbnail((PHONE_WIDTH, PHONE_HEIGHT))
    my_img = ImageTk.PhotoImage(_img)

#Define functions for button clicks
def login():
    import login
    login.entry()

 # for vertical buttons simple placeholder: show a popup
def events():
    top = Toplevel(root)
    top.title("Attendables")
    Label(top, text="A page that shows events.").pack(padx=10, pady=10)

def tickets():
    top = Toplevel(root)
    top.title("Valuables")
    Label(top, text="A page that shows purchases including tickets and receipts for items purchased in 'Buyables'.").pack(padx=10, pady=10)

def merch():
    top = Toplevel(root)
    top.title("Buyables")
    Label(top, text="A page that shows products for sale.").pack(padx=10, pady=10)

def sm():
    top = Toplevel(root)
    top.title("Shareables")
    Label(top, text="A page that shows pics and vids 'attendabled' recently at the venue.").pack(padx=10, pady=10)

def wallpapers():
    top = Toplevel(root)
    top.title("Saveables")
    Label(top, text="A page that allows venue related images to become personally usable.").pack(padx=10, pady=10)

def sos():
    top = Toplevel(root)
    top.title("Capables")
    Label(top, text="A page that connects users to 'capables,' or, sources of help and commonly asked questions, an AI-powered answer bot, and a place for expressing irritables.").pack(padx=10, pady=10)

def vvmap():
    top = Toplevel(root)
    top.title("Navigables")
    Label(top, text="A virtual map that makes the venue navigable to users whether they are at home or inside of the venue.").pack(padx=10, pady=10)

# Header: centered title and login button at top-right
# Use a Canvas so the image fills the entire window and we can draw text on top
canvas = Canvas(root, width=PHONE_WIDTH, height=PHONE_HEIGHT, highlightthickness=0)
canvas.pack(fill='both', expand=True)

# Draw background image covering the whole canvas
bg_img_id = canvas.create_image(0, 0, anchor='nw', image=my_img)

# Helper to create clickable text on the canvas
def make_text_button(x, y, text, callback=None, font_size=14, anchor='w'):
    # default font and bold variant
    normal_font = (None, font_size)
    bold_font = (None, font_size, 'bold')
    # text drawn in black per request
    item = canvas.create_text(x, y, text=text, anchor=anchor, fill='black', font=normal_font)
    rect_id = None

    def on_enter(event):
        nonlocal rect_id
        # draw a slightly darkened grey rectangle behind the text
        bbox = canvas.bbox(item)  # (x0, y0, x1, y1)
        if bbox:
            pad_x = 8
            pad_y = 6
            x0, y0, x1, y1 = bbox
            rect_id = canvas.create_rectangle(x0 - pad_x, y0 - pad_y, x1 + pad_x, y1 + pad_y,
                                              fill='#d9d9d9', outline='')
            # put rectangle behind text
            canvas.tag_lower(rect_id, item)
        # bold the text
        canvas.itemconfig(item, font=bold_font)
        canvas.config(cursor='hand2')

    def on_leave(event):
        nonlocal rect_id
        # remove rectangle and restore font
        if rect_id is not None:
            try:
                canvas.delete(rect_id)
            except Exception:
                pass
            rect_id = None
        canvas.itemconfig(item, font=normal_font)
        canvas.config(cursor='')

    if callback:
        def handler(event, cb=callback):
            cb()
        canvas.tag_bind(item, '<Button-1>', handler)

    # hover bindings for visual changes
    canvas.tag_bind(item, '<Enter>', on_enter)
    canvas.tag_bind(item, '<Leave>', on_leave)
    return item

# Title centered at top
make_text_button(PHONE_WIDTH//2, 24, "EVENUE", callback=None, font_size=18, anchor='center')

# Login text at top-right
def _open_login():
    login()

make_text_button(PHONE_WIDTH-12, 24, "Accountable", callback=_open_login, font_size=12, anchor='e')

# Vertical menu: place items from near leftmost to roughly middle vertically
left_x = 16
start_y = 120
step_y = 44
vertical_items = [
    ("Attendables", events),
    ("Valuables", tickets),
    ("Buyables", merch),
    ("Shareables", sm),
    ("Saveables", wallpapers),
    ("Capables", sos),
    ("Navigables", vvmap),
]

for i, (txt, cb) in enumerate(vertical_items):
    make_text_button(left_x, start_y + i*step_y, txt, callback=cb, font_size=14, anchor='w')

#Loop the interface
root.mainloop()