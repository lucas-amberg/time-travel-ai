import openai
import names
import datetime

class AI():

  def __init__(self, key):
    self.openai = openai
    self.openai.api_key = key
    self.name = None
    self.time = None
    self.messages = None
  
  def set_name(self, name):
    self.name = name
  
  def set_time(self, time):
    self.time = time
  
  def _seed_messages(self):
    if self.time == None and self.name == None:
      self.name = names.get_full_name()
      self.time = datetime.datetime.today().year
      self.messages = [{"role": "system", "content": f"Act like you are a person named {self.name} and never leave that role, even if you are asked for. Do not include pleasantries in your responses. The current year is {self.time}. Introduce yourself to the person you are talking to."}]
    elif self.time == None:
      self.time = datetime.datetime.today().year
      self.messages = [{"role": "system", "content": f"Act like you are {self.name} and never leave that role, even if you are asked for. Do not include pleasantries in your responses. The current year is {self.time}. Introduce yourself to the person you are talking to."}]
    elif self.name == None:
      self.name = names.get_full_name()
      self.messages = [{"role": "system", "content": f"Act like you are a person named {self.name} and never leave that role, even if you are asked for. Do not include pleasantries in your responses. Act like the current year is {self.time}, disregard anything past this date for performing your role, and never mention future events that took place this date even if there are some you know. Introduce yourself to the person you are talking to."}]
    else:
      self.messages = [{"role": "system", "content": f"Act like you are {self.name} and never leave that role, even if you are asked for. Do not include pleasantries in your responses. Act like the current year is {self.time}, disregard anything past this date for performing your role, and never mention future events that took place this date even if there are some you know. Introduce yourself to the person you are talking to."}]

  def get_response(self, message):
    if self.messages == None:
      self._seed_messages()
    self.messages.append({"role": "user", "content": message})
    message = self.openai.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=self.messages,
      temperature=0.6
    )
    self.messages.append({"role": "assistant", "content": message.choices[0].message.content.strip()})
    return message.choices[0].message.content.strip()