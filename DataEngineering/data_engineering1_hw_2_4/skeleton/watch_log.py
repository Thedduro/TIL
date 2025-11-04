import time

log_path = "/log/app.log"

with open(log_path, "r") as f:
    f.seek(0, 2)  # EOF로 이동
    while True:
        line = f.readline()
        if line:
            print("[LOG] " + line.strip())
        else:
            time.sleep(1) 