import re
import os
import glob
import subprocess


# function to display dashed lines
def print_dashed_line():
    print()
    print("-" * 50)
    print()


# function to create folders at required directory
# depending if downloading audio / video; will create folder with respective name
def create_folder(user_option: str):
    # check for the user's option
    if user_option == "audio":
        # meaning user wants to download audio
        dir_path = os.path.expanduser("~/Desktop/downloaded_audio")

        # check if the path exists
        if os.path.exists(dir_path):
            print("<-- Output Directory / Folder Already Exists! -->")
            print_dashed_line()

        else:
            print("<-- Creating Output Folder -->")
            print_dashed_line()
            # create the directory / folder
            os.mkdir(dir_path)

    if user_option == "audio_ordered":
        # meaning user wants to download audio
        dir_path = os.path.expanduser("~/Desktop/downloaded_audio_ordered")

        # check if the path exists
        if os.path.exists(dir_path):
            print("<-- Output Directory / Folder Already Exists! -->")
            print_dashed_line()

        else:
            print("<-- Creating Output Folder -->")
            print_dashed_line()
            # create the directory / folder
            os.mkdir(dir_path)

    if user_option == "video":
        # meaning user wants to download video
        dir_path = os.path.expanduser("~/Desktop/downloaded_video")

        # check if the path exists
        if os.path.exists(dir_path):
            print("<-- Output Directory / Folder Already Exists! -->")
            print_dashed_line()

        # if the directory / folder does not exists
        else:
            print("<-- Creating Output Folder -->")
            print_dashed_line()
            # create the directory / folder
            os.mkdir(dir_path)


# function to check if YouTube URL is valid
# WARNING: I am bad a pattern matching... Really Really Need to Learn This
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


# function to check for the file size
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


# function to validate file_format and bitrate for audio
def audio_file_bitrate_checker():
    # exception handling
    try:
        # prompt the user to enter file format + bitrate
        user_format = input("Please Select Between 'mp3' or 'wav': ")
        user_bitrate = int(input("Please Enter Bit Rate ( 100 - 2000 ): "))

        # evaluate the file format and codecs
        if user_format == "mp3":
            # to return the file format
            file_format = "mp3"
            # use the appropriate codec for mp3
            codec = "libmp3lame"

        elif user_format == "wav":
            # to return the file format
            file_format = "wav"
            # use the appropriate codec for wav
            codec = "pcm_s16le"

        elif user_format == "":
            # user wants to use default values
            print_dashed_line()
            print("<-- Using Default File Format -->")
            # use "default" file format
            file_format = "mp3"
            codec = "libmp3lame"

        else:
            # if the user enters something else
            print_dashed_line()
            print("<-- Invalid File Format Entered... Defaulting to MP3 -->")
            file_format = "mp3"
            codec = "libmp3lame"

        # perform check on bitrate
        if user_bitrate >= 100 and user_bitrate <= 2000:
            # everything is good... use user's bitrate
            actual_bitrate = str(user_bitrate) + "k"

            print_dashed_line()

        else:
            print_dashed_line()
            print("<-- Invalid Range For Bitrate... Defaulting to 192k -->")

            # change to "default" bitrate
            actual_bitrate = "192k"

            print_dashed_line()

        # return the file format, codec and bitrate to main program
        return file_format, codec, actual_bitrate

    # if the user does not enter integer values for bitrate
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please Enter Integer Value for Bitrate\n")
        return "mp3", "libmp3lame", "192k"


# function to validate file_format for vidoes
def video_file_fps_checker():
    # exception handling
    try:
        # prompt the user to enter file format + FPS
        user_format = input("Please Select Between 'mp4' or 'webm': ")
        user_fps = int(input("Please Select Between '60' or '30' FPS: "))

        # evaluate the file format and FPS
        if user_format == "mp4":
            # return the file format
            file_format = "mp4"

        elif user_format == "webm":
            # return the file format
            file_format = "webm"

        elif user_format == "":
            # user wants to use default values
            print_dashed_line()
            print("<-- Using Default File Format -->")
            # use "default" file format
            file_format = "mp4"

        else:
            # if the user enters something else
            print_dashed_line()
            print("<-- Invalid File Format Entered... Defaulting to MP4 -->")
            file_format = "mp4"

        # perform check on FPS
        if user_fps >= 30 and user_fps <= 60:
            # everything is good... use user's FPS
            actual_fps = str(user_fps)

            print_dashed_line()

        else:
            print_dashed_line()
            print("<-- Invalid Range For FPS... Defaulting to Max FPS -->")

            # change to "default" FPS
            actual_fps = "60"

            print_dashed_line()

        # return the file format, codec and bitrate to main program
        return file_format, actual_fps

    # if the user does not enter integer values for FPS
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please Enter Integer Value for Bitrate\n")
        return "mp4", "60"


