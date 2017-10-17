from flask import Flask, request, render_template
app = Flask(__name__,static_url_path="/static")
import requests
import os

@app.route('/')
@app.route('/index')
def root():
	"""
	If someone goes to the root of your website (i.e. http://localhost:5000/), run this function. The string that this
	returns will be sent to the browser
	"""
	return render_template("index.html") # Render the template located in "templates/index.html"

@app.route('/about')
def about():
	return render_template("about_us.html")

@app.route('/contact', methods=['GET'])
def contact():
	return render_template("contact_us.html")

@app.route('/contact/hi', methods=['POST'])
def contact_post():
	email_name = request.form.get('inputName')
	email_subject = request.form.get('subject')
	email_message = request.form.get('message')
	api_base_url = "https://api.mailgun.net/v3/"

	auth = (os.environ["INFO253_MAILGUN_USER"], os.environ["INFO253_MAILGUN_PASSWORD"])
	data = {
		'from': email_name + " <" + os.environ["INFO253_MAILGUN_FROM_EMAIL"] + ">",
		'to': os.environ["INFO253_MAILGUN_TO_EMAIL"],
		'subject': email_subject,
		'text': email_message}

	print(data)
	print(auth)

	send_message =  requests.post(
		api_base_url + os.environ["INFO253_MAILGUN_DOMAIN"] + "/messages", 
		auth=auth,
		data=data)
	print(api_base_url + os.environ["INFO253_MAILGUN_DOMAIN"] + "/messages")
	if send_message.status_code == requests.codes.ok:
		add_to_body = "Hi" + email_name + "Your message has been sent!"
	else:
		add_to_body = "An error occurred. Your message was unable to send :("

	return render_template("contact_us.html", add_to_body=add_to_body)

@app.route('/blog/<post_name>')
def blog_posts(post_name):
	return render_template("raw_content/" + post_name + ".html")
  