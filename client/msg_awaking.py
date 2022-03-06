import time, requests


class AppAwaking:
    """
    Helper class to make awaking message of bot.
    """

    def init_bot_info(self) -> None:
        self.bot = self.get_me()

    def send_awaking_msg(self) -> None:
        txt = self.prepare_awaking_msg()
        self.send_message(int(self.config_messages), txt)

    def prepare_awaking_msg(self) -> str:
        return (
            "**Turned on bot:** \n\n"
            f"```Bot:      {self.bot.first_name}\n"
            f"Username: @{self.bot.username}\n"
            f"User ID:  {self.bot.id}\n\n"
            f"{self.find_location()}"
            f"Time:     {time.strftime('%H:%M:%S %d/%m/%Y', time.localtime())}```"
        )

    @staticmethod
    def find_location():
        url = "http://ip-api.com/json/"
        with requests.get(url) as response:
            try:
                response.raise_for_status()
                json = response.json()
                return (
                    f"City:     {json['city']}\n"
                    f"Region:   {json['regionName']}\n"
                    f"Country:  {json['country']} {json['countryCode']}\n"
                    f"IP:       {json['query']}\n\n"
                )
            except:
                return ""