# function to convert between audio formats
def convert_audio_format(
    directory_path: str, file_format: str, bitrate: str, codec: str
):
    # change from the current working directory to where we downloaded the songs
    os.chdir(directory_path)
    # iterate through the whole directory / folder
    for input_song in glob.glob("*.m4a"):
        # out output "file" for the ffmpeg output flag
        output_song = os.path.splitext(input_song)[0]

        # create the ffmpeg command that will be run from Python
        ffmpeg_cmd = [
            "ffmpeg",
            "-i",
            input_song,
            "-vn",
            "-acodec",
            codec,
            "-ab",
            bitrate,
            "-ar",
            "44100",
            "-f",
            file_format,
            "-y",
            output_song,
        ]

        # run the command from Python
        subprocess.run(ffmpeg_cmd)
        # clean the non-converted file ==> with `.m4a` extension
        os.remove(input_song)


# function to convert download YouTube videos into audio format ( in file name order )
def audio_downloader_name_order():
    try:
        # welcome screen for audio convert + display options
        print("==> Audio Converter Selected<==\n")
        print("Option [1]: Enter Single YouTube Video")
        print("Option [2]: Use List of URLs from a Text File ( File Name Order )")
        print("Option [3]: Exit")

        # prompt the user select an option
        user_option = input("\nPlease Select An Option: ")

        # evaluate the user's option
        if user_option == "1":
            # user wants to only convert 1 YouTube link / video
            print("\n<-- Converting A Single URL -->")
            print_dashed_line()

            # call the function to create the output directory / folder
            create_folder("audio")

            # variable to hold the output directory / path
            output_path = os.path.expanduser("~/Desktop/downloaded_audio/")
            # variable to hold the output "filename" for the downloaded songs
            output_song_name = os.path.join(output_path + "%(title)s.%(ext)s")

            # prompt the user to enter the YouTube URL
            yt_url = input("Please Enter YouTube URL to Convert: ")

            print_dashed_line()
            print("<-- Checking if URL Entered is Correct -->")

            # call the function to check if URL entered is valid
            check_yt_url(yt_url)

            print("<-- Starting Downloading Process -->\n\n")

            # command to execute from Python in shell
            yt_dlp_cmd = ["yt-dlp", yt_url, "--format", "m4a", "-o", output_song_name]

            # run the command from Python to the Terminal
            subprocess.run(yt_dlp_cmd)

            print_dashed_line()
            print("<-- Starting Conversion Process -->\n\n")

            # call the function to return the file format, codec and bitrate to main program
            file_format, current_codec, actual_bitrate = audio_file_bitrate_checker()

            print(f"<-- Converting to '{file_format}' -->\n\n")

            # call the function to convert to required audio format
            convert_audio_format(
                output_path, file_format, actual_bitrate, current_codec
            )

        elif user_option == "2":
            # user wants to convert YouTube links / videos with Text File
            print_dashed_line()
            print("<-- Converting URLs from Text File -->")
            print_dashed_line()

            # call the function to create the output directory
            create_folder("audio")

            # variable to hold the output directory / path
            output_path = os.path.expanduser("~/Desktop/downloaded_audio/")
            # directory / path for our input file
            text_file = os.path.expanduser("~/Desktop/yt_urls.txt")
            # variable to hold the output "filename" for the downloaded songs
            output_song_name = os.path.join(output_path + "%(title)s.%(ext)s")

            # verify if text file `yt_urls.txt` exists
            if os.path.isfile(text_file) and os.path.exists(text_file):
                # check for contents in the text file
                check_file_size(text_file)

                # call the function to check if URL entered is valid
                print("<-- Checking if URL Entered is Correct -->")
                print_dashed_line()
                check_yt_url(text_file)

                print("<-- Starting Downloading Process -->\n\n")

                # if everything is correct start the downloading process
                # command to execute from Python in shell
                yt_dlp_cmd = [
                    "yt-dlp",
                    "-a",
                    text_file,
                    "--format",
                    "m4a",
                    "-o",
                    output_song_name,
                ]

                # run the command from Python to the Terminal
                subprocess.run(yt_dlp_cmd)

                print_dashed_line()
                print("<-- Starting Conversion Process -->\n\n")

                # call the function to return the codec and bitrate to main program
                file_format, current_codec, actual_bitrate = (
                    audio_file_bitrate_checker()
                )

                print(f"<-- Converting to '{file_format}' -->\n\n")

                # call the function to convert to required audio format
                convert_audio_format(
                    output_path, file_format, actual_bitrate, current_codec
                )

            else:
                # user does not have 'yt_urls.txt' file present at `~/Desktop`
                print_dashed_line()
                print("<-- You have no 'yt_urls.txt' File at Desktop Directory!!! -->")
                print_dashed_line()

        elif user_option == "3":
            # user wants to exit program
            print_dashed_line()
            print("Good Bye!")
            print_dashed_line()
            # exit without errors
            exit(0)

        # if user does not select the right option
        else:
            print_dashed_line()
            print("<-- Wrong Option -->")
            print_dashed_line()

    # if the user does not enter integer data for bitrate
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please Enter Integer Data for Bitrate\n")


