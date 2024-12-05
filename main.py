import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel, Field

from ml.data import apply_label, process_data
from ml.model import load_model

# DO NOT MODIFY


class Data(BaseModel):
    age: int = Field(..., example=37)
    workclass: str = Field(..., example="Private")
    fnlgt: int = Field(..., example=178356)
    education: str = Field(..., example="HS-grad")
    education_num: int = Field(..., example=10, alias="education-num")
    marital_status: str = Field(
        ..., example="Married-civ-spouse", alias="marital-status"
    )
    occupation: str = Field(..., example="Prof-specialty")
    relationship: str = Field(..., example="Husband")
    race: str = Field(..., example="White")
    sex: str = Field(..., example="Male")
    capital_gain: int = Field(..., example=0, alias="capital-gain")
    capital_loss: int = Field(..., example=0, alias="capital-loss")
    hours_per_week: int = Field(..., example=40, alias="hours-per-week")
    native_country: str = Field(...,
                                example="United-States",
                                alias="native-country")


encoder_path = "model/encoder.pkl"
encoder = load_model(encoder_path)

model_path = "model/model.pkl"
model = load_model(model_path)

# create a RESTful API using FastAPI
app = FastAPI()


@app.get("/")
async def get_root():
    """ Say hello!"""
    return {"message": "Hello there!"}


@app.post("/data/")
async def post_inference(data: Data):
    # Turn the Pydantic model into a dict
    data_dict = data.dict()

    # Clean up the dict to turn it into a Pandas DataFrame
    data = {k.replace("_", "-"): [v] for k, v in data_dict.items()}
    print(f"Data received: {data}")  # Add this line to see the received data

    data = pd.DataFrame.from_dict(data)

    # Ensure the data contains the expected categorical and numerical features
    cat_features = [
        "workclass", "education", "marital-status", "occupation",
        "relationship", "race", "sex", "native-country"
    ]

    # Check for missing columns
    missing_cols = [col for col in cat_features if col not in data.columns]
    if missing_cols:
        print(f"Warning: Missing columns in input data: {missing_cols}")

    # Ensure data is passed correctly to the process_data function
    data_processed, _, _, _ = process_data(data,
                                           categorical_features=cat_features,
                                           training=False, encoder=encoder)

    # Run the model prediction
    _inference = model.predict(data_processed)

    # Return the result as a string label
    return {"result": apply_label(_inference)}
