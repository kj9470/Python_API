from flask import Flask, render_template
import corona_data
from datetime import date, timedelta #날짜 기준으로 요청

app = Flask(__name__)

@app.route('/')
def index():
    now = date.today()
    now_str = now.strftime("%Y%m%d") # 날짜가 변수형으로 받아들이기 때문에 문자열로 바꿔야함
    print(now_str) # 확인 단계

    data = corona_data.get_corona_data(now_str, now_str) # 시작하는 날짜와 끝내는 날짜
    print(data) # 데이터 확인

    if not data : # 데이터가 없을 경우
        yesterday = now - timedelta(days = 1) # 하루 전날 데이터
        yesterday_str = yesterday.strftime("%Y%m%d")
        print(yesterday_str)

        data = corona_data.get_corona_data(yesterday_str, yesterday_str)
        print(data)

    return render_template('index.html', data = data[1:]) # 첫번째부터 끝까지 배열에 저장, html로 이동

if __name__ == "__main__":
    app.run(debug = True)
