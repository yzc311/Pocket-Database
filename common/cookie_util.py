import json
import os


class CookieUtil:


    @classmethod
    def cookie_exists(cls, file_path="data/cookies.json"):
        """
        判断cookie文件是否存在
        """

        return os.path.exists(file_path)



    @classmethod
    def save_cookie(cls, driver, file_path="data/cookies.json"):

        cookies = driver.get_cookies()


        directory = os.path.dirname(file_path)

        if directory and not os.path.exists(directory):
            os.makedirs(directory)


        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                cookies,
                f,
                ensure_ascii=False,
                indent=4
            )


        print("cookie保存成功")



    @classmethod
    def load_cookie(cls, driver, file_path="data/cookies.json"):


        with open(
            file_path,
            encoding="utf-8"
        ) as f:

            cookies = json.load(f)


        for cookie in cookies:

            driver.add_cookie(cookie)


        print("cookie加载成功")