from flask import Flask
#Код для задачи номер 7 "Результаты отбора"
app = Flask(__name__)

@app.route('/results/<nickname>/<level>/<rating>')  # ← Слеш в начале обязателен!
def result(nickname, level, rating):
    countdown_list = []
    countdown_list.append(f'Претендента на участие в миссии {nickname}:')
    countdown_list.append(f'Поздравляем, ваш рейтинг после {level} этапа отбора:')
    countdown_list.append(f'составляет {rating}')
    countdown_list.append('Желаем удачи!')
    return image(countdown_list)


def image(slit):
    return '''<head>
    <meta charset="UTF-8">
    <title>Результаты</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <p style="text-align: center; font-style: italic;">''' + 'Результаты отбора' + '''</p>
    <div class="promo-list">
        <div class="promo-item line1">''' + slit[0] + '''</div>
        <div class="promo-item line2">''' + slit[1] + '''</div>
        <div class="promo-item line3">''' + slit[2] + '''</div>
        <div class="promo-item line3">''' + slit[3] + '''</div>
    </div>
</body>'''

if __name__ == '__main__':
    app.run(port=4002, host='127.0.0.1')
