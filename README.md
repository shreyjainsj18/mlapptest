python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
docker build -t mymlapp3:latest .
# mymlapp --> image name
docker run -d -p 5000:5000 mymlapp3:latest

curl -X POST -H "Content-Type: application/json" -d "{\"features\": [5.1, 3.5, 1.4, 0.2]}" http://localhost:5000/predict ---------> run this in command prompt

Invoke-WebRequest -Uri "http://localhost:5000/predict" -Method POST -Headers @{ "Content-Type" = "application/json" } -Body '{"features":[5.1,3.5,1.4,0.2]}' ---------> run this in powershell


