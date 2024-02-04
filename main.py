from ai import *
import customtkinter as tk
import os
import re

class GUI(tk.CTk):

  def __init__(self):
    super().__init__()
    self.geometry("800x600")
    self.title('Time Travel AI')
    tk.set_default_color_theme('dark-blue')
  
  def change_title(self, title):
    if title:
      self.title(title)
    
  def get_api_key(self):
    if os.environ.get('OPENAI_API_KEY'):
      label = tk.CTkLabel(self, text="Retrieving API Key From Environment Variables...", anchor='center', font=("Comic Sans MS", 20))
      label.place(x=400, y=300, anchor='center')
      self.after(2000, self._clear_frame)
      return os.environ.get('OPENAI_API_KEY')
    else:
      self._clear_frame()
      textbox = tk.CTkEntry(self, "OpenAI API Key")
      textbox.place(x=400, y=200, anchor='center')
      button = tk.CTkButton(self, "Submit", command=lambda: self._check_and_return_key(textbox.get()))
      button.place(x=400, y=400, anchor='center')
    
    def _check_and_return_key(self, key):
      if re.match(r'^sk-[a-zA-Z0-9]{24}$', key):
        self._clear_frame()
        return key
      else:
        label = tk.CTkLabel(self, text="Invalid API Key", anchor='center', font=("Comic Sans MS", 20))
        label.place(x=400, y=300, anchor='center')  
        self.after(2000, self.get_api_key)
        
    
  def _clear_frame(self):
    for widget in self.winfo_children():
      widget.destroy()


# Main function
def main():
  # Create the window
  gui = GUI()
  api_key = gui.get_api_key()
  gui.mainloop()

# Run the program
if __name__ == "__main__":
  main()