>[!NOTE]
>I am writing this after **3 weeks**; hence, I am not going to bother about what I needed to "*write about*" here.
>Instead, I am just going to freely write about what I think is important ( _to be honest... **Everything is Important**_ ) and just go with the flow.

---

# Find the Size of a File

I wanted a way to find out if the text file `yt_urls.txt` contains links.
Because the user might have used the program before and deleted all the contents of *that* file. Hence, I wanted to perform a check if the file is empty or not!

There are a couple of ways of how we can proceed ( *that I know of* ). We can either use:

- `os.path.getsize(file_path)`
- `os.stat(file_path).st_size`

>I went on to use the first "*method*"!

## First Iteration

```python
# function to check for the file size
def check_file_size(file_path: str):
    # exception handling
    try:
        # get the size of the file in question
        txt_file_size = os.path.getsize(file_path)

        # output appropriate message based on size of text file
        # NOTE: this method `.getsize()` return size in bytes
        if txt_file_size == 0:
            # meaning that we have nothing in the file
            print_dashed_line()
            print("<-- The Text File Does NOT Contains Any URLs... Exiting!!! -->")
            print_dashed_line()

            # exit the program
            exit(0)

    # if file has not been found
    except FileNotFoundError as e:
        # NOTE: extracting the file name in the `except` part
        # so that it does not run if the text file has stuff in it ( innit )

        # split the path of file into a list
        path_split = file_path.split("/")
        # get the last value of the list
        file_name = path_split[len(path_split) - 1]

        # output appropriate message
        print(f"\nError: {e}")
        print(f"File '{file_name}' Has NOT Been Found at Desktop!!!")
```

## Second Iteration

>[!INFO]
>I am actually updating this function in this very moment!

```python
def check_file_size(file_path: str):
    # exception handling
    try:
        # then, get the size of the file
        file_size = os.path.getsize(file_path)

        # output the appropriate message
        if file_size == 0:
            # meaning we have no URLS in the file
            print_dashed_line()
            print("<-- The Text File Does NOT Contains Any URLs... Exiting!!! -->")
            print_dashed_line()

            # exit the program
            exit(0)

    # if file has not been found
    except FileNotFoundError as e:
        # get the name of the text file from file path
        # NOTE: we get the file name here because it will only run when needed
        file_name = os.path.basename(file_path)

        # output appropriate message
        print(f"\nError: {e}")
        print(f"File '{file_name}' Has NOT Been Found at Desktop!!!")
```

>Much smaller, we are getting the file name correctly in just **one line**!

### Explanation

At the time I did not know that we have `os.path.basename(file_path)`. Hence, I used my tiny brain with 2 of its brain cell left. They talked to each other and said, let's make the **file path** into a **list**.

Take a look below:

#### My Version with the List

```python
'''
Let's say that our file path ( with text file ) looks something like this:
	`~/Desktop/Folder1/Sub_Folder1/Something_Shit_Here/WTF_man/shit_on.txt`
What we are trying to do here is get the part where it says "shit_on.txt".
In addition, we know whatever text file or file in general we have in path...
Well, its going to **always** be at the end of the file path ( as you can see above ).

Hence, this is why my shitty list approach works... Lets' try it and compare it to the new one
'''
# well make a file path variable
file_path = "~/Desktop/Folder1/Sub_Folder1/Something_Shit_Here/WTF_man/shit_on.txt"
# split the file path by the character '/' obviously
file_path_splitted = file_path.split('/')
'''
well the variable `file_path_splitted` is a list of strings containing words / folder / files splitted at the character '/'.
Hence, the output of `file_path_splitted` should ( in this case ) look something like this
	['~', 'Desktop', 'Folder1', 'Sub_Folder1', 'Something_Shit_Here', 'WTF_man', 'shit_on.txt']
Finally get the last "value" of this list
'''
file_name = file_path_splitted[len(file_path_splitted) - 1]
# therefore the output of `file_name` will be ==> 'shit_on.txt'
```

>Lot of work to get that thing

#### The more Pythonic Version

```python
# remember to import the os module
import os
# our file path
file_path = "~/Desktop/Folder1/Sub_Folder1/Something_Shit_Here/WTF_man/shit_on.txt"
# well to get the file name just do
file_name = os.path.basename(file_path)
# similarly we get ==> 'shit_on.txt'
```

---

# Function to Check YouTube URLs

