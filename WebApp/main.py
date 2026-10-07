from flask import Flask, render_template, request
import pickle as pkl
import numpy as np


# =====================================================
# FLASK APP
# =====================================================

app = Flask(__name__)


# =====================================================
# LOAD MODELS
# =====================================================

with open("../models/LogisticRegressionModel.pkl", "rb") as f:
    lr_model = pkl.load(f)

with open("../models/RandomForestModel.pkl", "rb") as f:
    rf_model = pkl.load(f)

with open("../models/NaiveBayesModel.pkl", "rb") as f:
    nb_model = pkl.load(f)

with open("../models/scaler.pkl", "rb") as f:
    scaler = pkl.load(f)


# =====================================================
# HOME PAGE
# =====================================================

@app.route('/')
def home():

    return render_template("index.html")


# =====================================================
# GET INPUT DATA
# =====================================================

def getData():

    # ==========================================
    # USER INPUTS — EXACT TRAINING FEATURE ORDER
    # ==========================================

    age = float(request.form.get("age", 0))

    gender = float(request.form.get("gender", 0))

    weight = float(request.form.get("weight", 0))

    smokeage = float(request.form.get("smokeage", 0))

    smokeday = float(request.form.get("smokeday", 0))

    smokeyr = float(request.form.get("smokeyr", 0))

    pkyr = float(request.form.get("pkyr", 0))

    age_quit = float(request.form.get("age_quit", 0))

    cigsmok = float(request.form.get("cigsmok", 0))

    pipe = float(request.form.get("pipe", 0))

    cigar = float(request.form.get("cigar", 0))

    smokelive = float(request.form.get("smokelive", 0))

    smokework = float(request.form.get("smokework", 0))

    yrsfire = float(request.form.get("yrsfire", 0))

    anyscr_has_nodule = float(
        request.form.get("anyscr_has_nodule", 0)
    )

    lesionsize = float(request.form.get("lesionsize", 0))

    agecopd = float(request.form.get("agecopd", 0))

    agebron = float(request.form.get("agebron", 0))

    fammother = float(request.form.get("fammother", 0))

    famsister = float(request.form.get("famsister", 0))


    # ==========================================
    # EXACT SAME FEATURE ORDER USED FOR TRAINING
    # ==========================================

    X_pred = [[

        age,
        gender,
        weight,
        smokeage,
        smokeday,
        smokeyr,
        pkyr,
        age_quit,
        cigsmok,
        pipe,
        cigar,
        smokelive,
        smokework,
        yrsfire,
        anyscr_has_nodule,
        lesionsize,
        agecopd,
        agebron,
        fammother,
        famsister

    ]]

    return np.array(X_pred)


# =====================================================
# PREDICTION ROUTE
# =====================================================

@app.route('/predict', methods=['POST'])
def predict():

    try:

        # ==========================================
        # GET INPUT DATA
        # ==========================================

        data = getData()


        # ==========================================
        # SCALE DATA
        # ==========================================

        data_scaled = scaler.transform(data)


        # ==========================================
        # MODEL PREDICTIONS
        # ==========================================

        lr_prob = lr_model.predict_proba(data_scaled)[0][1] * 100

        rf_prob = rf_model.predict_proba(data_scaled)[0][1] * 100

        nb_prob = nb_model.predict_proba(data_scaled)[0][1] * 100


        # ==========================================
        # FINAL RISK
        # ==========================================

        final_risk = (

            lr_prob * 0.4 +

            rf_prob * 0.6
        )


        # ==========================================
        # FINAL RESULT
        # ==========================================

        if final_risk >= 50:

            final_result = "HIGH RISK OF LUNG CANCER 😔"

        elif final_risk >= 35 and final_risk < 50:

            final_result = "MEDIUM RISK OF LUNG CANCER 😔"

        else:

            final_result = "LOW RISK OF LUNG CANCER 🙂"


        # ==========================================
        # SEND TO HTML
        # ==========================================

        return render_template(

            "predict.html",

            lr_result=round(lr_prob, 2),

            rf_result=round(rf_prob, 2),

            nb_result=round(nb_prob, 2),

            avg_result=round(final_risk, 2),

            final_result=final_result
        )

    except Exception as e:

        return f"ERROR : {str(e)}"


# =====================================================
# RUN APP
# =====================================================

if __name__ == "__main__":

    app.run(

        debug=True,

        host="0.0.0.0",

        port=5000
    )