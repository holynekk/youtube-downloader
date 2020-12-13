from pytube import YouTube


while(True):
    yt_link = input("Enter the video link: ")

    yt_obj = YouTube(yt_link)

    # Title of the video
    print("Title: ", yt_obj.title)

    # View count of the video
    print("View count: ", yt_obj.views)

    # Length of the video
    print("Length: ", yt_obj.length)

    print("Is this the video that you want to download?[y/n]: ",end="")
    print("'q' for quit.")
    yes_no = input()

    if(yes_no in 'qqqQQQ'):
        print("Ok then, see ya!")
        break

    if(yes_no):

        ys = yt_obj.streams.get_highest_resolution()

        print("Donwloading...")
        ys.download("./Videos")
        print("Download completed.")

        print("want to continue?[y/n]: ")
        tr = input()
        if(tr == 'n'):
            break
    else:
        print("The link is wrong, Somebody jebaited you!")