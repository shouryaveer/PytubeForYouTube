# PytubeForYouTube
This repository shows how you can use Pytube package in Python to download videos from YouTube. Get python installed on your computer &amp; Check out the instructions below to try it yourself:
1) First install pytube using: 'pip install pytube3' command.
2) Clone the pytube git repository using: git clone https://github.com/nficano/pytube.git
3) Embed & install this source code to your pytube package dir by changing your directory using 'cd pytube' & entering 'pip install .'
4) Next execute the code file "yt.py" in this repo from your IDE or using 'python qr.py' from your terminal
5) When executed, you'll get a list of stream formats in your output. You can select any stream resolutions
   from your output by their "itag" & then add it in the blank space between '' in: video.streams.get_by_itag(' ').download()
6) You can also specify your own download location in .download() function: .download('your-path-directory')
