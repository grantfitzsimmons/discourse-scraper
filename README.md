# Discourse Scraper

This script allows you to create markdown files from every post you have access to on your Discourse instance.

## Configuration

1. Obtain the list of IDs you want to save

   I wanted to download every topic with IDs from 1 - 1246, so I set the `start_num` to `1` and `end_num` to `1246`.
   
   ```py
   # Set the base URL and range of file numbers
   base_url = 'https://discourse.specifysoftware.org/raw/'
   start_num = 1
   end_num = 1246
   ```
   
   These can be set to whatever set of numbers you would like.
   
2. Set the save directory to wherever you desire

   ```py
   # Set the directory where you want to save the downloaded files
   save_directory = 'posts'
   ```
   
   This saves it to a directory named `posts` in the current folder.
   
3. Obtain your API key from Discourse and insert it here:

   ```py
   # Set your API key generated from Discourse
   api_key = 'your-api-key-here'
   ```
   
   Replace `your-api-key-here` with your API key that you generated.
   
4. Run the script

   ```zsh
   python3 get_data.py
   ```