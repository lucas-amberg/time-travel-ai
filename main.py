from ai import *
import os
import re
import time



# Main function
def main():
  print('Welcome to Time Travel AI!')
  api_key = get_api_key()
  print()
  print('API key accepted!')

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