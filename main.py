from diaries.SampleDiary import DiarySample
from diaries.HiraiwaDiaryNew import DiaryHiraiwa

diaries = [DiarySample()
        , DiaryHiraiwa()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()