To be honest with you this was not needed. Because how can someone make a mistake while copying a YouTube URL or any URL for that matter.
But I made this because *I wanted to*!

>[!NOTE]
>If you are using your mouse like a peasant to highlight, copy and paste URLs... You can go fuck yourself with a toothbrush.
>We chads use `<Ctrl> + L`, `<Ctrl> + C` and `<Ctrl> + Shitf + V` to highlight, copy and paste without any formatting respectively.
>"*Be like Chads*"

>[!WARNING]
>I know **nothing** about *Regular Expressions* ( **Regex** )!
>Here is a great  YouTube Video about Regular Expressions: https://www.youtube.com/watch?v=K8L6KVGG-7o

## 2 Separate Function or 1 Function that does Both.

In the program we have 2 main types of input for the YouTube URLs.

1. The user enters a single YouTube URL
2. We get a list of URLs from the Text File

I thought that I would not be able to make the 1 function that does checks for both of them... Then I realised... `os.path.isfile(file_path)` does exists. Therefore we get this function:

```python
# function to check if YouTube URL is valid
def check_yt_url(input: str):
    # check if the input argument is a file or not
    if os.path.isfile(input):
        # open the file for read as "input" is a file
        with open(input, "r", encoding="utf-8") as txt_file:
            # start iterating through the text file
            for line_number, url in enumerate(txt_file):
                # remove the new line characters from URL
                url = url.strip()

                # skip any blank lines
                if not url:
                    continue

                # create the pattern that we want / is good
                yt_link_format = re.compile(r"^https?://(www\.)?youtube\.com/.*")
                # convert that pattern matching to bool
                # returns either True or False depending on output
                valid = bool(yt_link_format.match(url))

                # ouptut only the line number with bad URLs
                if valid == False:
                    print(f"{line_number + 1} --> {url} : {valid}")

    else:
        # input argument is NOT a file
        yt_link_format = re.compile(r"^https?://(www\.)?youtube\.com/.*")
        valid = bool(yt_link_format.match(input))

        # give appropriate ( messsage ) output depending on valid or not
        if valid == True:
            print_dashed_line()
            print("<-- Link Entered is Valid -->")
            print_dashed_line()

        elif valid == False:
            print_dashed_line()
            print("<-- Link Entered is NOT Valid... Exiting! -->\n")
            
            # exit the program
            exit(0)

        else:
            # if the `valid` becomes `None` for example
            print_dashed_line()
            print("<-- Something went wrong... Exiting -->\n")
            print_dashed_line()
            
            # exit the program
            exit(0)
```

In this function, we are passing in a **single** argument. This argument can either be a *text file* or a single YouTube *URL*.
Hence, we are going to use the `.isfile()` method to check if our input is a file.

### Input IS a File

If the *input* is a text file; we open the file for **read** ( *in this case the encoding is set to `utf-8`* ) and start iterating through the text file.

Normally, we do something simple as:

```python
with open(input, "r", encoding="utf-8") as txt_file:
	# read the contents of the file
	for line in txt_file:
		# do your things that we need to do!
		pass
```

Because us junior / beginner developers like to complicate shit up; we are going to instead do:

```python
with open(input, "r", encoding="utf-8") as txt_file:
	# start iterating through the text file
	for line_number, url in enumerate(txt_file):
		# do our shit here
		pass
```

As you can see from the variable name, we are going to also get the **line number**; "*why are we trying to get the line number?*". Because we are going to print out the **line number** of the URL(s) where you made a mistake!

