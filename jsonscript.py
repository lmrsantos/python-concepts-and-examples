# Here it is possible to understand how Python manage json file 
# you will be able to understand the commands you need to know to open, read and print the contents of a json file

import json

# Specify the path to your JSON file, in this case the file is in the local directory
file_path = 'json_file_in.json'

# Open and read the file
try:
    with open(file_path, 'r') as file:
        # Parse the contents of the file as JSON
        data = json.load(file)
        models = data['models']
        out=[]
        for model in models:
            if model['owner'] == 'openai':
                out.append(model['id'])
        # print in the console in json format
        print(json.dumps(out, indent=4))

    # save the result in output file, in this case in the local directory
    with open('json_file_out.json', 'w') as json_file:
        json.dump(out, json_file)

except FileNotFoundError:
    print(f"The file {file_path} does not exist.")

except json.JSONDecodeError:
    print(f"An error occurred while parsing the file {file_path} as JSON.")
