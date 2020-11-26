from diaries.AbstractDiary import AbstractDiary


class SuzukiDiaryNew(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "テスト日記"

    def get_author(self):
        return "Suzuki"