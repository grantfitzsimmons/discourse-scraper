import urllib.request
import os
import time

# Generate the list of file URLs
def generate_file_urls(base_url, start_num, end_num):
    file_urls = []
    for i in range(start_num, end_num + 1):
        file_urls.append(base_url + str(i))
    return file_urls

# Download the files
def download_files(file_urls, save_directory, api_key):
    # Create the save directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # Add headers to the request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
        'Api-Key': api_key
    }

    # Download each file
    for url in file_urls:
        file_name = url.split('/')[-1]  # Extract the file name from the URL
        save_path = os.path.join(save_directory, file_name + '.md')  # Save files as Markdown files

        # Create the request object with headers
        req = urllib.request.Request(url, headers=headers)

        try:
            # Download the file
            with urllib.request.urlopen(req) as response, open(save_path, 'wb') as out_file:
                data = response.read()
                out_file.write(data)
            print(f'Saved {file_name} to {save_path}')
        except urllib.error.HTTPError as e:
            print(f"Failed to download {url}. Error: {e}")

        time.sleep(1)  # Adjust the sleep duration as needed (e.g., 1 second)

    print('Download complete!')

# Set the base URL and range of file numbers
base_url = 'https://discourse.specifysoftware.org/raw/'
start_num = 1
end_num = 1246

# Set the directory where you want to save the downloaded files
save_directory = 'posts'

# Set your API key generated from Discourse
api_key = 'your-api-key-here'

# Generate the list of file URLs
file_urls = generate_file_urls(base_url, start_num, end_num)

# Download the files
download_files(file_urls, save_directory, api_key)
