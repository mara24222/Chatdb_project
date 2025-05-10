# Chatdb project using entertainment, fitness, and shopping databases
# This project allows users to ask questions in natrual languge and then the AI model converts it into SQL queries and produces an answer. 

# This project utilizes chatgpt as its AI model in order to translate natrual languge into sql queries. 
# For this project I created three databases using MYSQL based off of datasets I found on kaggle. 
# The three databases are Fitness, Entertainment(Netflix user info), and shopping(customer information along with purchase information)



# Tech Stack
Python 3.12.7
Open AI GPT-3.5 API
MYSQL
MYSQL connector 
streamlit 

# How to run everything 
## How to Run the Project:

# 1. Download the Databases:
   - `entertainment` (Netflix user info)
   - `GYM` (fitness-related data)
   - `shopping` (customer and purchase data)

# 2. Install Python:
   Download and install Python 3.12.7

# 3. Install MySQL and Connect to Databases:
   - Ensure MySQL is installed and running on your machine.
   - Connect the `MYSQL Connector` to link your Python code to the databases.

# 4. Optional: Run Streamlit for a Nice UI
   - Install Streamlit using `pip install streamlit`.
   - You can then run `streamlit run <script_name>.py` to start the interactive UI.

# 5. Obtain API Key:
   - Sign up for OpenAI and obtain your API client key.
   - Add your API key to the script to make requests to GPT-3.5.

# Note, u will need your own API client key in order to make the API request
