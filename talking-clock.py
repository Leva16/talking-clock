import os

from datetime import datetime
from mpg123 import Mpg123, Out123
from apscheduler.schedulers.blocking import BlockingScheduler


def timetalk():
    hour = datetime.now().strftime("%-I")
    mp3 = Mpg123("resourses/" + hour + ".mp3")
    out = Out123()
    for frame in mp3.iter_frames(out.start):
        out.play(frame)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_executor('processpool')
    scheduler.add_job(timetalk, 'cron', minute=0)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
