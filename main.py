from ai import *
import customtkinter as tk

class GUI(tk.CTk):

  def __init__(self):
    super.__init__()
    self.geometry("800x600")
    self.title('Time Travel AI')
  
  def change_title(self, title):
    if title:
      self.title(title)
    
  def get_api_key(self):
    


# Main function
def main():
  # Create the window
  gui = GUI()

  gui.mainloop()

# Run the program
if __name__ == "__main__":
  main()