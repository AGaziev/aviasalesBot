from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from .ticket_sender import send_tickets


def register_senders(scheduler: AsyncIOScheduler):
    ticket_sender_interval = IntervalTrigger(hours=1)
    scheduler.add_job(send_tickets, ticket_sender_interval)