# function to convert download YouTube videos into audio format ( in sequential order )
def audio_downloader_seq_order():
    # welcome screen for audio convert + display options
    print("==> Audio Converter Selected ( Name Order ) <==")
    print_dashed_line()

    # call the function to create the output directory
    create_folder("audio_ordered")

    # variable to hold the output directory / path
    output_path = os.path.expanduser("~/Desktop/downloaded_audio_ordered/")
    # directory / path for our input file
    text_file = os.path.expanduser("~/Desktop/yt_urls.txt")

    # verify if text file `yt_urls.txt` exists
    if os.path.isfile(text_file) and os.path.exists(text_file):
        # check for contents in the text file
        check_file_size(text_file)

        # user wants to convert YouTube links / videos with Text File
        print("<-- Converting URLs from Text File -->")
        print_dashed_line()

        # call the function to check if URL entered is valid
        print("<-- Checking if URL Entered is Correct -->")
        print_dashed_line()
        check_yt_url(text_file)

        print("<-- Starting Downloading Process -->\n\n")

        # variable that will increment with each download
        prefix_num = 1

        # open the `yt_urls.txt` file for read
        with open(text_file, "r") as yt_txt_file:
            # iterate through each line
            for urls in yt_txt_file:
                # remove the 'return' character
                yt_url = urls.strip()

                # skip any blank lines
                if not yt_url:
                    continue

                # variable to hold the output "filename" for the downloaded songs
                output_song_name = os.path.join(
                    output_path + f"{prefix_num}. " + "%(title)s.%(ext)s"
                )

                # if everything is correct start the downloading process
                # command to execute from Python in shell
                yt_dlp_cmd = [
                    "yt-dlp",
                    yt_url,
                    "--format",
                    "m4a",
                    "-o",
                    output_song_name,
                ]

                # run the command from Python to the Terminal
                subprocess.run(yt_dlp_cmd)

                # increase the variable `prefix_num` by 1
                prefix_num += 1

        print_dashed_line()
        print("<-- Starting Conversion Process -->\n\n")

        # call the function to return the codec and bitrate to main program
        file_format, current_codec, actual_bitrate = audio_file_bitrate_checker()

        print(f"<-- Converting to '{file_format}' -->\n\n")

        # call the function to convert to required audio format
        convert_audio_format(output_path, file_format, actual_bitrate, current_codec)
    else:
        # user does not have 'yt_urls.txt' file present at `~/Desktop`
        print_dashed_line()
        print("<-- You have no 'yt_urls.txt' File at Desktop Directory!!! -->")
        print_dashed_line()


