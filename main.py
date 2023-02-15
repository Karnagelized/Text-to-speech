
import gtts
import re
import webbrowser
from tkinter import *
from tkinter import ttk, filedialog
import tkinter.font as font

from config import *
from lang import _langs, languages, language_default
from log import log_write

def main():
    # Create window
    root = Tk()
    root.config(padx=15, pady=15)
    root.resizable(False, False)

    root.title(TITLE)
    root.geometry(f'{WIDTH}x{HEIGHT}+'
                  f'{root.winfo_screenwidth() // 2 - WIDTH // 2}+'
                  f'{root.winfo_screenheight() // 2 - HEIGHT // 2}'
                  )
    root.option_add('*TCombobox*Listbox.font', ('Times New Roman', 18))

    # Save file with selected directory
    def save_file() -> None:
        path = filedialog.asksaveasfilename(
            defaultextension='.json', filetypes=[('MP4', '*.mp4')],
            initialfile='Convert Audio',
            title='Choose filename'
        )

        if path != '':
            path_tx['state'] = 'normal'
            path_tx.delete(1.0, END)
            path_tx.insert(1.0, path)
            path_tx['state'] = 'disabled'

    # Conversation
    def convert(path:str, words:str, lang:str) -> None:
        if path != '\n':
            if re.findall('\S+', words) != []:
                words = ''.join(re.findall('\S+', words))

                if lang != '':
                    try:
                        aud = gtts.gTTS(words, lang=_langs.get(lang))
                        aud.save(path[:-1:])

                        title_successfully['text'] = 'Successfully!'
                        title_successfully['fg'] = 'green'
                    except FileNotFoundError:
                        title_successfully['text'] = 'No such directory!'
                        title_successfully['fg'] = 'red'
                    except Exception as e:
                        log_write(str(e))
                        title_successfully['text'] = 'Program Error!'
                        title_successfully['fg'] = 'red'
                else:
                    title_successfully['text'] = 'Choose language'
                    title_successfully['fg'] = 'red'
            else:
                title_successfully['text'] = 'Empty text field'
                title_successfully['fg'] = 'red'
        else:
            title_successfully['text'] = 'Bad Path'
            title_successfully['fg'] = 'red'

    # Info mess
    def show_message() -> None:
        convert(path_tx.get(1.0, END), words_entry.get('1.0', END), language_box.get())

    # Clear enters
    def clear_words() -> None:
        title_successfully['text'] = ''
        title_successfully['fg'] = 'black'
        path_tx['state'] = 'normal'
        path_tx.delete(1.0, END)
        path_tx['state'] = 'disabled'
        words_entry.delete('1.0', END)

    # Open links
    def callback_github(event):
        webbrowser.open_new("https://github.com/Karnagelized")

    def callback_telegram(event):
        webbrowser.open_new("https://t.me/masikantonov")

    def callback_vk(event):
        webbrowser.open_new("https://vk.com/masikantonov")

    # Path frame
    path_frame = Frame()
    path_frame.pack(fill=X)

    path_lb = Label(
        path_frame,
        width=10,
        text='Path',
        font=('Times New Roman', 20)
    )
    path_lb.pack(side=LEFT)

    path_tx = Text(
        path_frame,
        font=('Times New Roman', 20),
        height=1,
        width=35,
        wrap='none',
        state='disabled'
    )
    path_tx.pack(side=LEFT, fill=X)

    # Choose button
    clear_button = Button(
        path_frame,
        background='white',
        width=10,
        text='Choose',
        command=save_file,
        font=('Times New Roman', 15),
        relief=RIDGE,
        borderwidth=2
    )
    clear_button.pack(side=RIGHT)

    # ------------------ Indent ------------------ #
    Frame().pack(fill=X, pady=8)

    # Words frame
    words_frame = Frame()
    words_frame.pack(fill=X)

    words = Label(
        words_frame,
        width=10,
        text='Text',
        font=('Times New Roman', 20)
    )
    words.pack(side=LEFT, anchor=N)

    words_entry = Text(
        words_frame,
        wrap='word',
        height=8,
        font=('Times New Roman', 20),
        padx=5,
        pady=5
    )
    words_entry.pack()

    # ------------------ Indent ------------------ #
    Frame().pack(fill=X, pady=8)

    # Language frame
    language_frame = Frame()
    language_frame.pack(fill=X)

    language = Label(
        language_frame,
        width=10,
        text='Language',
        font=('Times New Roman', 20)
    )
    language.pack(side=LEFT)

    language_box = ttk.Combobox(
        language_frame,
        font=('Times New Roman', 20),
        values=languages,
        textvariable=StringVar(value=language_default),
        state='readonly'
    )
    language_box.pack(side=LEFT)

    # ------------------ Indent ------------------ #
    Frame().pack(fill=X, pady=8)

    # Buttons frame
    button_frame = Frame()
    button_frame.pack(fill=X, pady=0, expand=False)

    # Convert button
    button = Button(
        button_frame,
        background='white',
        width=9,
        text='Convert',
        command=show_message,
        font=('Times New Roman', 20),
        relief=RIDGE,
        borderwidth=5
    )
    button.pack(side=RIGHT)

    # Clear button
    clear_button = Button(
        button_frame,
        background='white',
        width=9,
        text='Clear',
        command=clear_words,
        font=('Times New Roman', 20),
        relief=RIDGE,
        borderwidth=5
    )
    clear_button.pack(side=LEFT)

    # ------------------ Indent ------------------ #
    Frame().pack(fill=X, pady=8)

    # Buttons frame
    successfully_frame = Frame()
    successfully_frame.pack(fill=X)

    title_successfully = Label(
        successfully_frame,
        text='',
        font=('Times New Roman', 25, 'bold'),
        height=3,
        highlightbackground='gray',
        highlightthickness=1
    )
    title_successfully.pack(fill=X)

    # ------------------ Indent ------------------ #
    Frame().pack(fill=X, pady=8)

    # Links frame
    created_by_frame = Frame()
    created_by_frame.pack(fill=X)

    link_github = Label(
        created_by_frame,
        text='GitHub',
        font=('Times New Roman', 15, 'bold'),
        fg='#666',
        cursor='heart',
        padx=5,
    )
    link_github.pack(side=LEFT)
    link_github.bind("<Button-1>", callback_github)

    link_telegram = Label(
        created_by_frame,
        text='Telegram',
        font=('Times New Roman', 15, 'bold'),
        fg='#666',
        cursor='heart',
        padx=5,
    )
    link_telegram.pack(side=LEFT)
    link_telegram.bind("<Button-1>", callback_telegram)

    link_vk = Label(
        created_by_frame,
        text='VK',
        font=('Times New Roman', 15, 'bold'),
        fg='#666',
        cursor='heart',
        padx=5,
    )
    link_vk.pack(side=LEFT)
    link_vk.bind("<Button-1>", callback_vk)

    created_by = Label(
        created_by_frame,
        text='Created by Karnagelized',
        font=('Times New Roman', 15, 'bold'),
        fg='#666',
    )
    created_by.pack(anchor=SE)

    root.mainloop()

if __name__ == '__main__':
    main()