>["Sometime my genius is almost frightening"](https://www.youtube.com/watch?v=R8vlNbk0Yww&t=13s)

We them simply take the each URL and strip any `\n` because we are in a text file and `\n` is simply the `<Return>` key!

We also added this simple yet really nice code:

```python
# skip any blank lines
if not url:
	continue
```

The above code is so simple that I don't want to explain it, but because we are Chads, we are going to explain this.

Fucking hell mate, it basically **skips** any blank lines ( *look at the fucking comment mate* )!

#### The Regular Expression Part

>[!CAUTION]
>This is the thing that I don't know about.
>Again, I suggest that you watch the video that I linked above.

```python
# create the pattern that we want / is good
yt_link_format = re.compile(r"^https?://(www\.)?youtube\.com/.*")
# convert that pattern matching to bool
# returns either True or False depending on output
valid = bool(yt_link_format.match(url))

# ouptut only the line number with bad URLs
if valid == False:
	print(f"{line_number + 1} --> {url} : {valid}")
```

This is a similar to `sed` but not really... For example, here is a little snippet code from my [kitty font script](https://github.com/Sunhaloo/dotfiles/blob/main/scripts/kitty_profile.sh)

```bash
sed -i 's/^font_family\s\+family="\(JetBrainsMono Nerd Font Mono\|CaskaydiaCove Nerd Font Mono\|FiraCode Nerd Font Mono\|MonaspiceKr Nerd Font Mono\|ShureTechMono Nerd Font Mono\|Liberation Mono\|BlexMono Nerd Font Mono\|CodeNewRoman Nerd Font Mono\)"/font_family      family="MonaspiceKr Nerd Font Mono"/' "$kitty_conf"
```

In this code, we are telling the script to change the font name **in place**. As you can see, we are have this:

```bash
's/^font_family\s\+family="\(JetBrainsMono Nerd Font Mono\|CaskaydiaCove Nerd Font Mono\|FiraCode Nerd Font Mono\|MonaspiceKr Nerd Font Mono\|ShureTechMono Nerd Font Mono\|Liberation Mono\|BlexMono Nerd Font Mono\|CodeNewRoman Nerd Font Mono\)
```

We are comparing / trying to find these "*keywords*" from the `kitty.conf` file to our input, i.e; find "*JetBrainsMono Nerd Font Mono*", "*CaskaydiaCove Nerd Font Mono*", "*Fira Nerd Font Mono*", "*MonaspicecKr Nerd Font Mono*", "*ShureTechMono Nerd Font Mono*", "*Liberation Mono*", "*BlexMono Nerd Font Mono*", "*CodeNewRoman Nerd Font Mono*" in the text file an change the font according to the user's choice.

In this case we don't need to perform an "*in-place*" change. But from what I have gathered with the help of [ChatGPT](https://chat.openai.com), we need to first try to *make* the **string** that we are trying to find / check. Hence, we get this variable:

```python
# create the pattern that we want / is good
yt_link_format = re.compile(r"^https?://(www\.)?youtube\.com/.*")
```

>Yes, as I have been saying and I am going to say again, I don't fucking know `re` and asked ChatGPT to make the the *expression* `^https?://(www\.)?youtube\.com/.*`.
>BTW the `r` before the `"` character means "*raw*"; like we know `\n` means caret return. Well with `r`, `\n` means ==> `\n`!

```python
# convert that pattern matching to bool
# returns either True or False depending on output
valid = bool(yt_link_format.match(url))
```

Simple enough, we are taking the URL ( *either single URL or in the text file* ) and returning a boolean value after we have `.match()` method.
We also have another method called `.search()` and I don't know the difference. I know that is you do something like:

```python
# this will NOT work BTW
valid = bool(yt_link_format.search(url))
```

I know that this will **not** work as we want.

After that, we simply do a little `if` statement to check whether our URL is valid or not.

>[!NOTE]
>I am not going to explain for the "*input is not a file*" because its the easier version of "*input is a file*".

---

# Audio - Video Downloader and Audio Format Converter

## Audio Downloader

As you know my back-end is not something like `pytube` or other. I am using [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [FFmpeg](https://ffmpeg.org/).
Where `yt-dlp` handles the YouTube downloads and `ffmpeg` converts `m4a` format into `mp3` or `wav` format.

### yt-dlp Usage

To download a **single** `m4a` audio format with `yt-dlp`, we need to run the command:

```bash
yt-dlp "https://www.youtube.com/watch?v=dQw4w9WgXcQ" --format m4a -o "/home/user/Desktop/downloaded_audio/%(title)s.%(ext)s"
```

But how do we run this command **from** Python? This was the main purpose of making this program. I wanted to learn this... "*How to run shell commands from a high-level enough programming language*".

Well, we have a module for that and its called the `subprocess` module which allow one to run shell commands inside of Python.

#### Downloading a Single YouTube Audio

Here is the command and command-execution for downloading a **single** video into `m4a` format

```python
# command to execute from Python in shell
yt_dlp_cmd = [
		"yt-dlp",
		yt_url,
		"--format", "m4a",
		"-o", output_song_name
	]

# run the command from Python to the Terminal / Shell
subprocess.run(yt_dlp_cmd)
```

Well, as you can see the variable `yt_dlp_cmd` is simply a **list** where we are passing each *word* of the command of type *string*. Then we simply apply the method `subprocess.run()` to that list where it will be executed.

Additionally, we the `output_song_name` is basically the path and the format of *output* that `yt-dlp` needs.

>I'll make you happy, here is the code!

```python
# variable to hold the output directory / path
output_path = os.path.expanduser("~/Desktop/downloaded_audio/")
# variable to hold the output "filename" for the downloaded songs
output_song_name = os.path.join(output_path + "%(title)s.%(ext)s")
```

#### Downloading Multiple YouTube Audio from File

>[!NOTE]
>One thing that I did not realise at the time for writing the first line of code was that `yt-dlp` already supports using links from a text file using the `-a` flag.
>I was so sad and disappointed that I nearly scraped the whole project.
>But then I realised something. I am doing this to learn and also to download songs from YouTube instead of using shitty online converters.
>I decided to **not** scrap this project and continue to work on so that I can have a "proper" ( *what is "proper" anyways* ) terminal user interface for downloading my songs.

In this list ( *or code if you wish* ), everything is the same except we now add the `-a` flag like I have been saying above.

```python
# command to execute from Python in shell
yt_dlp_cmd = [
		"yt-dlp",
		"-a", text_file,
		"--format",
		"m4a",
		"-o",
		output_song_name
	]

# run the command from Python to the Terminal
subprocess.run(yt_dlp_cmd)
```

## Video Downloader

### Downloading a Single Video

Similarly to our audio downloader, we are going to have the `output_path` and our `output_video_name`

```python
# variable to hold the output directory / path
output_path = os.path.expanduser("~/Desktop/downloaded_video/")
# variable to hold the output "filename" for the downloaded songs
output_video_name = os.path.join(output_path + "%(title)s.%(ext)s")
```

Hence, we are going to get the command and command-execution:

```python
# command to execute from Python in shell
yt_dlp_cmd = [
		"yt-dlp",
		"-f",
		f"bestvideo[ext={file_format}][height<=1080][fps<={actual_fps}]+bestaudio/best[ext={file_format}][height<=1080]",
		"--merge-output-format", file_format,
		"-o", output_video_name,
		yt_url
	]

# run the command from Python to the Terminal
subprocess.run(yt_dlp_cmd)
```

Well in this case, this seems a bit more complicated than the audio command.
Even though that this comes down to reading the YT-DLP documentation and basically sprinkle a bit of ChatGPT to correct your mistakes; I am still going to explain *myself* how I did this.

Well, in our Video Downloader, we allow the user to either download the video format in `mp4` or `webm`. To be honest, the program that I was trying to make only needed the "*audio downloader*" part. Again, I almost did not want to do this. But I guess I kept coding because of the adrenaline.

Yes, then after choosing the format, we are going to ask the user to enter the desired FPS which can either be 30 or 60. In addition, `yt-dlp` allows to use download in a variety of quality. But we want the highest quality ( *where the "highest quality" is going to be '1080p'* ) regardless of file size. Hence, we have this:

```bash
f"bestvideo[ext={file_format}][height<=1080][fps<={actual_fps}]+bestaudio/best[ext={file_format}][height<=1080]",
```

Here, we are saying to get the output at the format for `file_format` which, again, can either be `mp4` or `webm`. Now, if the video can do up to '4k', well stay on '1080p'. In addtion, get the best audio for that `file_format`.

During testing, even if you do use `webm`; it would still download the `mp4` format. Hence, we have this:

```bash
"--merge-output-format", file_format,
```

Where its going to merge the output to our desired output format.

### Downloading Multiple YouTube Video from File

Well, we just need to add our `-a` flag and provide the path to our text file and voila!

```python
# command to execute from Python in shell
yt_dlp_cmd = [
		"yt-dlp",
		"-a", text_file,
		"-f",
		f"bestvideo[ext={file_format}][height<=1080][fps<={actual_fps}]+bestaudio/best[ext={file_format}][height<=1080]",
		"--merge-output-format", file_format,
		"-o", output_video_name,
	]

# run the command from Python to the Terminal
subprocess.run(yt_dlp_cmd)
```

## Audio Format Converter

After **downloading** the `.m4a` file, we are going to use `ffmpeg` to convert it to either `mp3` or `wav` format. Now, when you convert something with `ffmpeg`, it will create **another** file with the same name but now with a different file extension.

Well, because we are good and honest people ( *wink wink* )... We are going to delete the **original** `.m4a` file so that we don't fill up the user's storage system.

>See, we are good people ( *wink wink* )!

### Iteration 1

Hence, I was thinking about doing something simple, as you know in the `os` module, we have the method `.listdir()` which list the current working directory. Therefore, I thought I could just do something like:

```python
# change to the working directory
os.chdir(os.path.expanduser("~/Desktop/downloaded_audio"))

# iterate through files
for input_song in os.listdir():
	# command to convert the audio ==> We are going to get the this later on
	
	# remove the input songs
	os.remove(input_song)
```


Well, this has a **MAJOR** problem, well you see, if you already have some downloaded and **already** converted audio. It will **also** *remove* these files.
This is due to the fact that I was using `os.listdir()` which "*globs*" everything in the directory even if the file has already been converted by `ffmpeg`.

Then I said to myself, there should be a way so that I can only take the `.m4a` file in *that* directory so that even if you run the program / function to convert to your desired audio format. The "*older*" files would still be intact.

>Well, I had no other option to search on the "search engine" called ChatGPT ( *wink wink* ).

### Iteration ChatGPT

>`glob glob`, at least I learned something new!
>But still I only know one method from that library

Here comes the `glob` module! The Chad Himself!

```python
# function to convert between audio formats
def convert_audio_format(directory_path: str, file_format: str, bitrate: str, codec: str):
    # change from the current working directory to where we downloaded the songs
    os.chdir(directory_path)

    # iterate through the whole directory / folder
    for input_song in glob.glob("*.m4a"):
        # out output "file" for the ffmpeg output flag
        output_song = os.path.splitext(input_song)[0]

        # create the ffmpeg command that will be run from Python
        ffmpeg_cmd = [
            "ffmpeg", 
            "-i", input_song, 
            "-vn", 
            "-acodec", codec, 
            "-ab", bitrate, 
            "-ar", "44100", 
            "-f", file_format,
            "-y",
            output_song
        ]

        # run the command from Python
        subprocess.run(ffmpeg_cmd)
        # clean the non-converted file ==> with `.m4a` extension
        os.remove(input_song)
```

>BTW this is the final solution for converting the audio files!

Similarly, we are changing the current working directory to `~/Desktop/downloaded_audio/` and then instead of using `os.listdir()`. We are going to use `glob.glob("*.m4a")`.

---

As you know in Unix / Linux based system ( *IDK if you can do this in CMD / Powershell* ), we have the `*` "*operator*"

Let's say that you have these files in the directory `~/Desktop/`

```console
file.txt
shit.txt
dickhead.sh
main.py
main.c
```

Now, how can we delete every text file `.txt` files in this directory, Well you can do something like

```bash
# list the current workind directory
ls
# after looking at the text files; remove them by typing the names of these files
rm file.txt shit.txt
```

A better way instead of typing all of this is to instead use the command:

```bash
# remove every text file from that directory
rm *.txt
```

After that, your `~/Desktop` directory will end up looking like this:

```console
dickhead.sh
main.py
main.c
```

>The `*` is similar to the one in SQL!

---

Therefore we know that `glob.glob("*.m4a")` will find all the file in *that* directory which only have an extension of `.m4a`!
Thus, we don't need to worry the method `os.remove(input_song)` as it will not remove any other converted songs as the variable `input_song` will only contains songs with the `.m4a` format.

>[!TIP] Success!

#### FFmpeg Command

```python
# create the ffmpeg command that will be run from Python
ffmpeg_cmd = [
	"ffmpeg", 
	"-i", input_song, 
	"-vn", 
	"-acodec", codec, 
	"-ab", bitrate, 
	"-ar", "44100", 
	"-f", file_format,
	"-y",
	output_song
]
```

Again, this comes down to the documentation which BTW I tried to read and got more confused!
I am not going to lie to you, I used ChatGPT to make the bash command so that I can convert the `.m4a` files to the desired format.

---

# Socials

- **Instagram**: https://www.instagram.com/s.sunhaloo
- **YouTube**: https://www.youtube.com/channel/UCMkQZsuW6eHMhdUObLPSpwg
- **GitHub**: https://www.github.com/Sunhaloo

---

S.Sunhaloo
Thank You!
