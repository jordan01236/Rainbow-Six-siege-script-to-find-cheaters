import os
import time
import requests
from bs4 import BeautifulSoup
import re

# Specify the folder path using raw string literal
folder_path = r"C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\cache\avatars"

# Define the base URL
base_url = "https://stats.cc/siege/"

# ANSI escape codes for text formatting
COLOR_RED = '\033[91m'
COLOR_BLUE = '\033[94m'
COLOR_GREEN = '\033[92m'
COLOR_END = '\033[0m'
BOLD = '\033[1m'

# Set to store processed file names
processed_files = set()

# Look for known cheaters
def is_cheater(account_id):
    with open(r'C:\Cheaters\Cheaters.txt', 'r') as file:
        cheater_ids = file.read().splitlines()
    return account_id in cheater_ids

while True:
    # Get a list of all files and directories in the specified folder
    files_and_dirs = os.listdir(folder_path)

    # Filter out directories, leaving only files
    file_names = [f for f in files_and_dirs if os.path.isfile(os.path.join(folder_path, f))]

    # Strip everything after an underscore (_) in each file name
    stripped_files = [f.split('_')[0] for f in file_names]

    # Remove duplicates while preserving the order
    account_ids = list(dict.fromkeys(stripped_files))

    # Process only new files
    new_account_ids = [account_id for account_id in account_ids if account_id not in processed_files]

    for account_id in new_account_ids:
        url = base_url + account_id
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Fetching data for account ID: {account_id}\n")
            # Parse the HTML content of the response
            soup = BeautifulSoup(response.content, 'html.parser')

            # Find the username
            username_element = soup.find('h2', class_='text-2xl truncate')
            if username_element:
                username = username_element.get_text(strip=True)
                print("Username:", username)

            # Find the KD value
            kd_element = soup.find('span', string='KD')
            if kd_element:
                kd_value = kd_element.find_next_sibling('span').get_text(strip=True)
                print("KD:", end=' ')
                if float(kd_value) > 2.0:
                    print(COLOR_RED + kd_value + COLOR_END)
                elif 1.5 <= float(kd_value) <= 2.0:
                    print(COLOR_BLUE + kd_value + COLOR_END)
                else:
                    print(kd_value)
            else:
                print("KD value not found")


            # Find the matches played

            matches = soup.find('div', class_='text-contrast-500').text.strip()
            print(f"Matches: {matches}")



            # Find shitters
            if float(kd_value) < 1.0:
                print(COLOR_GREEN + kd_value + " THIS GUY SUCKS" + COLOR_END)

            # Find the win rate element
            win_rate_element = soup.find('span', string='WR')
            if win_rate_element:
                # Navigate to the next sibling span element to get the win rate value
                win_rate_value = win_rate_element.find_next_sibling('span').get_text(strip=True)
                print("Win Rate:", win_rate_value)
            else:
                print("Win rate not found")

            # Find the kills per match
            kills_per_match_div = soup.find('p', string='kills per match').parent
            if kills_per_match_div:
                # Find the next span element with class "text-xl"
                kills_per_match_span = kills_per_match_div.find_next('span', class_='text-xl')
                if kills_per_match_span:
                    kills_per_match_value = kills_per_match_span.get_text(strip=True)
                    print("Kills per Match (Last 7 Days):", kills_per_match_value)
                else:
                    print("Kills per Match value (Last 7 Days) not found")
            else:
                print("Div containing 'kills per match' not found")

            # Find the account level
            level_element = soup.find('span', class_='bg-base-200 border-base-200 rounded-md border px-2 shadow-lg')
            if level_element:
                account_level = level_element.get_text(strip=True)
                account_level = int(account_level)  # Convert to integer for comparison
                print("Account Level:", end=' ')
                if account_level < 150:
                    print(COLOR_BLUE + BOLD + str(account_level) + COLOR_END)
                else:
                    print(account_level)
            else:
                print("Account level information not found")

            # Check if the account ID is in the list of cheaters
            if is_cheater(account_id):
                print(COLOR_RED + BOLD + "Known Cheater" + COLOR_END)

            #reputation bans
            repBan = soup.find('h4', class_='flex items-center gap-2 p-3 border-b border-base-100').text.strip()

            if repBan == "Reputation Bans":
                print(COLOR_RED + BOLD +"Reputation Ban" + COLOR_END)
            else:
                print('')




            #Previous Season Stats

            # Find all elements that match the criteria
            elements = soup.find_all('div', class_='flex w-full pl-2 pr-1 font-medium')

            # Check if there are at least two matching elements
            if len(elements) >= 2:
                # Extract text from the second element (index 1)
                input_string = elements[1].text.strip()

                # Proceed with further processing on input_string
                # Define your regex patterns and continue with your logic as before
                kd_pattern = r'(\d+)(KD([\d.]+))'  # Example pattern
                wr_pattern = r'(WR([\d%]+))'  # Example pattern

                kd_match = re.search(kd_pattern, input_string)
                wr_match = re.search(wr_pattern, input_string)

                if kd_match and wr_match:
                    matches_number = kd_match.group(1)  # Example processing
                    kd_value = float(kd_match.group(3))  # Example processing

                    # Your further processing logic here
                    # ...

                    # Example of formatted output
                    formatted_output = f"Matches: {matches_number} KD: {kd_value} WR: {wr_match.group(2)}"
                    print(formatted_output)
                else:
                    print("Input string does not match expected format.")
            else:
                print("Not enough matching elements found.")




            print()  # Add a new line after each account's data

            # Add the processed account ID to the set
            processed_files.add(account_id)
        else:
            print(f"Failed to fetch data for account ID: {account_id}")

    # Sleep for some time before checking again
    time.sleep(0.5)  # Check every 0.5 seconds for new files
