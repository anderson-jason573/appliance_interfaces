"""
This module tracks the progress of desired actions.
"""

class ProgressBar:
    def __init__(self, message, length):
        self.message = message
        self.length = length

    def progress_bar(self, bar_count):
        print(self.message, bar_count,'/',self.length)

# end
