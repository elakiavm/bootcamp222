from flask import Flask, render_template, request, redirect, url_for, jsonify

def index():

        return render_template('index.html', games=Game.query.all())


class Game(db.Model):

    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(255), nullable=False)

    description = db.Column(db.String(1024), nullable=False)

    yor = db.Column(db.Integer, nullable=False)

    publisher = db.Column(db.String(255), nullable=False)

    genre = db.Column(db.String(255), nullable=False)

 

    db.create_all()

 

@app.route('/')

def index():

    return render_template('index.html', games=Game.query.all())

 

@app.route('/games/create', methods=['POST'])

def create_game():

   try:

       title = request.get_json()['title']

       description = request.get_json()['description']

       yor = request.get_json()['yor']

       publisher = request.get_json()['publisher']

       genre = request.get_json()['genre']

       game = Game(title=title, description=description, yor=yor, publisher=publisher, genre=genre)

       db.session.add(game)

       db.session.commit()

   except:

       db.session.rollback()

   finally:

       return jsonify({'title':game.title, 'id':game.id})

       db.session.close()

 

@app.route('/games/<game_id>/read', methods=['POST'])

def read_game(game_id):

    game=Game.query.get(game_id)

    return jsonify({

    'title':game.title,

    'description':game.description,

    'yor':game.yor,

    'publisher':game.publisher,

    'genre':game.genre

    })

 

@app.route('/games/<game_id>/update', methods=['POST'])

def update_game(game_id):

    error = False

    try:

                title = request.get_json()['title']

                description = request.get_json()['description']

                yor = request.get_json()['yor']

                publisher = request.get_json()['publisher']

                genre = request.get_json()['genre']

                

                game=Game.query.get(game_id)

                game.title = title

                game.description = description

                game.yor = yor

                game.publisher = publisher

                game.genre = genre

                db.session.query(Game).filter_by(id=game_id).update ({"title": title, "description": description, "yor": yor, "publisher": publisher, "genre": genre}, synchronize_session='fetch')

                db.session.commit()

                    except:

                    db.session.rollback()

                    finally:

                    return jsonify({

                    'title':game.title,

                    })

                    db.session.close()

    

@app.route('/games/<game_id>/delete', methods=['DELETE'])

def delete_game(game_id):

    try:

        game=Game.query.get(game_id)

        db.session.delete(game)

        db.session.commit()

        db.session.close()

            except:

        error = True

        db.session.rollback()

            finally:

        db.session.close()

            return jsonify({'success':True})

 

if __name__ == '__main__':

    app.run()