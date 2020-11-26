from diaries.SampleDiary import DiarySample
from diaries.ItoDiaryNew import ItoDiaryNew

diaries = [DiarySample(), ItoDiaryNew()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()