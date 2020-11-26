from diaries.AbstractDiary import AbstractDiary


class DiaryHiraiwa(AbstractDiary):

    def get_date(self):
        return "2020-11-26"

    def get_summary(self):
        return "GitHub難しい(T . T)"

    def get_author(self):
        return "Hiraiwa"