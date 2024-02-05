import time

class Log():
  def __init__(self):
    self.name = None
    self.file = None
  
  def create_log_file(self, ai):
    self.name = f'{ai.name}-{ai.time}-{time.time()}-log.txt'
    self.file = open(f'./logs/{self.name}', 'x')
  
  def write_to_log(self, message):
    self.file.write(f'{message}')
  
  def print_and_log(self, message):
    print(message)
    self.write_to_log(message)

  def get_input_and_log(self, message):
    user_input = input(message)
    self.write_to_log(f'{message}{user_input}\n')
    return user_input
  
  def new_line(self):
    print()
    self.write_to_log('')