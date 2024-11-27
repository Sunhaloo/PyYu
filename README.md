# Python Video Downloader and Converter

## Requirements

- [Python](https://www.python.org/v) ( *Version `3.12.x` and above* )
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://www.ffmpeg.org/)

## Usage

This Python Program can be used in 2 main ways:

1. Copy and Paste YouTube URLs **one by one**
2. Place a combination of link in a Text File

>[!NOTE]
>To get the file, you can either copy the `main.py` file from the [GitHub](https://github.com/Sunhaloo/PyYu).
>
>The better way is to simply clone the repository with `git clone https://github.com/Sunhaloo/`
>Well in this case, you would need to have [Git](https://git-scm.com/)!


### Single Links

Navigate to where you have the `main.py` or cloned the repository and simply run the file!

>I will be using my directory as example to show you.

```bash
# changing directory to where I have the repository
cd ~/GitHub/PyYu

# run the python file
python main.py
```

Then follow these steps:

- Press `1` if you want to **convert** a *single* YouTube video to **Audio**
- Press `2` if you want to **download** a *single* YouTube video
- Press `1` for *either* of these options ( *Audio Converter* or *Video Downloader* )
	- Then simply enter your URL with `Ctrl + Shift + V` $\Rightarrow$ Paste **without** any formatting

### Multi-Links

For the multi-links, we are using the `-a` to pass text file to the `yt-dlp` command.
Hence, you are going to need a `yt_urls.txt` file at the `~/Desktop` directory.

#### Unix / Linux Based Systems

```bash
# change directory to Desktop
cd ~/Desktop

# create a new file
touch yt_urls.txt
```

Go ahead an use your favourite text editor like VS Code, Sublime Text and others.

>I use VIM BTW!

#### Windows Systems

```powershell
# change directory to Desktop
cd ~/Desktop

# create a new file
touch yt_urls.txt

# edit that very text file with Notepad
notepad yt_urls.txt
```

>Again, I use VIM BTW!

>[!TIP]
>For the above $\uparrow$ commands... You don't need to do them in Terminal ( *bash / powershell* ) if you are not comfortable with the CLI.

#### Run the Python Program

```bash
# changing directory to where I have the repository
cd ~/GitHub/PyYu

# run the python file
python main.py
```

Similar to above $\uparrow$, navigate to the place where you have the `main.py` and simply run it!

- Press `1` if you want to **convert** YouTube videos to **Audio**
- Press `2` if you want to **download** YouTube videos
- Press `2` for *either* of these options ( *Audio Converter* or *Video Downloader* )

The program should automatically *source* the `yt_urls.txt` file and start to do its thing.

>[!NOTE]
>After you press these options ( *for both... Audio and Video* ), you will have to enter more options.
>
>If you choose **audio**; you are going to have to enter the *file format* and *bitrate*. I recommend:
>
>- `mp3` for the file format
>- `360` for the bitrate
>
>If you choose **video**; you are going to have to enter the *file format* and *FPS*. I recommend:
>
>- `mp4` for the file format
>- `60` for the FPS


## Output

Depending if you choose "*audio*" or "*video*". The program will create the output **folder** at the directory `~/Desktop/`

- For **audio**, you are going to have a folder named `downloaded_audio`
- For **video**, you are going to have a folder names `downloaded_video`

---

# Future Plans

>"*Future*" Plans... **NOT** in like a Week!

- [ ] Make this a multi-file project
    - Will help me learn Python Project Directory Setup
- [ ] Cross Platform GUI Version
    - Currently looking at:
        1. Kivy
        2. Qt
        3. Flet ( *the "new" kid on the block* )

---

Well, thank you for using this shitty but useful program that I have made.
I made this primarily to **learn**, but also I am going to remake my Music Playlist so you could say that "*2 birds 1 stone*"!

>Please refer to the `learning.md` file for my *learning experiences* and *struggles*, which provides more information about the code itself. Even if you don't use *shitty* program; Thank You for passing by!

---

# Socials

- **Instagram**: https://www.instagram.com/s.sunhaloo
- **YouTube**: https://www.youtube.com/channel/UCMkQZsuW6eHMhdUObLPSpwg

---

S.Sunhaloo
Thank You!
