import os
import threading
import math
import subprocess
from queue import Queue

share_q = Queue()

# cmd = 'youtube-dl --proxy socks5://127.0.0.1:10808 -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" --playlist-start 1 --playlist-end 3 -c -o "F:/YoutubeDownload/%(title)s.%(ext)s" https://www.youtube.com/playlist?list=PLJV_el3uVTsO07RpBYFsXg-bN5Lu0nhdG'
# COMMAND = r'youtube-dl -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" --playlist-start {begin} \
#   --playlist-end {end} -c -o "{download_dir}%(title)s.%(ext)s" {youtube_url}'


def Download(cmd):
    os.system(cmd)


def CreateQueue(b, e, d_dir, url, thread_count=5):
    # COMMAND = 'youtube-dl --proxy socks5://127.0.0.1:10808 -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" --playlist-start {begin} --playlist-end {end} -c -o "{download_dir}/%(title)s.%(ext)s" {youtube_url}'.format(begin=b, end=e, download_dir=d_dir, youtube_url=url)
    # print("Command: ", COMMAND)

    global share_q

    list_count = e - b + 1
    every_step = (list_count // thread_count) if (list_count % thread_count == 0) else (list_count // thread_count + 1)
    recursives = math.ceil(list_count/every_step)

    step_count = []
    
    s = b
    t = s + every_step - 1

    for i in range(recursives):
        if i == recursives - 1:
            if b == e or recursives == 1:
                step_count.append([b, e])
            else:
                step_count.append([t+1, e])
        else:
            s = b+i*every_step
            t = s+every_step - 1
            step_count.append([s, t])

    # print(b, e, list_count, thread_count, every_step, recursives)
    # print(step_count)

    for step_b, step_e in step_count:
        COMMAND = 'youtube-dl -i --proxy socks5://127.0.0.1:10808 -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" --playlist-start {begin} --playlist-end {end} -c -o "{download_dir}/%(title)s.%(ext)s" {youtube_url}'.format(begin=step_b, end=step_e, download_dir=d_dir, youtube_url=url)
        # COMMAND = 'youtube-dl -i -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" --playlist-start {begin} --playlist-end {end} -c -o "{download_dir}/%(title)s.%(ext)s" {youtube_url}'.format(begin=step_b, end=step_e, download_dir=d_dir, youtube_url=url)
        share_q.put(COMMAND)

    return recursives


if __name__ == '__main__':
    actual_thread_count = CreateQueue(
        b=1, 
        e=32,
        d_dir="F:/YoutubeDownload",
        url='https://www.youtube.com/playlist?list=PLJV_el3uVTsO07RpBYFsXg-bN5Lu0nhdG',
        thread_count=1)

    thread_list = []
    while not share_q.empty():
        cmd = share_q.get()
        t = threading.Thread(target=Download, args=(cmd, ))
        thread_list.append(t)

    for thread in thread_list:
        thread.setDaemon(True)
        thread.start()

    for thread in thread_list:
        thread.join()
