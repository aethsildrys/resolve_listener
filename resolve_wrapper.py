import time, subprocess
from datetime import datetime
# importing config.py file (gitignore)
from config import file_dest, process
def main():
    # open davinci resolve studio
    resolve = subprocess.Popen([process])

    # write time to variables
    date = datetime.now().strftime("%d/%m/%Y")
    # +3600sec beacuse my timezone is UTC+1
    launch_time = time.time() + 3600
    launch_time_hours = launch_time // 3600 % 24
    launch_time_minutes = launch_time // 60 % 60
    launch_time_seconds = launch_time % 60

    # when resolve was closed write time to second variable
    resolve.wait()
    if resolve.returncode == 0:
        # +3600sec beacuse my timezone is UTC+1
        end_time = time.time() + 3600
        end_time_hours = end_time // 3600 % 24
        end_time_minutes = end_time // 60 % 60
        end_time_seconds = end_time % 60

        # calculate time
        calculated_time = end_time - launch_time
        calculated_time_days = calculated_time // 86400
        calculated_time_hours = calculated_time // 3600 % 24
        calculated_time_minutes = calculated_time // 60 % 60
        calculated_time_seconds = calculated_time % 60

        # write time and date to file
        with open(file_dest, 'a') as f:
            f.write(f'DATE: {date}\n'
                    f'Start time: {int(launch_time_hours)}:{int(launch_time_minutes)}:{int(launch_time_seconds)}\n'
                    f'End time: {int(end_time_hours)}:{int(end_time_minutes)}:{int(end_time_seconds)}\n'
                    f'Resolve was opened for: {int(calculated_time_days)} day(s), {int(calculated_time_hours)} hour(s), '
                    f'{int(calculated_time_minutes)} minute(s), {int(calculated_time_seconds)} second(s)\n\n')
    else:
        print(f"Exit code: {resolve.returncode}")
if __name__ == "__main__":
    main()