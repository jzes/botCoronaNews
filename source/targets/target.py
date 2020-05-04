from models.news import New

class Target:

    def connect(self):
        """Connect to target API"""
        pass

    def post_new(self, new: New):
        """Post a new in target"""
        pass

    def can_post(self, new: New)->bool:
        """
            Check if a new can be posted, 
            if is not a dublicate or something like that
        """
        pass