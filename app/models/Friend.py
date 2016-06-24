from system.core.model import Model

class Friend(Model):
    def __init__(self):
        super(Friend, self).__init__()

    def get_all(self):
        query="SELECT * FROM friends"
        return self.db.query_db(query)

    def get_by_id(self, id):
        query="SELECT * FROM friends WHERE id=:id LIMIT 1"
        data={'id':id}
        return self.db.get_one(query, data)

    def insert_friend(self, request_form):
        data={
            'first_name':request_form['first_name'], 
            'last_name':request_form['last_name'], 
            'occupation':request_form['occupation'], 
            'known_since':request_form['known_since']
        }
        query="INSERT INTO friends (first_name, last_name, occupation, known_since, created_at, updated_at) VALUES (:first_name, :last_name, :occupation, :known_since, NOW(), NOW())"
        return self.db.query_db(query, data)

    def delete_friend(self, id):
        query="DELETE FROM friends WHERE id=:id"
        data={'id':id}
        return self.db.query_db(query, data)

    def update_friend(self, request_form, id):
        data={
            'id':id, 
            'first_name':request_form['first_name'], 
            'last_name':request_form['last_name'], 
            'occupation':request_form['occupation'], 
            'known_since':request_form['known_since']
        }
        query="UPDATE friends SET first_name=:first_name, last_name=:last_name, occupation=:occupation, known_since=:known_since, updated_at=NOW() WHERE id=:id"
        return self.db.query_db(query, data)