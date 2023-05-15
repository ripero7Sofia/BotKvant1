import datetime
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


class VKBot:
	def __init__(self, bot_name, api_token):
		self.session = vk_api.VkApi(token=api_token)
		self.longpoll = VkLongPoll(self.session)
		self.vk = self.session.get_api()
		self.bot_name = bot_name

	def send_message(self, message, id):
		self.vk.messages.send(user_id=id, message=message, random_id=datetime.datetime.now().microsecond)

	def start(self):
		for event in self.longpoll.listen():
			if event.type == VkEventType.MESSAGE_NEW and event.to_me:
				if str(event.text).split(" ")[0] == self.bot_name:
					self.send_message(message="Это я!", id=event.user_id)


bot = VKBot("KvantBot", "vk1.a.remDLGeajVP-GFKzEju_s2f63RdS659FP5PeNTJvT_st7grhlnnqiw46rasXmlNfIRdt40PvfhmrbbtjAccuVRYbREaYsH58GI32IzeiE0ieR_iW1biMm76kX23lLxXDvu8sX9gvmeiDMFcHYdzoW8QZXYCbe-TZnKeYiWe_y2tXDs1vZxnVCEUoNCmM767AAULJbfAQ8VNIeBDohmLQUw")
bot.start()
