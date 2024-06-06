from posts import MessagePost, PhotoPost, EventPost #Importing 3 classes from posts module.


class Newsfeed():
    """
    The NewsFeed class stores news posts for the news feed in a
    social network application (like FaceBook or Google+).
     
    Display of the posts is currently simulated by printing the
    details to the terminal. (Later, this should display in a browser.)
     
    This version does not save the data to disk, and it does not
    provide any search or ordering functions.
    
    @author: Alessandro
    """
    def __init__(self):
        self.posts = list()    # list of message/photo posts

    # Add a post to the news feed.
    def add_post(self, post):
        self.posts.append(post)

    def display(self):
        """Display all the newsfeed details"""
        for post in self.posts:
            print(post)
            print()

newsfeed = Newsfeed() #Creating a newsfeed

eventpost1 = EventPost("Fabian", "Boxing", "MMA fight", "First pro fight", "Sports city", "9 pm", "10 pm") #Creating a new eventpost
newsfeed.add_post(eventpost1) 

photopost1 = PhotoPost("Basil", "jpg", "Won the Cricket tournament")
photopost1.like()
photopost1.unlike()
photopost1.like()
photopost1.add_comment("OMG Congratsss")
photopost1.edit_comment("OMG Congratsss","YAYAYAY")
newsfeed.add_post(photopost1)

messagepost1 = MessagePost("Gelo", "Spending time with Fabian")
messagepost1.updated_message("Fabian spending time with Enid***")
messagepost1.emotion("Excited")
messagepost1.like()
messagepost1.add_comment("\U0001F600")
messagepost1.add_comment("\U00002764")
newsfeed.add_post(messagepost1)

newsfeed.display()