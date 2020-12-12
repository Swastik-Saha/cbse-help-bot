import requests
from bs4 import BeautifulSoup


class Respond():

    book_url = "http://ncertbooks.prashanthellina.com/"

    def get_reply(self, msg, menu, payloadstr):
        msg = msg.lower()
        if payloadstr != "":
            payloadstr = eval(payloadstr)
        if msg == '2' and menu == "mainmenu":
            menu = "book_grademenu"
            msg = "Select your Class<br>Send the Number :-<br>1 -> For Class I<br>2 -> For Class II<br>3 -> For Class III<br>4 -> For Class IV<br>5 -> For Class V<br>6 -> For Grade VI<br>7 -> For Class VII<br>8 -> For Class VIII<br>9 -> For Class IX<br>10 -> For Class X<br>11 -> For Class XI<br>12 -> For Class XII"
            payloadstr = str(payloadstr)
            return msg, menu, payloadstr
        
        elif (menu == "book_grademenu") and (msg in [str(i) for i in range(1, 13)]):
            menu = "book_subjectmenu"
            r = requests.get(self.book_url)
            htmlContent = r.content
            soup = BeautifulSoup(htmlContent, 'html.parser')
            links = soup.find_all('a')
            subjects_and_links = {}
            n = 0
            reply_str = "Choose the Subject<br>Send the Number :-<br>"
            for item in links:
                link = item.get('href')
                subject = item.get_text()
                if str(link).startswith(msg):
                    n += 1
                    subjectlink = self.book_url + link
                    subjects_and_links[str(n)] = [subject, subjectlink]
                    reply_str += f"{n} -> For {subject}<br>"
            payloadstr = str(subjects_and_links)
            return reply_str.rstrip('<br>'), menu, payloadstr

        elif (menu == "book_subjectmenu") and (msg in payloadstr.keys()):
            menu = "book_bookmenu"
            subjectlink = payloadstr[msg][1]
            r = requests.get(subjectlink)
            htmlContent = r.content
            soup = BeautifulSoup(htmlContent, 'html.parser')
            books = soup.find_all('a')
            books_and_links = {}
            s_no = 0
            reply_str = "Choose the Book<br>Send the Number :-<br>"
            for book in books:
                bookname = book.h3.string
                booklink = self.book_url + book.get('href')
                s_no += 1
                books_and_links[str(s_no)] = [bookname, booklink]
                reply_str +=  f"{s_no} -> For {bookname}<br>"
            payloadstr = str(books_and_links)
            return reply_str.rstrip('<br>'), menu, payloadstr

        elif (menu == "book_bookmenu") and (msg in payloadstr.keys()):
            menu = "mainmenu"
            chaplink = payloadstr[msg][1] 
            reply = f'Visit the below link to download the book.<br><a href="{chaplink}" target="_blank"><strong>Click Here</strong></a>'
            payloadstr = ""
            return reply, menu, payloadstr

        elif msg == '1' and menu == "mainmenu":
            result_url = "https://cbseresults.nic.in/"
            reply = f'Click the below link to visit the results page<br><a href="{result_url}" target="_blank"><strong>Click Here</strong></a>'
            return reply, menu, payloadstr

        elif msg == '3' and menu == 'mainmenu':
            reply = "Select the Class <br> Send the Number :- <br> 1 -> For Class XII <br> 2 -> For Class X"
            payloadstr = str({'1': "XII", '2': "X"})
            menu = "sample_paper_menu"
            return reply, menu, payloadstr

        elif (menu == "sample_paper_menu") and (msg in payloadstr.keys()):
            if payloadstr[msg] == 'XII':
                sample_url = 'http://cbseacademic.nic.in/SQP_CLASSXII_2020-21.html'
                reply =  f'Click the below link to download the latest sample papers of class XII<br><a href="{sample_url}" target="_blank"><strong>Click Here</strong></a>'

            elif payloadstr[msg] == 'X':
                sample_url = 'http://cbseacademic.nic.in/SQP_CLASSX_2020-21.html'
                reply = f'Click the below link to download the latest sample papers of class X<br><a href="{sample_url}" target="_blank"><strong>Click Here</strong></a>'
            
            menu = 'mainmenu'
            payloadstr = ""
            return reply, menu, payloadstr

        elif msg == "4" and menu == "mainmenu":
            manual_link = "https://ncert.nic.in/science-laboratory-manual.php"
            reply = f'Click the below link to download the Lab Manuals <br><a href="{manual_link}" target="_blank"><strong>Click Here</strong></a>'
            return reply, menu, payloadstr

        elif msg == "5" and menu == "mainmenu":
            curriculum_link = "http://www.cbseacademic.nic.in/revisedcurriculum_2021.html"
            reply = f'Click the below link to download the Latest Syllabus <br><a href="{curriculum_link}" target="_blank"><strong>Click Here</strong></a>'
            return reply, menu, payloadstr

        elif msg == "6" and menu == "mainmenu":
            materials_link = "https://cbse.nic.in/newsite/examination.html"
            reply = f'Click the below link to view Examination Related Materials <br><a href="{materials_link}" target="_blank"><strong>Click Here</strong></a>'
            return reply, menu, payloadstr

        elif msg == "7" and menu == "mainmenu":
            circulars_link = "https://cbse.nic.in/newsite/circulars.html"
            reply = f'Click the below link to view Latest CBSE Circulars <br><a href="{circulars_link}" target="_blank"><strong>Click Here</strong></a>'
            return reply, menu, payloadstr

        else:
            reply = "Hii! <br>I am CBSE Help Bot. <br>Send the Number :- <br>1 -> For CBSE Results <br> 2 -> For NCERT Books <br> 3 -> For Latest Sample Papers <br> 4 -> For Lab Manual <br> 5 -> For Latest Syllabus <br> 6 -> For Examination Related Materials <br> 7 -> For Latest CBSE Circulars"
            menu = "mainmenu"
            payloadstr = ""
            return reply, menu, payloadstr

