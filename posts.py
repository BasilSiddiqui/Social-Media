import datetime #Importing a module datetime
import time #Importing a module for tracking time


class Post():
    """
    This class stores information about a post in a social network. 
    The main part of the post consists of a (possibly multi-line)
    text message. Other data, such as author and time, are al
    @author: Alessandro 
    """
    def __init__(self, author):
        self.username = author   # username of the post's author
        self.timestamp = datetime.datetime.now() #Jots down the time when the post was created
     
    def get_timestamp(self):
        """Return the timestamp of this post."""
        return self.timestamp
    
    def __str__(self):
        """Display the details of this post."""
        post_str = f"Author: {self.username}\n" 
        post_str += f"Created: {self._time_string(self.timestamp)}\n" #Concatonate the strings together 
        return post_str
    
    def _time_string(self, time):
        """Create a string describing a time point in the past in terms relative 
        to current time, such as "30 seconds ago" or "7 minutes ago"""
        current = datetime.datetime.now()
        past_time: datetime.timedelta = current - time      # time passed in milliseconds
        seconds = past_time.total_seconds() 
        minutes = seconds // 60
        if minutes > 0 :
            return f"{minutes} minutes ago"
        else:
            return f"{seconds} seconds ago"
        
class CommentedPost(Post):
    
    def __init__(self, author):
        super().__init__(author)
        self.username = author   # username of the post's author
        self.timestamp = datetime.datetime.now() #Time of comment
        self.likes = 0 #Likes start from 0 on a new post
        self.comments = list() #Creating a list for comments

    def like(self):
        """Record one more 'Like' indication from a user."""
        self.likes += 1 #Add a like

    def unlike(self):
        """Record that a user has withdrawn his/her 'Like' vote."""
        if self.likes > 0 : #If post is already liked
            self.likes -= 1 #Remove a like

    def add_comment(self, text):
        """Add a comment to this post."""
        self.comments.append(text) #Add a comment 
        
    def get_timestamp(self):
        """Return the timestamp of this post."""
        return self.timestamp
                
    def edit_comment(self,  comment_to_edit, edited_comment):
        if comment_to_edit in self.comments:
            comment_index = self.comments.index(comment_to_edit)
            self.comments[comment_index] = edited_comment #Edited comment becomes the new comment, hence changing it.
 
    def __str__(self):
        post_str = super().__str__()
        if self.likes > 0:
            post_str += f"\t- {self.likes} people like this." #Shows how many people like the comment
    
        if len(self.comments) == 0 :
            post_str += "# No comments." #Shows no comment if there are 0 of them
        else :
            post_str += f"# {len(self.comments)} comment(s)\n"
            for comment in self.comments:
                post_str += f"\t- Comment: {comment}\n"
        return post_str
            
class MessagePost(CommentedPost):
    """
    This class stores information about a post in a social network. 
    The main part of the post consists of a (possibly multi-line)
    text message. Other data, such as author and time, are al
    @author: Alessandro
    """
    def __init__(self, author, message):
        super().__init__(author)
        self.message = message      # an arbitrarily (multi-line) message

    def get_message(self):
        """Return the message contained in this post."""
        return self.message
    
    def updated_message(self, new_message):
       self.message = new_message #Message changes as edited message becomes the new message.
        
    def emotion(self, emotion):
        feeling = "Feeling "+emotion
        print(feeling)
    
    def __str__(self):
     post_str = f"[MessagePost] {self.message}\n"
     # calls the superclass __str__ method to inherit its behaviour
     post_str += super().__str__()
     return post_str
 
class PhotoPost(CommentedPost):
    """
    This class stores information about a post in a social network. 
    The main part of the post consists of a photo and a caption. 
    Other data, such as author and time, are also stored.
    @author: Alessandro
    """
    def __init__(self, author, filename, caption):
        super().__init__(author)   # username of the post's author
        self.filename = filename      
        self.caption = caption #Storing caption in caption

    def get_image_file(self):
        """Return the file name of the image in this post."""
        return self.filename

    def get_caption(self):
        """Return the caption of the image of this post."""
        return self.caption
    
    def update_caption(self, new_caption):
        self.caption = new_caption #Caption gets edited as caption is now changed to a new one

    def __str__(self):
        post_str = f"[PhotoPost: {self.filename}] {self.caption}\n"
        # calls the superclass __str__ method to inherit its behaviour
        post_str += super().__str__()
        return post_str #Returns post_str
     
class EventPost(Post): #Inheriting a child class from a parent class.
    def __init__(self, author, event_type, heading, details, location, start_time, stop_time):
        super().__init__(author)
        self.event_type = event_type #Storing the type of event.
        self.heading = heading #Storing title of event.
        self.details = details #Storing details of event.
        self.location = location #Storing location of event.
        self.start_time = start_time #Storing start time of event.
        self.stop_time = stop_time #Storing end time of event.

    def __str__(self):
        post_str = f"{self.event_type}\n{self.heading}\n{self.details}\n{self.location}\n{self.start_time}\n{self.stop_time}"
        return post_str