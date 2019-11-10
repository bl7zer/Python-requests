from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import vk_api
from random import randint

def main_VkBot():
    try:
        vk = vk_api.VkApi(token="token вашей группы")
        vk._auth_token()
        vk.get_api()
        longpoll = VkBotLongPoll(vk, "id вашей группы"(Как число, не строка))
        
        help_set = {"help", "помощь", "команды", "начать"}
        #Сообщение с функциями бота
        def help():
            helpcommands = "Команды: (+команды вашего бота)"
            vk.method('messages.send', {
                "peer_id": event.object.peer_id,
                "message": helpcommands,
                "random_id": 0
            })
    
        #Кидает рандомное видео с группы
        def random_video():
            #Минус этого способа, бот может скинуть удаленное видео
            rndm_video = "video-" + str("id группы") + "_" + str(randint(456240000, 456245443))
            vk.method('messages.send', {
                "peer_id": event.object.peer_id,
                "attachment": rndm_video,
                "random_id": 0
            })
        #Кидает документ с заданным критерием поиска
        def random_doc():
            q = event.object.text.split()[1:]
            search = vk.method('docs.search', {
                "q": q,
                "search_own": 0,
                "count": "999",
                })
            count = 999
            if count > search['count']:
                count = search['count']
            if count == 0:
                vk.method('messages.send', {
                    "peer_id": event.object.peer_id,
                    "message": "Ничего не найдено",
                    "random_id": 0
                })
            else:
                r_count = randint(0, count - 1)
                doc = search['items'][r_count]['url']
                quer = doc.index("?")
                doc = doc[15:quer]
                vk.method('messages.send', {
                    "peer_id": event.object.peer_id,
                    "attachment": doc,
                    "random_id": 0
                })]
        #Рандомный пост
        def godnotent_post():
            try:
                vk = vk_api.VkApi(token="Токен вашего приложения(НЕ ГРУППЫ)")
                vk._auth_token()
                wall = vk.method('wall.get', {
                        "owner_id": -109125388,
                        #Кол-во возвращаемых постов
                        "count": 100,
                        #offset - смещение поиска
                        "offset": randint(0, 1000),
                    })
                write = wall['items'][randint(1, 99)]
                text = write['text']
                attachment = ""
                #Считывает вложения
                for i in range(len(write['attachments'])):
                    attachment_type = write['attachments'][i]['type']
                    attchmnt = write['attachments'][i][attachment_type]
                    attachment += attachment_type + str(attchmnt['owner_id']) + "_" + str(attchmnt['id']) + ','
                vk = vk_api.VkApi(token="token вашей группы")
                vk._auth_token()
                vk.method('messages.send', {
                    "peer_id": event.object.peer_id,
                    "message": text,
                    "attachment": attachment,
                    "random_id": 0
                })
            #Если в посте нет вложений
            except KeyError:
                vk = vk_api.VkApi(token="token вашей группы")
                vk._auth_token()
                vk.method('messages.send', {
                    "peer_id": event.object.peer_id,
                    "message": text,
                    "random_id": 0
                })
        while True:
            for event in longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW:
                    if event.object.text.lower() in help_set:
                        help()
                    elif event.object.text.lower() == "random video":
                        random_video()
                    elif event.object.text.lower().startswith("random_doc"):
                        random_doc()
                    elif "прикол" in event.object.text.lower():
                        godnotent()
    except Exception as e:
        vk.method('messages.send', {
            "peer_id": "Id пользователя для сообщения об ошибке",
            "message": ("Fuck something went wrong: " + str(e)),
            "random_id": 0
        })
        main_VkBot()

main_VkBot()
