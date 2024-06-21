from datetime import datetime, time
import pytz

from repository import bot, aviasales_manager

async def send_tickets():
    dates = [
        ["2024-07-29", "2024-08-01"],
        ["2024-07-30", "2024-08-02"],
        ["2024-07-31", "2024-08-03"],
        ["2024-08-01", "2024-08-04"]
    ]
    tickets_info = []
    for date in dates:
        tickets_info.extend(aviasales_manager.get_tickets_for_dates(
            origin="KGD", destination="LED",
            departure_at=date[0], return_at=date[1]
        ))

    sorted(tickets_info,key=lambda x: x.price)
    tickets_info_str = map(str, tickets_info[:5])
    is_with_notification = is_now_work_hours()
    print(is_with_notification)
    #print("\n".join(tickets_info_str))
    await bot.send_message(292667494, "\n---\n".join(tickets_info_str), parse_mode="Markdown",
                           disable_web_page_preview=True, disable_notification=not is_with_notification)

def is_now_work_hours():
    timezone = pytz.timezone('Europe/Amsterdam')
    current_time = datetime.now(timezone).time()

    # Определяем рабочие часы
    start_time = time(9, 0, 0)
    end_time = time(21, 0, 0)

    # Проверяем, находится ли текущее время в рабочем интервале
    return start_time <= current_time <= end_time