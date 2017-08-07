
import unittest

from changes import get_commits, readfile

class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = readfile('changes_python.log')

    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0]['author'])
        self.assertEqual('r1551925', commits[0]['revision'])
        self.assertEqual('2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', commits[0]["date"])

if __name__ == '__main__':
    unittest.main()
