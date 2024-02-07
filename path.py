{
    'auth': {'path': 'auth', 'children':
                {
                    'login': {'path': 'login'}, 
                    'logout': {'path': 'logout'}, 
                    'register': {'path': 'register'}
                }
        },

    'api': {'path': 'api', 'children': 
                {'favorite': {'path': 'favorite'}
                 }
            }, 

    'course': {'path': '<course_name>', 'children': 
                {'chapter': 
                    {'path': '<chapter_name>', 'children': 
                        {'introduce': {'path': 'introduce.html'}, 
                         'question': {'path': '<question_topic_number>'}
                         }
                    }
                }
            }
}