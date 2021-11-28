import sys
import robot
import unittest
import world.text
import world.turtle.world
import world.obstacles
from test_base import captured_output

class MyTestCase(unittest.TestCase):

    def test_robot_import(self):
        import robot
        self.assertTrue('robot' in sys.modules, "robot imported in world.py")


    def test_obstacles_import(self):
        import world.obstacles
        self.assertTrue('world.obstacles' in sys.modules, "world.obstacles imported in world.py")

    def test_position_allowed_text(self):
        allowed = world.text.is_position_allowed(0, 200)
        self.assertEqual( allowed, True)

    def test_position_not_allowed_text(self):
        allowed = world.text.is_position_allowed(0, 201)
        self.assertEqual( allowed, False)
    
    def test_position_allowed_turtle(self):
        allowed = world.turtle.world.is_position_allowed(0, 200)
        self.assertEqual( allowed, True)

    def test_position_not_allowed_turtle(self):
        allowed = world.turtle.world.is_position_allowed(0, 201)
        self.assertEqual( allowed, False)

    def test_update_position(self):
        allowed = world.turtle.world.update_position(10)
        self.assertEqual(type(allowed), bool)
        
    def test_do_forward(self):
        forward = world.text.do_forward('007', 10)
        self.assertEqual(forward,(True, ' > '+'007'+' moved forward by '+str(10)+' steps.'))

    def test_do_forward_with_obstacles(self):
        forward = world.text.do_forward('007', 10)
        if world.text.update_position(10) == False and robot.count > 0:
            self.assertEqual(forward,(True, ''+'007'+': Sorry, there is an obstacle in the way.'))


    def test_do_forward_with_safe_zone(self):
        forward = world.text.do_forward('007', 10)
        if world.text.update_position(10) == False and robot.count == 0:
            self.assertEqual(forward,(True, ''+'007'+': Sorry, I cannot go outside my safe zone.'))

    def test_do_back(self):
        backward = world.text.do_back('007', 10)
        self.assertEqual(backward,(True, ' > '+'007'+' moved back by '+str(10)+' steps.'))

    def test_do_back_with_obstacles(self):
        backward = world.text.do_back('007', 10)
        if world.text.update_position(10) == False and robot.count > 0:
            self.assertEqual(backward,(True, ''+'007'+': Sorry, there is an obstacle in the way.'))


    def test_do_back_with_safe_zone(self):
        backward = world.text.do_back('007', 10)
        if world.text.update_position(10) == False and robot.count == 0:
            self.assertEqual(backward,(True, ''+'007'+': Sorry, I cannot go outside my safe zone.'))


    def test_do_left(self):
        left = world.text.do_left_turn('007')
        self.assertEqual(left,(True, ' > '+'007'+' turned left.'))

    def test_do_right(self):
        right = world.text.do_right_turn('007')
        self.assertEqual(right,(True, ' > '+'007'+' turned right.'))

      
if __name__ == '__main__':
    unittest.main()