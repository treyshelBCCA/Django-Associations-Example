from django.test import TestCase
from django.contrib.auth.models import User
from .models import *


# Create your tests here.
# ========= One To One Tests =========
class UserProfileTestCase(TestCase):
    def test_user_profile_creation(self):
        user = User.objects.create_user(username="testuser", password="12345")

        UserProfile.objects.create(
            user=user, bio="Bio of testuser", website="http://example.com"
        )

        user_profile = UserProfile.objects.get(user=user)

        # Verify that the UserProfile instance is associated with the correct User
        self.assertEqual(user_profile.user.username, "testuser")
        self.assertEqual(user_profile.bio, "Bio of testuser")
        self.assertEqual(user_profile.website, "http://example.com")


# ========= One To Many Tests =========
class AuthorBookTestCase(TestCase):
    def test_book_creation(self):
        author = Author.objects.create(name="John Doe", bio="A prolific writer")

        # Create a Book instance
        book = Book.objects.create(
            title="Sample Book",
            author=author,
            publication_date="2021-01-01",
        )

        # Verify the Book is linked to the Author correctly
        self.assertEqual(book.author.name, "John Doe")
        self.assertEqual(book.title, "Sample Book")

    def test_author_books_relation(self):
        author = Author.objects.create(name="John Doe", bio="A prolific writer")

        # Create a Book instance
        book = Book.objects.create(
            title="Sample Book",
            author=author,
            publication_date="2021-01-01",
        )

        # Check if the book is in the author's book list
        self.assertIn(book, author.books.all())


# ========= Many To Many =========
class CourseStudentTestCase(TestCase):
    def test_course_students(self):
        student1 = Student.objects.create(name="Alice", enrollment_date="2022-02-01")
        student2 = Student.objects.create(name="Bob", enrollment_date="2022-03-01")

        course = Course.objects.create(
            name="Mathematics", start_date="2022-01-01", end_date="2022-06-01"
        )

        course.students.add(student1, student2)
        # Check that both students are enrolled in the course
        self.assertIn(student1, course.students.all())
        self.assertIn(student2, course.students.all())

    def test_student_courses(self):
        student1 = Student.objects.create(name="Alice", enrollment_date="2022-02-01")
        student2 = Student.objects.create(name="Bob", enrollment_date="2022-03-01")

        course = Course.objects.create(
            name="Mathematics", start_date="2022-01-01", end_date="2022-06-01"
        )
        course.students.add(student1, student2)

        # Check that the course is in each student's course list
        self.assertIn(course, student1.courses.all())
        self.assertIn(course, student2.courses.all())
