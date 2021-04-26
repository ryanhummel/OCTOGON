from django.test import TestCase
from user_profile_db.models import Course, User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="warsh1", email="example@example.com", password="password", name_first="James", name_last="Warshaw", is_instructor=False)
        # User.objects.create(username="warsh2", email="example@example2.com", password="password", name_first="James2", name_last="Warshaw2", is_instructor=False)
        # User.objects.create(username="warsh3", email="example@example3.com", password="password", name_first="James3", name_last="Warshaw3", is_instructor=False)
        # User.objects.create(username="warsh4", email="example@example4.com", password="password", name_first="James4", name_last="Warshaw4", is_instructor=False)
        Course.objects.create(name_short="CMSC 447", name_long="Software Engineering I")
        # Course.objects.create(name_short="CMSC 448", name_long="Software Engineering II")
        # Course.objects.create(name_short="CMSC 449", name_long="Software Engineering III")
        # Course.objects.create(name_short="CMSC 450", name_long="Software Engineering IV")
    def test_User(self):
        user = User.objects.get(username="warsh1")
        # user.save()
        course = Course.objects.get(name_short="CMSC 447")
        # course.save()
        self.assertEqual(user.name_first, "James")
        self.assertEqual(user.name_last, "Warshaw")
        self.assertEqual(user.is_instructor, False)
        user.courses.add(course)
        # user.save()
        self.assertEqual(user.courses.get(id=1), course)
        self.assertEqual(user.courses.get(id=1).name_long, "Software Engineering I")
    def test_Course(self):
        course = Course.objects.get(name_short="CMSC 447")
        self.assertEqual(course.name_short, "CMSC 447")
        self.assertEqual(course.name_long, "Software Engineering I")
    
    #THIS IS PURELY FOR PERSONAL TESTING REASONS
    # def test_Test(self):
        # user1 = User.objects.get(username="warsh1")
        # #user1.save()
        # user2 = User.objects.get(username="warsh2")
        # #user2.save()
        # user3 = User.objects.get(username="warsh3")
        # #user3.save()
        # user4 = User.objects.get(username="warsh4")
        # #user4.save()
        # course1 = Course.objects.get(name_short="CMSC 447")
        # #course1.save()
        # course2 = Course.objects.get(name_short="CMSC 448")
        # #course2.save()
        # course3 = Course.objects.get(name_short="CMSC 449")
        # #course3.save()
        # course4 = Course.objects.get(name_short="CMSC 450")
        # #course4.save()
        # user1.courses.add(course1)
        # user1.courses.add(course2)
        # user1.courses.add(course3)
        # user1.courses.add(course4)
        # user2.courses.add(course1)
        # user2.courses.add(course3)
        # user2.courses.add(course4)
        # user3.courses.add(course1)
        # user3.courses.add(course2)
        # user4.courses.add(course1)
        # user4.courses.add(course3)
        # #user1.save()
        # #user2.save()
        # #user3.save()
        # #user4.save()
        # #course1.save()
        # #course2.save()
        # #course3.save()
        # #course4.save()
        # print("\nclasses in user1")
        # for foo in user1.courses.all():
            # print(foo.name_long)
        # print("users in class 2")
        # for bar in course2.user_set.all():
            # print(bar)
        # print("users in class 1")
        # for baz in course1.user_set.all():
            # print(baz)