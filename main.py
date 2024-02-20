from pytube import YouTube

link = input('Cole o link: ')

youtube_var = YouTube(link)

youtube_var.streams.filter(progressive=True, file_extension='mp4').first().download()

print('Donloawded', link)