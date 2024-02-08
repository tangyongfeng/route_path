from flask import Flask,render_template_string,url_for

import yaml

from route import Route 

app = Flask(__name__)
route = Route('test_routes.yaml')

print (route.list_routes())


# 定义视图函数
@app.route('/<test_a>/<test_b>/detail_<number>.html')
def test(test_a,test_b,number):
    return f"{test_a} {test_b} {number}"

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
def introduce(course_name, chapter_name):
    return f"introduce page for {course_name}, {chapter_name}"




# 创建课程相关的三级路由的视图函数
@app.route(route.get_route_path('course.chapter.question'))
def course_chapter_question(course_name, chapter_name, question_topic_number):
    return f"Course: {course_name}, Chapter: {chapter_name}, Question: {question_topic_number}"


@app.route('/show_endpoints')
def show_endpoints():
    output = ["<h1>Available Routes:</h1>"]
    with app.test_request_context():  # 创建一个测试请求上下文
        for rule in app.url_map.iter_rules():
            # 跳过静态文件路由和show_endpoints自身，以避免无限循环
            if rule.endpoint != 'static' and rule.endpoint != 'show_endpoints':
                try:
                    # 尝试为每个路由生成URL
                    url = url_for(rule.endpoint, **(rule.defaults or {}))
                    output.append(f"<li>{rule.endpoint}: <a href='{url}'>{url}</a></li>")
                except Exception as e:
                    output.append(f"<li>{rule.endpoint}: Could not generate URL. ({e})</li>")

    return "<ul>" + "".join(output) + "</ul>"

@app.route(route.get_route_path('root'))
def home():
    return render_template_string('''
        <html>
            <head>
                <title>Home Page</title>
            </head>
            <body>
                <h1>Welcome to the Flask App</h1>
                <p>Click <a href="/show_endpoints">here</a> to see all endpoints.</p>
                <p><a href="{{url_for('test',test_a='cc', test_b='dd',number=12)}}">tt</a></p>
            </body>
        </html>
    ''')

# 运行 Flask 应用
if __name__ == "__main__":
    app.run(debug=True)
