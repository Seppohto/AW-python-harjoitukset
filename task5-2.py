from crontab import CronTab

cron = CronTab(user='olli')

job1 = cron.new(command='python task5.py')

job1.minute.every(1)

cron.write()