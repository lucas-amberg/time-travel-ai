from ai import AI
import os
import re
import time
import datetime
from log import Log

# Main function
def main():
  print('Welcome to Time Travel AI!')
  api_key = get_api_key()
  print()
  time.sleep(1)
  print('API key accepted!')
  print()
  time.sleep(1)

  # Create an AI object
  ai = AI(api_key)

  

  valid_options = ['1', '2', 'X', 'Q'] # Valid options for the user to select
  option = ''
  while option != 'X': # Loop until the user selects the option to begin the conversation
    # Display the menu
    print('Please select an option from the menu below:')
    print('\t[1] Set the name of the person you would like the AI agent to become')
    print('\t[2] Set the year you would like the AI agent to act like it is')
    print('\t[X] Begin the conversation')
    print('\t[Q] Quit the program')
    option = input('> ')
    if option not in valid_options:
      print('Invalid option. Please select a valid option.')
      print()
    elif option == '1': # If the user selects the option to set the name, call the get_name method of the AI object
      ai.get_name()
    elif option == '2': # If the user selects the option to set the year, call the get_time method of the AI object
      ai.get_time()
    elif option == 'X': # If the user selects the option to begin the conversation, begin the conversation
      break
    elif option == 'Q': # If the user selects the option to quit the program, exit the program
      print('Quitting the program...')
      exit()
    
  
  # Begin the conversation
  ai.seed_messages()
  log = Log()
  log.create_log_file(ai)
  start_time = time.time()
  message_count = 0
  log.print_and_log('Beginning the conversation...\n')
  log.print_and_log(f'The year is {ai.time if ai.time else datetime.datetime.today().year}. You are now entering a conversation with {ai.name if ai.name else "somebody"}...\n')
  while True:
    user_message = log.get_input_and_log('You: ') # Get the user's message and log it
    log.new_line()
    response = ai.get_response(user_message)
    if ('goodbye' in response.lower() and 'goodbye' in user_message.lower()) or ('bye' in response.lower() and 'bye' in user_message.lower()):
      log.print_and_log(f'{ai.name}: {response}\n')
      log.new_line()
      message_count += 2 # Increment the message count by 2
      break
    log.print_and_log(f'{ai.name}: {response}\n') 
    log.new_line()
    message_count += 2 # Increment the message count by 2
  log.print_and_log(f'Conversation ended after {round(time.time() - start_time, 2)} seconds with {message_count} messages.') # Log the end of the conversation
    


# This function will get the API key from the user
# If the user selects option 1, the function will attempt to get the API key from the environment variable
# If the user selects option 2, the function will prompt the user to input the API key
def get_api_key():
  time.sleep(1)
  print('This program requires an OpenAI API Key to run...')
  time.sleep(1)
  print()
  print('Please select an option for submitting an OpenAI API key:')
  print('\t[1] Gather API key from environment variable (OPENAI_API_KEY)')
  print('\t[2] Manually input API key')
  valid_options = ['1', '2']
  option = ''

  # Get the user's option and validate it to ensure it is a valid option
  while option not in valid_options:
    option = input('> ')
    if option not in valid_options:
      print('Invalid option. Please select a valid option.')
      print()

  if option == '1': # Get API key from environment variable
    api_key = os.environ.get('OPENAI_API_KEY')
    if api_key == None:
      print('API key not found in environment variable')
      return get_api_key() # Recursion
    else:
      return api_key
    
  elif option =='2': # Manually input API key
    valid = False # Flag to check if the API key is valid
    while not valid:
      print('Please input your API key: ')
      api_key = input('\n> ')
      # Validate the API key
      match = re.search(r"^sk-[a-zA-Z0-9]{32,}$", api_key)
      if match: # If the API key is valid, return it
        return api_key
      else: # If the API key is invalid, prompt the user to input a valid API key
        print('Invalid API key. Please input a valid API key.')
        print()
    

# Run the program
if __name__ == "__main__":
  main()