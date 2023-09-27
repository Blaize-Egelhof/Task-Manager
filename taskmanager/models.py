from taskmanager import db

class Category(db.Model): 
    #Schema for category model

    id= db.Column(db.Integer, primary_key="True")
    category_name = db.Column(db.String(25), unique = True , nullable = False)

    def __repr__(self):
        #represent itself as a string. 
        return self



class Task(db.Model): 
    #Schema for task model  model
    id= db.Column(db.Integer, primary_key="True")
    task_name = db.Column(db.string(50), unique=True , nullable=False)
    task_description = db.Column(db.Text, nullable = False)
    is_urgent = db.Column(db.Boolean, default = False , nullable =False)

    def __repr__(self):
        #represent itself as a string. 
        return self