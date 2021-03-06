from flask import Flask, request, render_template, redirect, url_for, flash
app = Flask(__name__)
app.secret_key='12345'

@app.route("/",methods=['POST','GET'])
def account():
    if request.method == 'POST':
        print (request.form)
        name = request.form['name']
        city = request.form['city']

        return render_template('welcome.html',name=name,city=city)
        
    else:
        page ='''
        <html>
        <head>
            <meta charset="utf-8">
            <meta name=""viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://fonts.googleapis.com/css2?family=Leckerli+One&display=swap" rel="stylesheet">
            <link href="https://fonts.googleapis.com/css2?family=Itim&display=swap" rel="stylesheet">           
            <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">
            <link href="/static/css/cssWelcome.css" rel="stylesheet"/>
            
        
        </head>
        <body>
            <div class="container-fluid" >
                <div class="row">
                <h2 class="title">Welcome to Shappy!</h2>
                </div>
            </div>
            <div class="container-fluid">
                <div class="row">
                <div class="col-sm-3">
                </div>
                <div class="col-sm-6">
                <form action="" method="post" name="form">
                <label for="name">What is your name?</label>
                <input type="text" name="name" id="name"/>
                <br>
                <label for="city">What is the name of your city?</label>
                <input type="text" name="city" id="city"/>
                <br>                
                <button class="button" type="submit">Let's play!</button>
                </div>
                <div class="col-sm-3">
                </div>
                </form>
                </div>
            </div>
        </body>
        </html>'''

        return page, 200
    


@app.route("/fstScreen", methods=['POST','GET'])
def firstScreen():
    return render_template('screen1.html')


@app.route("/scndScreen",methods=['POST','GET'])
def secondScreen():
    return render_template('screen2.html')

@app.route("/thrdScreen",methods=['POST','GET'])
def thirdScreen():
    return render_template('screen3.html')

@app.route("/endSerie",methods=['POST','GET'])
def EndOfSerie():
    return render_template('endSerie.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

