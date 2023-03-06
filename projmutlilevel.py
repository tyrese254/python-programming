class book:
    def __init__(self, title, sub_heading):
        self.title = title
        self.sub_heading = sub_heading

    def text(self):
        print("Title :The Jolly Rodger")

    def sub(self):
        print("SUB heading :The Foustin lake")


class Description(book):
    def __init__(self, title, sub_heading):
        super().__init__(title,sub_heading)

    def author(self):
        print("AUTHOR : John Whistler")



class story_line(Description):
    def __init__(self, title, sub_heading):
        super().__init__(title,sub_heading)
    def line(self):
        print("Story Line : Is about a young man called Tompson who found love in terrible war and stuggle to have the love of his life")

class setting(story_line):
    def __init__(self, title, sub_heading):
        super().__init__(title, sub_heading)
    def place(self):
        print("Story Setting : The story is set in Califonia in the 80's")

s = setting("The Jolly Rodger - (revised)"," The Foustin lake - (revised)")
s.text()
s.sub()
s.author()
s.line()
s.place()
(print(s.title))
(print(s.sub_heading))


