import requests
import json

def main():
    url = 'https://harvarduniversity-js07qb0d.api.unstructuredapp.io/general/v0/general'
    api_key = input("Enter your API key: ")
    file_path = input("Enter the file name (with path): ")
    output_file = input("Enter the output JSON file name (with path): ")

    headers = {
        'accept': 'application/json',
        'unstructured-api-key': api_key,
    }

    try:
        with open(file_path, 'rb') as file:
            files = {
                'files': file
            }

            response = requests.post(url, headers=headers, files=files)

            print(f"Status code: {response.status_code}")
            if response.status_code == 200:
                print("Response received, saving to file...")
                with open(output_file, 'w') as json_file:
                    json.dump(response.json(), json_file, indent=4)
                print(f"Data successfully saved to {output_file}")
            else:
                print("Failed to partition the document:")
                print(response.text)

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
