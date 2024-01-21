from django_cron import CronJobBase, Schedule
from apps.transactions.models import Transactions
from datetime import timedelta

class CoinCronJob(CronJobBase):
    RUN_EVERY_DAYS = 30  
    schedule = Schedule(run_every_days=RUN_EVERY_DAYS)
    code = 'coins.CoinCronJob' 

    def do(self):  
        user_coins_list = Transactions.objects.all()
        for user_coins in user_coins_list:
            user_coins.balance -= 4  
            user_coins.save()

    
    