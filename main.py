from diaries.SampleDiary import DiarySample
from diaries.SuzukiDiaryNew import SuzukiDiaryNew
from diaries.MiyamuraDiaryNew import MiyamuraDiaryNew

diaries = [DiarySample(), MiyamuraDiaryNew(), SuzukiDiaryNew(), ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()