
from authomatic.providers import oauth2, oauth1

CONFIG = {
    
    'tw': {
        'class_': oauth1.Twitter,
        
        'consumer_key': 'XIAwxTKWMwMKx7h4pJB0sQE8h',
        'consumer_secret': 'zascFBptMoJvWHtaltnaPvdOv8t01cbVZk09Z1FnrZmTUipjDQ',
    },
    
    'fb': {
           
        'class_': oauth2.Facebook,
        
        'consumer_key': '272653332934111',
        'consumer_secret': '386f985211c983c87713804f221b8b94',
        
        'scope': ['user_about_me', 'email', 'publish_stream'],
    },
    

}