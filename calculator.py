import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.current_input = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self.root, textvariable=self.current_input, font=('Arial', 18), bd = 10, insertwidth=2, width=14, borderwidth=4)
        entry.grid(row=0, column=0, columnspan=4)

        button = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]     

        row_val = 1
        col_val = 0
        for button in button:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 18), command=action).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
    def on_button_click(self, char):
        if char == '=':
            try:
                result = eval(self.current_input.get())
                self.current_input.set(result)
            except Exception as e:
                self.current_input.set("Error")
        elif char in ('+', '-', '*', '/', '.'):
            if self.current_input.get() and self.current_input.get()[-1] not in ('+', '-', '*', '/', '.'):
                self.current_input.set(self.current_input.get() + char)
        else:
            self.current_input.set(self.current_input.get() + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()