import pyperclip
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier


module_urls = {
    "Module 2": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-operating-systems-module-2-chapter-02-exam-answers/",
    "Module 3": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-working-in-linux-module-3-chapter-03-exam-answers/",
    "Module 4": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-open-source-software-and-licensing-module-4-chapter-04-exam-answers/",
    "Module 5": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-command-line-skills-module-5-chapter-05-exam-answers/",
    "Module 6": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-navigating-the-filesystem-module-7-chapter-07-exam-answers/",
    "Module 7": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-working-in-linux-module-7-chapter-07-exam-answers/",
    "Module 8": "https://examtube.org/ndg-linux-essentials-2-21/managing-files-and-directories-module-8-chapter-08-exam-answers/",
    "Module 9": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-archiving-and-compression-module-9-chapter-09-exam-answers/",
    "Module 10": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-working-with-text-module-10-chapter-10-exam-answers-full-100/",
    "Module 11": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-basic-scripting-module-11-chapter-11-exam-answers-full-100/",
    "Module 12": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-understanding-computer-hardware-module-12-chapter-12-exam-answers-full-100/",
    "Module 13": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-where-data-is-stored-module-13-chapter-13-exam-answers-full-100/",
    "Module 14": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-network-configuration-module-14-chapter-14-exam-answers-full-100/",
    "Module 15": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-system-and-user-security-module-15-chapter-15-exam-answers-full-100/",
    "Module 16": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-creating-users-and-groups-module-16-chapter-16-exam-answers-full-100/",
    "Module 17": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-ownership-and-permissions-module-17-chapter-17-exam-answers-full-100/",
    "Module 18": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-working-in-linux-module-18-chapter-18-exam-answers/",
    "Final": "https://examtube.org/ndg-linux-essentials-2-21/ndg-linux-essentials-2-21-special-directories-and-files-module-18-chapter-18-exam-answers-full-100/"
}

print("Available modules:")
for module in module_urls:
    print(module)

selectedModule = input("Enter the module name: ")
url = module_urls[selectedModule]

def scrape_questions_answers():
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    question_answers = {}
    questions = soup.find_all("h3")

    for question in questions:
        question_text = question.get_text(strip=True)
        unordered_list = question.find_next("ul")
        if unordered_list:
            spans = unordered_list.find_all("span", style=lambda value: value and "color: #ff0000" in value)
            if spans:
                answer_texts = ", ".join(span.get_text(strip=True) for span in spans)
                question_answers[question_text] = answer_texts
    return question_answers

def check_clipboard():
    clipboard_text = pyperclip.paste().strip()
    if clipboard_text in question_answers:
        answer = question_answers[clipboard_text]
        if answer:
            toaster = ToastNotifier()
            toaster.show_toast("Answer", answer, duration=5, threaded=True)
            pyperclip.copy("")


question_answers = scrape_questions_answers()

while True:
    check_clipboard()