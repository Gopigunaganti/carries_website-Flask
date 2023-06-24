from flask import Flask,render_template,jsonify 
app = Flask(__name__)


JOBS=[{
  'id':1,
  'position':'Data analyst',
  'location':'bangaluru,india',
  'salary':'15LPA'
  
},
      {
  'id':2,
  'position':'Data scientist',
  'location':'hyderbad,india',
  'salary':'65LPA'
  
},
    
      {
  'id':3,
  'position':'front-end engineer',
  'location':'remote',
  'salary':'17LPA'
  
},
    {
      
  'id':4,
  'position':'back-end devloper',
  'location':'noida,india',
  'salary':'10LPA'
  

    }
     ]



@app.route("/")
def hello_jovian():
  return render_template("home.html",jobs=JOBS,company_name="flipkart")
@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)