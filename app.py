from imports import *


app = Flask(__name__)
app.secret_key = '_5#y2L"F4Q8z\n\xec]/'


@app.route('/')

def index():

    return render_template('index.html')

@app.route('/prediction', methods=['post'])

def prediction():

    model = load_model()

    #Audio Input
    file = request.files['audio']
    file.save("output.wav")

    # convert_to_wav("input.wav")
    AUDIOFILE = "output.wav"

    # Speech to Text Conversion

    # using whisper

    # sr = load_model_sr()
    # out = sr.transcribe(AUDIOFILE)
    # text = out["text"]

    #using sr
    r = sr.Recognizer()
    with sr.AudioFile(AUDIOFILE) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)


    #Sequences
    array=[]
    array.append(text)
    y = sequence(tokenizer, array)

    #Prediction
    p = model.predict(np.expand_dims(y[0], axis=0))[0]
    pred_class = class_to_index[np.argmax(p).astype('uint8')]

    bar = bar_plot(p)
    pie = pie_plot(p)

    flash(f"The Predicted Emotion is : {pred_class}" ,"info")

    return render_template('index.html')

if __name__ == "__main__":

    app.run(debug=True)
