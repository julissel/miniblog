from datetime import  datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post


class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='kate')
        u.set_password('katekate')
        self.assertFalse(u.check_password('annann'))
        self.assertTrue(u.check_password('katekate'))

    def test_avatar(self):
        u = User(username='john', email='john@example.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/'
                                         'd4c74594d841139328695756648b6bd6'
                                         '?d=identicon&s=128'))

    def test_follow(self):
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='kate', email='kate@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u1.followed.first().username, 'kate')
        self.assertEqual(u2.followers.count(), 1)
        self.assertEqual(u2.followers.first().username, 'john')

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)

    def test_follow_posts(self):
        # 4 new users
        u1 = User(username='kate', email='kate@example.com')
        u2 = User(username='anna', email='anna@example.com')
        u3 = User(username='nina', email='nina@example.com')
        u4 = User(username='polina', email='polina@axample.com')
        db.session.add_all([u1, u2, u3, u4])

        # 4 new posts
        now = datetime.utcnow()
        p1 = Post(body="post from kate", author=u1, timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from anna", author=u2, timestamp=now + timedelta(seconds=5))
        p3 = Post(body="post from nina", author=u3, timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from polina", author=u4, timestamp=now + timedelta(seconds=10))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # setup the followers
        u1.follow(u2) # kate follows anna
        u1.follow(u4) # kate follows polina
        u2.follow(u3) # anna follows nina
        u3.follow(u4) # nina follows polina
        db.session.commit()

        # checking following posts of each user
        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(set(f1), set([p2, p4, p1]))
        self.assertEqual(set(f2), set([p2, p3]))
        self.assertEqual(set(f3), set([p3, p4]))
        self.assertEqual(f4, [p4])

if __name__ == '__main__':
    unittest.main(verbosity=2)
