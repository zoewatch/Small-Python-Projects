import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on")
while(break_count < total_breaks):
      time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=j_XvqwnGDko")
    break_count = break_count + 1
