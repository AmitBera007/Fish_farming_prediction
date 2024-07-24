from flask import Flask, render_template, request, jsonify, url_for
import pickle


app = Flask(__name__)


prediction_model = pickle.load(open('prediction.pkl','rb'))


@app.route('/', methods=['GET', 'POST'])
def interactive_form():
    if request.method == 'POST':

        input_ph = float(request.form['ph'])
        input_temparature = float(request.form['temparature'])
        input_turbidity = float(request.form['turbidity'])

        
        
        fish_dataset = ['Carpio', 'Katla', 'Koi', 'Magur', 'Pangas', 'Prawn', 'Rui', 'Shrimp', 'SilverCup', 'Sing', 'Tilapia']

        predicted_fish_index = prediction_model.predict([[input_ph, input_temparature, input_turbidity]])
    
        
        return jsonify({
            'message': fish_dataset[predicted_fish_index[0]]
        })
    else:
        print("I am on the way...")

    return render_template('index.html')

    
if __name__ == '__main__':
    app.run(debug=True)

