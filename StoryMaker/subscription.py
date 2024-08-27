import os
from flask import session

def check_subscription():
    # Check if the user has any stories left in their subscription
    if 'story_count' not in session:
        session['story_count'] = 1  # Free users get 1 story
    
    return session['story_count'] > 0

def decrement_story_count():
    if 'story_count' in session:
        session['story_count'] -= 1

def upgrade_subscription():
    # TODO: Implement subscription upgrade logic
    session['story_count'] = float('inf')  # Unlimited stories for paid users