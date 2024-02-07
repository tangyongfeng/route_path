from flask import Flask,render_template_string

import yaml

from route import Route 

app = Flask(__name__)
route = Route()

print (route.route_tree)

print (route.list_routes())
exit()
# 定义视图函数
@app.route(route.get_route_path('auth.login'))
def login():
    return "Login Page"

@app.route(route.get_route_path('auth.logout'))
def logout():
    return "Logout Page"

@app.route(route.get_route_path('auth.register'))
def register():
    return "Register Page"

@app.route(route.get_route_path('course.chapter.introduce'), methods=['GET', 'POST'])
def introduce(course_name_, chapter_name, introduce):
    return f"introduce page for {course_name_}, {chapter_name}, {introduce}"




# 创建课程相关的三级路由的视图函数
@app.route(route.get_route_path('course.chapter.question'))
def course_chapter_question(course_name, chapter_name, question_topic_number):
    return f"Course: {course_name}, Chapter: {chapter_name}, Question: {question_topic_number}"


@app.route('/show_endpoints')
def show_endpoints():
    output = []
    for rule in app.url_map.iter_rules():
        methods = ','.join(sorted(rule.methods))
        line = f"Endpoint: {rule.endpoint}; URL: {rule.rule}; Methods: {methods}"
        output.append(line)
    return '<br>'.join(output)

@app.route('/')
def home():
    return render_template_string('''
        <html>
            <head>
                <title>Home Page</title>
            </head>
            <body>
                <h1>Welcome to the Flask App</h1>
                <p>Click <a href="/show_endpoints">here</a> to see all endpoints.</p>
            </body>
        </html>
    ''')

# 运行 Flask 应用
if __name__ == "__main__":
    app.run(debug=True)
