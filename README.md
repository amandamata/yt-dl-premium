# YouTube Video Downloader

This script allows you to download videos from YouTube, including premium content, using cookies for authentication.

## Installation

1. **Clone this repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Install `yt-dlp`**:
    ```bash
    pip install yt-dlp
    ```

## Exporting Cookies

To download premium content, you need to export your YouTube cookies from your browser.

### Steps to Export Cookies

1. **Install a browser extension** to export cookies. We recommend using [EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg) or [Get cookies.txt](https://chrome.google.com/webstore/detail/get-cookiestxt/lgpdjdcokldibneegfobpfgknagdfbfb).

2. **Visit YouTube** and log in to your account.

3. **Export the cookies** using the browser extension and save them to a file named `cookies.txt`.

## Running the Script

1. **Modify the script**:
    - Open `download_video.py`.
    - Set the `video_url` variable to the URL of the video you want to download.
    - Set the `output_folder` variable to the desired output folder path where you want to save the downloaded video.

    ```python
    import yt_dlp
    import os

    cookies_file = 'cookies.txt'
    video_url = 'URL_OF_THE_VIDEO'
    output_folder = 'path/to/output/folder'

    ydl_opts = {
        'cookiefile': cookies_file,
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'format': 'best',
    }

    def download_video(url):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    if __name__ == '__main__':
        download_video(video_url)
    ```

2. **Run the script**:
    ```bash
    python3 yt-dl-premium.py
    ```

The video will be downloaded to the specified output folder.

## Notes

- Ensure the `cookies.txt` file is in the same directory as the script, or update the `cookies_file` variable to the correct path.
- Keep the `cookies.txt` file up to date as cookies can expire.
- Verify the legality and terms of service compliance for downloading content from YouTube.

