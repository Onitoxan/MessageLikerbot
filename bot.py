import json
import requests
import time

TOKEN = '861342303:AAHePPsFMoTZqoUb-Hq27TFCgLhwC-H1Jag'
FATHER_CHAT_ID = 610513796
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
EMOJI_CORAZON = "\u2764\ufe0f"
EMOJI_STOP = "\u26d4\ufe0f"
with open("./MsgLikerbotDB.json", encoding="utf-8") as f:  # AÑADIR BASE DE DATO, AQUI SOLO SE ABRE.
    database = json.load(f)

print(database)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    try:
        for update in updates.get("result", Exception):
            update_ids.append(int(update["update_id"]))
        return max(update_ids)
    except Exception as e:
        send_message("Error en el metodo get_last_update_id: " + str(e), FATHER_CHAT_ID)


def like_dislike(updates):
    for update in updates.get("result", Exception):
        try:
            bool_check_reply_to_message = update.get("message").get("reply_to_message")
            text = update.get("message", Exception).get("text", Exception)
            message_id = update.get("message", Exception).get("message_id", Exception)
            chat = update.get("message", Exception).get("chat", Exception).get("id", Exception)

            if text.strip() == "/like" or text.strip() == "/like@MsgLikebot" and "reply_to_message" in update.get(
                    "message"):
                user = update["message"]["from"]["first_name"]
                replied_user = update["message"]["reply_to_message"]["from"]["first_name"]
                replied_text_message_id = update["message"]["reply_to_message"].get("message_id")

                if "photo" in bool_check_reply_to_message:
                    reply_to_message("{}️A {} le ha gustado esta foto{}️".format(EMOJI_CORAZON, user, EMOJI_CORAZON),
                                     chat, replied_text_message_id,
                                     message_id)
                elif "sticker" in bool_check_reply_to_message:
                    reply_to_message("{}A {} le ha gustado este Sticker{}".format(EMOJI_CORAZON, user, EMOJI_CORAZON),
                                     chat, replied_text_message_id,
                                     message_id)
                elif "video" in bool_check_reply_to_message:
                    reply_to_message("{}A {} le ha gustado este video{}️".format(EMOJI_CORAZON, user, EMOJI_CORAZON),
                                     chat, replied_text_message_id,
                                     message_id)
                elif "audio" in bool_check_reply_to_message:
                    reply_to_message(
                        "{}️A {} le ha gustado esta pista de audio{}️".format(EMOJI_CORAZON, user, EMOJI_CORAZON), chat,
                        replied_text_message_id, message_id)
                elif "animation" in bool_check_reply_to_message:
                    reply_to_message("{}️A {} le ha gustado este GIF{}️".format(EMOJI_CORAZON, user, EMOJI_CORAZON),
                                     chat, replied_text_message_id,
                                     message_id)
                elif "voice" in bool_check_reply_to_message:
                    reply_to_message("{}A {} le ha gustado este audio{}️".format(EMOJI_CORAZON, user, EMOJI_CORAZON),
                                     chat, replied_text_message_id,
                                     message_id)
                elif "voice_note" in bool_check_reply_to_message:
                    reply_to_message(
                        "{}A {} le ha gustado este videomensaje{}️".format(EMOJI_CORAZON, user, EMOJI_CORAZON), chat,
                        replied_text_message_id,
                        message_id)
                elif "document" in bool_check_reply_to_message:
                    reply_to_message("{}A {} le ha gustado este documento{}".format(EMOJI_CORAZON, user, EMOJI_CORAZON),
                                     chat, replied_text_message_id,
                                     message_id)
                elif "contact" in bool_check_reply_to_message:
                    reply_to_message("{}A {} le ha gustado este contacto{}️".format(EMOJI_CORAZON, user, EMOJI_CORAZON),
                                     chat, replied_text_message_id,
                                     message_id)
                elif "text" not in bool_check_reply_to_message:
                    reply_to_message("{}A {} le ha gustado esta encuesta{}️".format(EMOJI_CORAZON, user, EMOJI_CORAZON),
                                     chat, replied_text_message_id,
                                     message_id)
                else:
                    replied_text = update["message"]["reply_to_message"]["text"]
                    send_message(
                        "{}{} le ha dado me gusta al mensaje de {}{}: '{}'".format(EMOJI_CORAZON, user, replied_user,
                                                                                   EMOJI_CORAZON, replied_text),
                        chat, message_id)

            elif text.strip() == "/dislike" or text.strip() == "/dislike@MsgLikebot" and "reply_to_message" \
                    in update.get("message"):
                user = update["message"]["from"]["first_name"]
                replied_user = update["message"]["reply_to_message"]["from"]["first_name"]
                replied_text_message_id = update["message"]["reply_to_message"].get("message_id")

                if "photo" in bool_check_reply_to_message:
                    reply_to_message("{}️A {} no le ha gustado esta foto{}️".format(EMOJI_STOP, user, EMOJI_STOP), chat,
                                     replied_text_message_id,
                                     message_id)
                elif "sticker" in bool_check_reply_to_message:
                    reply_to_message("{}A {} no le ha gustado este Sticker{}".format(EMOJI_STOP, user, EMOJI_STOP),
                                     chat, replied_text_message_id,
                                     message_id)
                elif "video" in bool_check_reply_to_message:
                    reply_to_message("{}A {} no le ha gustado este video{}️".format(EMOJI_STOP, user, EMOJI_STOP), chat,
                                     replied_text_message_id,
                                     message_id)
                elif "audio" in bool_check_reply_to_message:
                    reply_to_message(
                        "{}️A {} no le ha gustado esta pista de audio{}️".format(EMOJI_STOP, user, EMOJI_STOP), chat,
                        replied_text_message_id, message_id)
                elif "animation" in bool_check_reply_to_message:
                    reply_to_message("{}️A {} no le ha gustado este GIF{}️".format(EMOJI_STOP, user, EMOJI_STOP), chat,
                                     replied_text_message_id,
                                     message_id)
                elif "voice" in bool_check_reply_to_message:
                    reply_to_message("{}A {} no le ha gustado este audio{}️".format(EMOJI_STOP, user, EMOJI_STOP), chat,
                                     replied_text_message_id,
                                     message_id)
                elif "voice_note" in bool_check_reply_to_message:
                    reply_to_message(
                        "{}A {} no le ha gustado este videomensaje{}️".format(EMOJI_STOP, user, EMOJI_STOP), chat,
                        replied_text_message_id,
                        message_id)
                elif "document" in bool_check_reply_to_message:
                    reply_to_message("{}A {} no le ha gustado este documento{}".format(EMOJI_STOP, user, EMOJI_STOP),
                                     chat, replied_text_message_id,
                                     message_id)
                elif "contact" in bool_check_reply_to_message:
                    reply_to_message("{}A {} no le ha gustado este contacto{}️".format(EMOJI_STOP, user, EMOJI_STOP),
                                     chat, replied_text_message_id,
                                     message_id)
                elif "text" not in bool_check_reply_to_message:
                    reply_to_message("{}A {} no le ha gustado esta encuesta{}️".format(EMOJI_STOP, user, EMOJI_STOP),
                                     chat, replied_text_message_id,
                                     message_id)
                else:
                    replied_text = update["message"]["reply_to_message"]["text"]
                    send_message(
                        "{}{} le ha dado dislike al mensaje de {}{}: '{}'".format(EMOJI_STOP, user, replied_user,
                                                                                  EMOJI_STOP, replied_text),
                        chat, message_id)

        except KeyError as ke:

            print("No pasa nada, alguien ha puesto /dislike o /like sin contestar a nada: " + str(ke))

        except Exception as e:

            send_message("Error en like_dislike " + str(e), FATHER_CHAT_ID)


def get_last_chat_id_and_text(updates, i=1):
    num_updates = len(updates["result"])
    last_update = num_updates - i
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return text, chat_id


def send_message(text, chat_id, message_id=None, delete=True):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    if delete:
        delete_message(chat_id, message_id)


def reply_to_message(text, chat_id, reply_to_message_id, message_id=None, delete=True):
    url = URL + "sendMessage?text={}&chat_id={}&reply_to_message_id={}".format(text, chat_id, reply_to_message_id)
    get_url(url)
    if delete:
        delete_message(chat_id, message_id)


def delete_message(chat_id, message_id):
    url = URL + "deleteMessage?chat_id={}&message_id={}".format(chat_id, message_id)
    get_url(url)


def main():
    last_update_id = None

    try:
        while True:
            updates = get_updates(last_update_id)
            if len(updates.get("result")) > 0:
                last_update_id = get_last_update_id(updates) + 1
                like_dislike(updates)

            time.sleep(0.5)
    except Exception as e:
        send_message("Error en el main obteniendo result" + str(e), FATHER_CHAT_ID)


if __name__ == '__main__':
    main()
