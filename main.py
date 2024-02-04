from ai import *
import customtkinter as tk
import os

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
      print('retrieved api key')
      textbox = tk.CTkLabel(self, text="Retrieving API Key From Environment Variables...", anchor='center', font=("Comic Sans MS", 20))
      textbox.place(x=400, y=300, anchor='center')
      return os.environ.get('OPENAI_API_KEY')
    else:
      self._clear_frame()
      textbox = tk.CTkEntry(self, "API Key")
      textbox.pack()
    
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