import sys
from test_base import captured_output
import unittest
import robot


class MyTestCase(unittest.TestCase):

    def test_text_import(self):
        import world.text
        self.assertTrue('world.text' in sys.modules, "world.text imported in robot")

    def test_turtle_import(self):
        import world.turtle
        self.assertTrue('world.turtle' in sys.modules, "world.turtle imported in robot")

    def test_obstacles_import(self):
        import world.obstacles
        self.assertTrue('world.obstacles' in sys.modules, "world.obstacles imported in robot")

    def test_help_works_in_call_command(self):
        help = robot.do_help() 
        result = robot.call_command('help', '', '007')
        self.assertEqual(help,result)
        
    def test_forward_works_in_call_command(self):
        import world.text
        forward = world.text.do_forward('007', 10)
        result = robot.call_command('forward', 10, '007')
        self.assertEqual(forward,result)

    # def test_back_works_in_call_command(self):
    #     import world.text
    #     back = world.text.do_back('007', 100)
    #     result = robot.call_command('back', 100, '007',[''])
    #     self.assertEqual(back,result)

    def test_right_works_in_call_command(self):
        import world.text
        right = world.text.do_right_turn('007')
        result = robot.call_command('right', '', '007')
        self.assertEqual(right,result)
        

    def test_left_works_in_call_command(self):
        import world.text
        left = world.text.do_left_turn('007')
        result = robot.call_command('left', '', '007')
        self.assertEqual(left,result)

    def test_sprint_works_in_call_command(self):
        with captured_output():
            import world.text
            sprint = world.text.do_sprint('007', 5)
            result = robot.call_command('sprint', 5, '007')
            self.assertEqual(sprint,result)

    def test_handle_command(self):
        import world.text
        result = robot.handle_command('007','off')
        self.assertEqual(result , False)
    
    def test_handle_command(self):
        import world.text
        result = robot.handle_command('007','off')
        self.assertEqual(result , False)

        
if __name__ == '__main__':
    unittest.main()