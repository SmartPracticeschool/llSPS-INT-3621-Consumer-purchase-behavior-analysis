from flask import Flask , render_template,request
import pickle
model = pickle.load(open('purchase.pkl','rb'))
app = Flask(__name__)
global m2
@app.route('/') #when the browser is routed towrads url execute below function
def hello_world():
   return render_template("webapp.html")
@app.route('/login',methods=["POST"])

def func2():
    Product_ID = request.form['Product_ID']
    Gender = request.form['Gender']
    if(Gender=='MALE'):
        g2=1
    if(Gender=='FEMALE'):
        g2=0
    Age = request.form['Age']
    Occupation = request.form['Occupation']
    City_Category = request.form['City_Category']
    Stay_in_current_city_year = request.form['Stay_in_current_city_year']
    Marital = request.form['Marital']
    if(Marital=='Single'):
        m2=1
    if(Marital=='Married'):
        m2=0
    Product_category1 = request.form['Product_category1']
    Product_category2 = request.form['Product_category2']
    Product_category3 = request.form['Product_category3']
    data = [[int(Product_ID),g2,int(Age),int(Occupation),int(City_Category),float(Stay_in_current_city_year),m2,int(Product_category1),float(Product_category2),float(Product_category3)]]
    pred = model.predict(data)
    print(pred[0])
    
    return render_template("webapp.html", y = "customer purchase is : " + str(pred[0]))
if __name__ == '__main__':
   app.run(debug = True)






