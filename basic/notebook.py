class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_back_number(self, new_number):
        print("선수의 등번호를 변경한다 : From %d to %d" % (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, My name is %s. I play in %s in center." % (self.name, self.position)

# _ 1개 : 이후로 쓰이지 않을 변수에 특별한 이름을 부여하고 싶지 않을 때 사용
# 임의의 변수명 대신에 사용
# __ 2개 : 특수한 예약 함수나 변수에 사용

junghyun = SoccerPlayer("junghyun", "MF", 27)

print("현재 선수의 등 번호는 : ", junghyun.back_number)
junghyun.change_back_number(5)
print("현재 선수의 등 번호는 : ", junghyun.back_number)
print(junghyun)

names = ["messi", "ramos", "ronaldo", "park", "buffon"]
positions = ["mf", "df", "cf", "wf", "gk"]
numbers = [10, 4, 7, 13, 1]

players = [[name, position, number] for name, position, number in zip(names, positions, numbers)]
print(players)
print(players[0])

player_object = [SoccerPlayer(name, position, number) for name, position, number in zip(names, positions, numbers)]
print(player_object[0])


# 노트북 프로그램 만들기

class Note(object):
    def __init__(self, contents = None):
        self.contents = contents

    def write_contents(self, contents):
        self.contents = conents

    def remove(self):
        self.conents = ""

    def __str__(self):
        return self.contents



class NoteBook(object):
    def __init__(self, title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def add_note(self, note, page = 0):
        if (self.page_number < 300):
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                self.notes = {page : note}
                self.page_number += 1
        else:
            print("페이지가 모두 해워졌다.")

    def remove_notes(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않는다.")

    def get_number_of_pages(self):
        return len(self.notes.keys())
