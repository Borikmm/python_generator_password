from tkinter import Tk, BooleanVar, StringVar, messagebox
from tkinter.ttk import Frame, Button, Label, Entry, Checkbutton, Style
from Main import generator

class Panel1(Frame):
    def __init__(self):
        self.password = StringVar()
        self.seed_give = StringVar()
        super().__init__()
        frame1 = Frame(self)
        frame1.pack(fill="both")

        self.Label1 = Label(frame1, text="Password", width=8)
        self.Entry1 = Entry(frame1, textvariable=self.password)

        self.Label1.pack(side="left")
        self.Entry1.pack(fill="x")

        frame2 = Frame(self)
        frame2.pack(fill="x", side="right", expand=True)

        self.Label2 = Label(frame2, text="Seed", width=8)
        self.Entry2 = Entry(frame2, textvariable=self.seed_give)

        self.Label2.pack(side="left")
        self.Entry2.pack(fill="x")

class Panel2(Frame):
    def __init__(self):
        self.lenght = StringVar()
        self.register = StringVar()
        self.word = StringVar()
        self.language = StringVar()
        self.del_symbols = StringVar()
        self.seed_set = StringVar()
        super().__init__()

        frame1 = Frame(self)
        frame1.pack(fill="both", pady=5, padx=5)

        frame2 = Frame(self)
        frame2.pack(fill="both", pady=5, padx=5)

        frame3 = Frame(self)
        frame3.pack(fill="both", pady=5, padx=5)

        frame4 = Frame(self)
        frame4.pack(fill="both", pady=5, padx=5)

        self.first_line(frame1)
        self.second_line(frame2)
        self.third_line(frame3)
        self.fourth_line(frame4)

    def first_line(self, frame1):
        self.Label1 = Label(frame1, text="Lenght", width=8)
        self.Entry1 = Entry(frame1, textvariable=self.lenght)

        self.Label2 = Label(frame1, text="Register")
        self.Entry2 = Entry(frame1, width=10, textvariable=self.register)

        self.Label1.pack(side="left")
        self.Entry1.pack(side="left")
        self.Entry2.pack(side="right")
        self.Label2.pack(side="right")

    def second_line(self, frame1):
        self.numbers = BooleanVar()
        self.spec_symbols = BooleanVar()

        self.cb1 = Checkbutton(frame1, text="Numbers", variable=self.numbers)

        self.cb2 = Checkbutton(frame1, text="Spec symbols", variable=self.spec_symbols)

        self.cb1.pack(side="left")
        self.cb2.pack(side="right")

    def third_line(self, frame1):
        self.Label1 = Label(frame1, text="Word", width=8)
        self.Entry1 = Entry(frame1, textvariable=self.word)

        self.Label2 = Label(frame1, text="Language")
        self.Entry2 = Entry(frame1, width=10, textvariable=self.language)

        self.Label1.pack(side="left")
        self.Entry1.pack(side="left")
        self.Entry2.pack(side="right")
        self.Label2.pack(side="right")

    def fourth_line(self, frame1):
        self.Label1 = Label(frame1, text="Del symbols")
        self.Entry1 = Entry(frame1, textvariable=self.del_symbols)

        self.Label2 = Label(frame1, text="Seed")
        self.Entry2 = Entry(frame1, width=10, textvariable=self.seed_set)

        self.Label1.pack(side="left")
        self.Entry1.pack(side="left")
        self.Entry2.pack(side="right")
        self.Label2.pack(side="right")

class Panel3(Frame):
    def __init__(self):
        super().__init__()
        self.col_pas = StringVar()
        self.path = StringVar()

        frame = Frame(self)
        frame.pack(fill="both", pady=5, padx=5)

        self.second_line(frame)


    def second_line(self, frame):
        self.Label1 = Label(frame, text="Path to file save")
        self.Entry1 = Entry(frame, textvariable=self.path)

        self.Label2 = Label(frame, text="Col parols")
        self.Entry2 = Entry(frame, width=10, textvariable=self.col_pas)

        self.Label1.pack(side="left")
        self.Entry1.pack(side="left")
        self.Entry2.pack(side="right")
        self.Label2.pack(side="right")

    def save(self, func):
        try:
            path = self.path.get() or "password.txt"
            col_par = self.col_pas.get() or None

            if col_par == None or not col_par.isdigit() or int(col_par) not in range(0, 10000):
                messagebox.showinfo("error", "error col!!!!")
                return

            passwords = ""
            for a in range(0, int(col_par)):
                value = func()
                if "error" in value:
                    messagebox.showinfo("error", f"{value}!!!!")
                    return
                passwords += str(value) + "\n"

            with open(path, "w+", encoding="utf-8") as file:
                file.write(passwords)

            messagebox.showinfo("Ok", "success")
        except:
            messagebox.showinfo("error", "error path!!!!")


class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.generator = generator()
        self.geometry("450x320+525+150")
        self.title("Randomaizer passwords by Borikmm")

        btn = Button(self, text="Generate", command=self.gen)
        btn.pack(fill="both")

        self.Panel1 = Panel1()
        self.Panel1.pack(fill="both")

        frame1 = Frame(self)
        frame1.pack(fill="both")
        self.Label = Button(frame1, text="Copy", command=self.set_buf)
        self.Label.pack(fill="both")

        self.Panel2 = Panel2()
        self.Panel2.pack(fill="both")

        self.Panel3 = Panel3()

        frame2 = Frame(self)
        frame2.pack(fill="both")

        self.Label1 = Button(frame2, text="Save to file:", command=lambda: self.Panel3.save(self.gen))
        self.Label1.pack(fill="both")

        self.Panel3.pack(fill="both")

    def set_buf(self):
        result = str(self.Panel1.password.get())
        self.clipboard_clear()
        self.clipboard_append(result)

    def gen(self):

        def set_text(entry, text):
            entry.delete(0, "end")
            entry.insert(0, text)

        length = self.Panel2.lenght.get() if self.Panel2.lenght.get() else 10
        register = self.Panel2.register.get() or "low"
        numbers = self.Panel2.numbers.get() or False
        specific_symbols = self.Panel2.spec_symbols.get() or False
        word = self.Panel2.word.get() or None
        language = self.Panel2.language.get() or "eng"
        del_symbols = self.Panel2.del_symbols.get() or None
        seed = self.Panel2.seed_set.get() if self.Panel2.seed_set.get() else None

        checker = self.__check_valid(str(length), language, register, str(seed))
        try:
            if checker != "":
                raise ValueError
            if seed != None:
                seed = int(seed)
            value, seed = self.generator.get_password(int(length), numbers, specific_symbols, language, register, seed, word, del_symbols)
        except:
            value, seed = f"{checker} error", "error"

        set_text(self.Panel1.Entry1, value)
        set_text(self.Panel1.Entry2, seed)

        return value

    @staticmethod
    def __check_valid(length, language, register, seed):
        a = ""
        if length.isdigit():
            if int(length) not in range(0, 1000):
                a += "length "
        else:
            a += "length "
        if language not in ["ru", "eng"]:
            a += "language "
        if not seed.isdigit() and seed != "None":
            a += "seed "
        if register not in ["up", "low", "all"]:
            a += "register "
        a = ",".join(a.split())
        return a

if __name__ == '__main__':
    app = GUI()
    app["bg"] = "gray22"
    app.mainloop()



