from flask import Flask , render_template , url_for , redirect , request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://youruser:yourpassword@localhost/yourdatabase'

db = SQLAlchemy(app)

class Event_Collector(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(125) , nullable=False)
    desc = db.Column(db.String(225) , nullable=True)
    date = db.Column(db.DateTime , default=datetime.now())
    def __rep__(self):
        return '<Event %r>' % self.id
    pass
pass

"""
with app.app_context():
    db.create_all()
"""

@app.route('/' , methods=['GET' , 'POST'])
def Add():
    if request.method=='POST':
        event_listner = request.form['content']
        event_desc = request.form['desc']
        new_event = Event_Collector(name=event_listner , desc=event_desc)
        try:
            db.session.add(new_event)
            db.session.commit()
            return redirect('/')
        except:
            return "ERROR"
    else:
        events = Event_Collector.query.order_by(Event_Collector.date).all()
        return render_template('Add.html',events=events)
pass

@app.route('/delete/<int:id>')
def delete(id):
    event_to_delete = Event_Collector.query.get_or_404(id)

    try:
        db.session.delete(event_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

if __name__ == "__main__":
    app.run(debug=True)
