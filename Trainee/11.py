"""
Сгенерируйте рандомное число при помощи модуля рандом:
import random

random_number = random.randint(1, 10)

При помощи модуля time засеките время ожидания программы и выведите его в консоль

start_time = <ваш код здесь>
"усыпите" выполнение программы на <random_number> секунд
end_time = <ваш код здесь>
"""

from datetime import datetime
import time
import random

random_number = random.randint(1, 10)

start_time = datetime.now()
time.sleep(random_number)
end_time = datetime.now() - start_time

print(end_time)
