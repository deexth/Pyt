import unittest
from survey import Anonymous


class TestSurvey(unittest.TestCase):
    """Test for the calss Anonymous"""
    
    def setUp(self):
        """Create a survey and a set of responses foe use in all test modules."""
        
        question = "What language did you first learn?\n"
        self.my_survey = Anonymous(question)
        self.responses = ['Kinyarwanda', 'French', 'English']
        
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
            

if __name__ == '__main__':
    unittest.main()