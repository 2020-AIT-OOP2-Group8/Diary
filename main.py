from diaries.SampleDiary import DiarySample
from diaries.SuzukiDiaryNew import SuzukiDiaryNew

diaries = [DiarySample(), SuzukiDiaryNew()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()