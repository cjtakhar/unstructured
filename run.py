import unstructured_client
from unstructured_client.models import operations, shared, errors
import sys
import os

def install_package(package):
    os.system(f"{sys.executable} -m pip install {package}")

def main():
    try:
        import unstructured_client
    except ImportError:
        print("unstructured-client is not installed. Installing...")
        install_package("unstructured-client")

    # Input the API key and file name
    api_key = input("Enter your API key: ")
    filename = input("Enter the file name (with path): ")

    # Check if the file exists in the current directory
    if not os.path.isfile(filename):
        print(f"File '{filename}' not found in the current directory.")
        return

    try:
        client = unstructured_client.UnstructuredClient(
            api_key_auth=api_key,
            server_url="https://api.unstructuredapp.biz"  # Specify the API URL here
        )

        with open(filename, "rb") as file:
            res = client.general.partition(request=operations.PartitionRequest(
                partition_parameters=shared.PartitionParameters(
                    files=shared.Files(
                        content=file.read(),
                        file_name=filename,
                    ),
                    strategy=shared.Strategy.HI_RES,
                    chunking_strategy=shared.ChunkingStrategy.BY_PAGE,
                ),
            ))

        if res.elements is not None:
            print("Response received:")
            for element in res.elements:
                print(element)
        else:
            print("No elements found in the response.")
    except errors.SDKError as e:
        print(f"API error occurred: {e.status_code}")
        print(e.response_text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
