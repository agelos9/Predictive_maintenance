Example code used for the Predictive maintenace task of a Remote Terminal Unit (RTU).
The main modules of this task are:
  1) Data gathering (via Mqtt in a MongoDB) / simple Python scripts to subscribe to MQTT broker, store data in MongoDB and publish measurements
  2) Data preprocessing
  3) Time-series forecasting / using the Walk Forward Validation (WFV) method with different models (XGBoost, ARIMA, LSTM)
  4) Anomaly Detection on the forecasted data (Isolation Forest, DBSCAN, Autoencoder)
