import tkinter as tk

class Calculator:

    def __init__(self, root):

        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        self.input_text = tk.StringVar()

        input_frame = tk.Frame(root)
        input_frame.pack()

        input_field = tk.Entry(
            input_frame,
            textvariable=self.input_text,
            font=('arial', 20),
            bd=10,
            insertwidth=2,
            width=14,
            borderwidth=4,
            justify='right'
        )

        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        btns_frame = tk.Frame(root)
        btns_frame.pack()

        buttons = [
            ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
            ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
            ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
            ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3)
        ]

        for (text,row,col) in buttons:

            tk.Button(
                btns_frame,
                text=text,
                width=5,
                height=2,
                font=('arial',18),
                command=lambda t=text:self.click(t)
            ).grid(row=row,column=col,padx=5,pady=5)

        tk.Button(
            root,
            text="Clear",
            width=20,
            height=2,
            font=('arial',12),
            command=self.clear
        ).pack(pady=5)


    def click(self, item):

        if item == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""

        else:
            self.expression += str(item)
            self.input_text.set(self.expression)


    def clear(self):
        self.expression = ""
        self.input_text.set("")


if __name__ == "__main__":

    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
