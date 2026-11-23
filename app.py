from email.policy import default

from flask import Flask,render_template,request

from PIL import Image, ImageDraw, ImageFont
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_meme():
    if request.method == "GET":
        return render_template("index.html")

    slika = request.files["slika"]
    zgornji_text = request.form["zgornji_text"]
    spodnji_text = request.form["spodnji_text"]

    with Image.open(slika.stream) as im:
        draw = ImageDraw.Draw(im)

    font = ImageFont.load_default(size=50)

    draw.text((im.width / 2, 10), zgornji_text, fill="white", stroke_fill="black",
            stroke_width=2, anchor="mt", font=font) # mt - (x, y) je sredina zgornjega roba besedila
    draw.text((im.width / 2, im.height - 10), spodnji_text, fill="white",
            stroke_fill="black", stroke_width=2, anchor="mb", font=font) # (x, y) je sredina spodnjega roba

    im.save("static/meme.png")
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=False, port=5001, host="0.0.0.0")
