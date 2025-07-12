import tkinter as tk
from tkinter import messagebox, ttk
from src.core import BrailleConverter

class BrailleGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🔤 Conversor Braille-Texto Multiparadigma")
        self.geometry("520x320")
        self.resizable(False, False)
        self.configure(bg="#292F36")
        self.converter = BrailleConverter()
        self._build_ui()

    def _build_ui(self):
        style = ttk.Style()
        style.configure('TButton', font=('Segoe UI', 11, 'bold'), foreground="#292F36", background="#C7E8F3")
        style.configure('TLabel', font=('Segoe UI', 11), background="#292F36", foreground="#EAF6FB")

        # Título
        ttk.Label(self, text="Conversor Braille-Texto", font=('Segoe UI', 18, 'bold')).pack(pady=10)

        # Cuadro de texto de entrada
        frame_in = tk.Frame(self, bg="#292F36")
        frame_in.pack(pady=5)
        self.input_text = tk.Entry(frame_in, font=("Segoe UI", 13), width=38)
        self.input_text.grid(row=0, column=0, padx=5)
        self.input_text.insert(0, "hola mundo")
        ttk.Button(frame_in, text="Limpiar", command=self.clear_input).grid(row=0, column=1, padx=4)

        # Botones
        frame_btn = tk.Frame(self, bg="#292F36")
        frame_btn.pack(pady=12)
        ttk.Button(frame_btn, text="Texto → Braille", width=18, command=self.to_braille).grid(row=0, column=0, padx=4)
        ttk.Button(frame_btn, text="Braille → Texto", width=18, command=self.to_text).grid(row=0, column=1, padx=4)

        # Resultado
        ttk.Label(self, text="Resultado:", font=('Segoe UI', 12, 'italic')).pack()
        self.result_box = tk.Text(self, font=("Segoe UI", 16), width=35, height=2, bg="#FAF9F6", fg="#1B2430", borderwidth=2, relief="solid")
        self.result_box.pack(pady=8)
        self.result_box.config(state="disabled")

        # Pie de página
        ttk.Label(self, text="Proyecto Multiparadigma • Python", font=('Segoe UI', 9)).pack(side="bottom", pady=6)

    def clear_input(self):
        self.input_text.delete(0, tk.END)
        self.result_box.config(state="normal")
        self.result_box.delete("1.0", tk.END)
        self.result_box.config(state="disabled")

    def to_braille(self):
        text = self.input_text.get()
        result = self.converter.text_to_braille(text)
        self._show_result(result.converted_text)
        if not result.success:
            messagebox.showerror("Error", result.error_message or "Conversión fallida")

    def to_text(self):
        braille = self.input_text.get()
        result = self.converter.braille_to_text(braille)
        self._show_result(result.converted_text)
        if not result.success:
            messagebox.showerror("Error", result.error_message or "Conversión fallida")

    def _show_result(self, text):
        self.result_box.config(state="normal")
        self.result_box.delete("1.0", tk.END)
        self.result_box.insert(tk.END, text)
        self.result_box.config(state="disabled")

if __name__ == "__main__":
    app = BrailleGUI()
    app.mainloop()
