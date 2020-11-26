from diaries.AbstractDiary import AbstractDiary


class MiyamuraDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "GitHub使えるようになりたい"

    def get_author(self):
        return "Miyamura"