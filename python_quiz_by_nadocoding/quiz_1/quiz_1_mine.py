def yield_name(names):
    for name in names:
        yield name


def write_txt(names, text):
    for name in yield_name(names):
        with open(f'./{name}.txt', 'w', encoding="utf8") as txt_file:
            txt_file.write(text.format(name, name))


names = ["아이언맨", "토르", "헐크", "스파이더맨"]
text = """안녕하세요? {}님.

(주)나도출판 편집자 나코입니다.
현재 저희 출판사는 파이썬에 관한 주제로 책 출간을 기획 중입니다.
{}님의 유튜브 영상을 보고 연락을 드리게 되었습니다.
자세한 내용은 첨부드리는 제안서를 확인 부탁드리며, 긍정적인 회신 기다리겠습니다.

좋은 하루 보내세요 ^^
감사합니다.

- 나코 드림.
"""

write_txt(names, text)