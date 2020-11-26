from diaries.AbstractDiary import AbstractDiary


class ItoDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "今日は疲れた"

    def get_author(self):
        return "Ito"