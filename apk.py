import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog
from pytubefix import YouTube
from pytubefix.cli import on_progress

### functions - do samething ###
def choose_video():
    if ch_string.get() == 'single':
        single_entry['state'] = 'normal'
        multiple_entry['state'] == 'disabled'
    else:
        single_entry['state'] = 'disabled'
        multiple_entry['state'] = 'normal'

def choose_folder():
    filename = filedialog.askdirectory(initialdir='/')
    save_string.set(value=filename)
    button['state'] = 'normal'

def download_video_button():
    urls = []
    resolution = res_string.get()
    save_location =save_string.get()
    single_url = url_string.get()
    if single_url != '':
        urls.append(single_url)
    else:
        multi_url = multiple_entry.get(1.0, 'end').split(',')
        urls = [
            url.strip() for url in multi_url
        ]
   #print(urls, resolution, save_location)
    download_video(urls, resolution, save_location)

def download_video(urls, resolution, save_location):
    try:
        for url in urls:
            yt = YouTube(url, on_progress_callback=on_progress)
            print(yt.title)
            if resolution == 'low' :
                res_streams = yt.streams.get_lowest_resolution()
            else:
                res_streams = yt.streams.get_highest_resolution()
            res_streams.download(output_path=save_location)
            print("vidio sukses di download! ")
    except Exception as e:
        print(e)

### windows ###
window = ttk.Window(themename='journal')
window.title("YouTube Downloader")
window.minsize(550, 700)

### variable ###
ch_string = tk.StringVar()
url_string = tk.StringVar()
res_string = tk.StringVar()
save_string = tk.StringVar()

### widgets ###
# Header
header_label = ttk.Label(master=window, text='Youtube Video Downloader', font=('verdana', 30, 'bold'), bootstyle='primary')





# choose single vidoe or multiple videos
frame = ttk.Frame(master=window)
ch_radio_single = ttk.Radiobutton(master=frame,text='Single Video', bootstyle='success', value='single' , 
                    variable=ch_string, command=choose_video)
ch_radio_bulk = ttk.Radiobutton(master=frame, text='Multiple Videos', bootstyle='success', value='multiple' , 
                     variable=ch_string, command=choose_video)

# Enter Single Video URL
single_entry_label = ttk.Label(master=window, text='Enter Video URL')
single_entry = ttk.Entry(master=window, bootstyle='success', textvariable=url_string, width=40, state='disabled')

# choose Resolution
frame2 = ttk.Frame(master=window)
high_radio =ttk.Radiobutton(master=frame2 ,text='high resolution', bootstyle='success', value='high ' , 
                    variable=res_string)
low_radio  = ttk.Radiobutton(master=frame2,text='low resolution ', bootstyle='success', value='low',
                     variable=res_string)


# Enter Multiple Video URL
multiple_entry_label = ttk.Label(master=window, text='Enter Video URLs (separated by comma)')
multiple_entry = ttk.Text(master=window, width=40, height=15, state='disabled')

# Select the Folder
save_label = ttk.Label(master=window, text='Select the Folder to save the vidio ')
frame3 = ttk.Frame(master=window)
save_entry = ttk.Entry(master=frame3, bootstyle='success', textvariable=save_string)
save_button = ttk.Button(master=frame3,bootstyle='success-outline', text='select folder', command=choose_folder)

# Download Button
button = ttk.Button(master=window, bootstyle='success-outline', text='Download', state='disabled' , command=download_video_button)

### layout ###
header_label.pack(padx=(20,20), pady=(20,20))
frame.pack(padx=(0,20))
ch_radio_single.pack(side='left', padx=(0,20))
ch_radio_bulk.pack()
single_entry_label.pack()
single_entry.pack(padx=(0,20))
multiple_entry_label.pack()
multiple_entry.pack(padx=(0,20))
frame2.pack(padx=(0,20))
high_radio.pack(side='left', padx=(0,20))
low_radio.pack()
save_label.pack()
frame3.pack(padx=(0,20))
save_entry.pack(side='left', padx=(0,20))
save_button.pack()
button.pack(pady=(20,20))


### run ###
window.mainloop() 