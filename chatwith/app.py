from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    influencers = [
        {'name': 'Influencer 1', 'image_url': 'path_to_image1.jpg', 'followers': '20'},
        {'name': 'Influencer 2', 'image_url': 'path_to_image2.jpg', 'followers': '15'},
        # Add more influencers as needed
    ]
    return render_template('index.html', influencers=influencers)


if __name__ == '__main__':
    app.run(debug=True)
