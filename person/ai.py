from openai import OpenAI
from . import models
import httpx

client = httpx.Client(proxy='http://anu3yl5fmt-corp.mobile.res-country-US-hold-session-session-673336dc98054:IZGLt6XaW30dPdhW@93.190.139.6:9999')

client = OpenAI(
  api_key="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",
    http_client=client,
)

def generate(data: models.Person):
    TEXT = f"""
Ты - профессиональный копирайтер, твоя задача исправить, структурировать и сделать биографию более красивой. Пиши в художественном стиле.

НЕЛЬЗЯ ЧТО-ТО ВЫДУМЫВАТЬ, БИОГРАФИЯ ДОЛЖНА БЫТЬ МАКСИМАЛЬНО ПРАВДИВАЯ, ПО ДАННЫМ КОТОРЫМ Я ДАЛ

Длина +- 1000 символов (МОЖНО писать меньше если информации мало, главное не выдумывай)

Пиши сплошным текстом, не используй маркдаун

Вот информация которая у меня есть:
ФИО: {data.last_name} {data.first_name} {data.middle_name}
Даты: {data.date_of_birth} - {data.date_of_death}
Участник: {data.armed_conflict.title}
Награды: {[medal.title for medal in data.medals.all()]}
Наименование военного комиссариата: {data.military_commissariat}
Воинское звание: {data.military_rank}
Место рождения: {data.place_of_birth}
Место захоронения: {data.burial_place}
Биография: {data.biography}
    """

    completion = client.chat.completions.create(
      model="gpt-4o-mini",
      store=True,
      messages=[
        {"role": "user", "content": TEXT}
      ]
    )

    return completion.choices[0].message.content

if __name__ == '__main__':
    for user in models.Person.objects.all():
        print(user)