# function to download YouTube videos
def video_downloader():
    try:
        # welcome screen for audio convert + display options
        print("==> YouTube Video Downloader Selected <==\n")
        print("Option [1]: Enter Single YouTube Video")
        print("Option [2]: Use List of URLs from a Text File")
        print("Option [3]: Exit")

        # prompt the user select an option
        user_option = input("\nPlease Select An Option: ")

        # evaluate the user's option
        if user_option == "1":
            # user wants to only convert 1 YouTube link / video
            print("\n<-- Converting A Single URL -->")
            print_dashed_line()

            # call the function to create the output directory / folder
            create_folder("video")

            # variable to hold the output directory / path
            output_path = os.path.expanduser("~/Desktop/downloaded_video/")
            # variable to hold the output "filename" for the downloaded songs
            output_video_name = os.path.join(output_path + "%(title)s.%(ext)s")

            # prompt the user to enter the YouTube URL
            yt_url = input("Please Enter YouTube URL to Convert: ")

            print_dashed_line()
            print("<-- Checking if URL Entered is Correct -->")

            # call the function to check if URL entered is valid
            check_yt_url(yt_url)

            # call the function to return the file format + fps to the main program
            file_format, actual_fps = video_file_fps_checker()

            print(
                f"<-- Starting Downloading Process ( {file_format} | {actual_fps} ) -->\n\n"
            )

            # command to execute from Python in shell
            yt_dlp_cmd = [
                "yt-dlp",
                "-f",
                f"bestvideo[ext={file_format}][height<=1080][fps<={actual_fps}]+bestaudio/best[ext={file_format}][height<=1080]",
                "--merge-output-format",
                file_format,
                "-o",
                output_video_name,
                yt_url,
            ]

            # run the command from Python to the Terminal
            subprocess.run(yt_dlp_cmd)

        elif user_option == "2":
            # user wants to convert YouTube links / videos with Text File
            print_dashed_line()
            print("<-- Converting URLs from Text File -->")
            print_dashed_line()

            # call the function to create the output directory
            create_folder("video")

            # variable to hold the output directory / path
            output_path = os.path.expanduser("~/Desktop/downloaded_video/")
            # variable to hold the output "filename" for the downloaded songs
            output_video_name = os.path.join(output_path + "%(title)s.%(ext)s")
            # directory / path for our input file
            text_file = os.path.expanduser("~/Desktop/yt_urls.txt")

            # verify if text file `yt_urls.txt` exists
            if os.path.isfile(text_file) and os.path.exists(text_file):
                # check for contents in the text file
                check_file_size(text_file)

                # call the function to check if URL entered is valid
                print("<-- Checking if URL Entered is Correct -->")
                print_dashed_line()
                check_yt_url(text_file)

                # call the function to return the file format + fps
                file_format, actual_fps = video_file_fps_checker()

                print(
                    f"<-- Starting Downloading Process ( {file_format} | {actual_fps} ) -->\n\n"
                )

                # command to execute from Python in shell
                yt_dlp_cmd = [
                    "yt-dlp",
                    "-a",
                    text_file,
                    "-f",
                    f"bestvideo[ext={file_format}][height<=1080][fps<={actual_fps}]+bestaudio/best[ext={file_format}][height<=1080]",
                    "--merge-output-format",
                    file_format,
                    "-o",
                    output_video_name,
                ]

                # run the command from Python to the Terminal
                subprocess.run(yt_dlp_cmd)

        elif user_option == "3":
            # user wants to exit program
            print_dashed_line()
            print("Good Bye!")
            print_dashed_line()
            # exit without errors
            exit(0)

    # if the user does not enter integer data for bitrate
    except ValueError as e:
        print(f"\nError: {e}")
        print("Please Enter Integer Data for Bitrate\n")


# function to display options to user
def display_options():
    # main welcome screen and display options to user
    print("\nYouTube Video Downloader and Converter\n")
    print("Option [1]: Download Audio")
    print("Option [2]: Download Audio ( Text File Only ==> Ordered by Number )")
    print("Option [3]: Download Video")
    print("Option [4]: Exit")
    print_dashed_line()


# function to evaluate the user's choice
def evaluate_choice(user_choice: str):
    # conditions to evaluate based on user's choice
    if user_choice == "1":
        # user wants to download in audio format ( in random order )
        audio_downloader_name_order()

    if user_choice == "2":
        # user wants to download in audio format ( in sequential order )
        audio_downloader_seq_order()

    elif user_choice == "3":
        # user wants to download in video format
        video_downloader()

    elif user_choice == "4":
        # user is closing the program
        print_dashed_line()
        print("Good Bye!")
        print_dashed_line()
        exit(0)

    # if user does not select something appropriate
    else:
        print_dashed_line()
        print("Wrong Option")
        print_dashed_line()


# our main function
def main():
    # call function to display options to user
    display_options()

    # ask the user to enter his choice
    user_option = input("Please Select an Option: ")

    print_dashed_line()

    # call the function to evaluate the user's choice
    evaluate_choice(user_option)


# source the main function
if __name__ == "__main__":
    main()
