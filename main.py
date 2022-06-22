from flask import Flask,render_template,request
import requests
from smtplib import SMTP
MY_EMAIL ="munasinghehiruka@gmail.com"
PASSWORD ="Hirukasoftwareengineer"
app = Flask(__name__)

blog_url ="https://api.npoint.io/c790b4d5cab58020d391"
posts = requests.get(blog_url).json()


@app.route('/')
def home():
    return render_template("index.html",all_posts = posts)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post=blog_post
    return render_template("post.html",post=requested_post)



@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/contact",methods=["GET","POST"])
def receive_data():
    if request.method=="POST":
        data = request.form
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html",msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_mail(name,email,phone,message):
    email_message =f"Subject: New Message\n\nName: {name}\nEmail: {email} \nPhone: {phone} \nMessage: {message}"
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,PASSWORD)
        connection.sendmail(MY_EMAIL,MY_EMAIL,email_message)



if __name__=="__main__":
    app.run(debug=True)

