from flask import Flask,render_template
app = Flask(__name__)
import requests
blog_url ="https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(blog_url).json()


@app.route('/')
def home():
    return render_template("index.html",all_posts = posts)


@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post=blog_post
    return render_template("post.html",post=requested_post)



if __name__=="__main__":
    app.run(debug=True)