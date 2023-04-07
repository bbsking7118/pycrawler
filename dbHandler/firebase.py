import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore


class FireAuth():
    def __init__(self, mode=None):
        super().__init__()
        # Firebase database 인증 및 앱 초기화
        self.cred = credentials.Certificate(r'config/auth.json')
        firebase_admin.initialize_app(self.cred, {
            'projectId': 'e2db-4d6f7',
        })


class FireStore():
    def __init__(self, mode=None):
        super().__init__()
        self.db = firestore.client()

    def getIntance(self):
        return self.db

    def write(self, col, doc, data):
        doc_ref = self.db.collection(col).document(doc)
        doc_ref.set(data)
        # db.collection(u'users').delete()

    def write(self, col, data):
        update_time, doc_ref = self.db.collection(col).add(data)
        print(doc_ref.id)
        return doc_ref
        # doc_ref.set(data)
        # db.collection(u'users').delete()
        
class FireStorage():
    def __init__(self, mode=None):
        super().__init__()




