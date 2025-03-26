from flask import Flask

app = Flask(__name__)
@app.route('/')
def name():
    return 'Миссия Колонизация Марса'

@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def promotion():
    countdown_list = ['Человечество вырастает из детства.',
                      'Человечеству мала одна планета.',
                      'Мы сделаем обитаемыми безжизненные пока планеты.',
                      'И начнем с Марса!',
                      'Присоединяйся!']
    return '</br>'.join(countdown_list)

@app.route('/image_mars')
def image():
    return '''<head>
    <meta charset="UTF-8">
    <title>Привет, Марс!</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
        <h1>Жди нас, Марс!</h1>
    <img src="/static/img/mars.png" alt="Фотография Марса" style="max-width: 80%; display: block; margin: 20px auto;">
    <p style="text-align: center; font-style: italic;">Вот она какая, красная планета.</p>
    <div class="promo-list">
        <div class="promo-item line1">Человечество вырастает из детства.</div>
        <div class="promo-item line2">Человечеству мала одна планета.</div>
        <div class="promo-item line3">Мы сделаем обитаемыми безжизненные пока планеты.</div>
        <div class="promo-item line4">И начнем с Марса!</div>
        <div class="promo-item line5">Присоединяйся!</div>
    </div>
</body>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')