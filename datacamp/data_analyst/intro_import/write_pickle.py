import os
import pickle


curso_dir = 'C:\\Users\\tiagog\\Documents\\curso-python'
data_dir = curso_dir + '\\datacamp\\data_analyst\\intro_import\\data'
os.chdir(data_dir)

data = {'June': '69.4', 'Aug': '85', 'Airline': '8', 'Mar': '84.4'}

# using encode() + dumps() to convert to bytes
# data_bytes = json.dumps(data).encode('utf-8')

with open('data.pkl', 'ab') as file:
    pickle.dump(data, file)
