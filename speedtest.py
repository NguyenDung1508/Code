import tkinter as tk
import speedtest as s
import threading as th

def run():
    check_button.config(text="Loading...")
    check_button.config(state=tk.DISABLED)

    def test():
        speedtester = s.Speedtest()
        speedtester.get_best_server()
        
        download_speed = speedtester.download() / 1024 / 1024
        upload_speed = speedtester.upload() / 1024 / 1024

        download_speed_label.config(text=str(download_speed) + " Mbps")
        upload_speed_label.config(text=str(upload_speed) + " Mbps")
        
        check_button.config(state=tk.NORMAL)
        check_button.config(text="Run Speedtest")

    thread = th.Thread(target=test)
    thread.start()



root = tk.Tk()
root.title( "Speedtest" )
root.config(bg = "white" )
root.geometry( "400x450" )

frame = tk.Frame(root, bg = 'white')
frame.pack(padx= 50, pady= 100)

download_label = tk.Label(frame, text = "Download speed", font = ('gabriola', 12), bg = 'white', fg = 'black', height= 1, width= 40, highlightthickness = 1)
download_label.pack(pady = 7)

download_speed_label = tk.Label(frame, text = "0 Mbps", font = ('gabriola', 12), bg = 'white', fg = 'black', height= 1, width= 40, highlightthickness = 1)
download_speed_label.pack(pady = 7)

upload_label = tk.Label(frame, text = "Upload speed", font = ('gabriola', 12), bg = 'white', fg = 'black', height= 1, width= 40, highlightthickness = 1)
upload_label.pack(pady = 7)

upload_speed_label = tk.Label(frame, text = "0 Mbps", font = ('gabriola', 12), bg = 'white', fg = 'black', height= 1, width= 40, highlightthickness = 1)
upload_speed_label.pack(pady = 7)

check_button = tk.Button(frame, command = run,text = "Run Speedtest", font = ('gabriola', 12), bg = 'white', fg = 'black', height= 1, width= 40, highlightthickness = 1)
check_button.pack(pady=7)




root.mainloop()
