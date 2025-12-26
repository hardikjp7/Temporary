Below is a clean, step-by-step hands-on guide to complete your Minikube + iris-classifier-site deployment, including verification and common fixes.
You can copy-paste commands exactly as shown.


---

0️⃣ Prerequisites (Ubuntu)

You already have these steps — keep them as-is:

sudo apt update
sudo apt install docker.io -y
sudo systemctl unmask docker
sudo systemctl enable docker
sudo service docker restart

(Optional but recommended)

sudo usermod -aG docker $USER
newgrp docker


---

1️⃣ Install Minikube

curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb
rm -rf minikube_latest_amd64.deb

Verify:

minikube version


---

2️⃣ Start Minikube Cluster

minikube start --driver=docker

Verify cluster:

kubectl get nodes

You should see STATUS = Ready


---

3️⃣ Create Deployment YAML

Create the deployment file:

cat <<EOF > iris-classifier-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: iris-classifier-site
  labels:
    app: web
spec:
  replicas: 1
  selector:
    matchLabels:
      app: iris-classifier
  template:
    metadata:
      labels:
        app: iris-classifier
    spec:
      containers:
        - name: mlexample
          image: gpcplay/playimages:mlexample
          ports:
            - containerPort: 5000
EOF

Apply deployment:

kubectl apply -f iris-classifier-deployment.yaml

Wait for pod creation:

kubectl get pods -w

✅ Pod should reach Running state


---

4️⃣ Create Service YAML (NodePort)

Create the service file:

cat <<EOF > iris-classifier-service.yaml
apiVersion: v1
kind: Service
metadata:
  name: iris-classifier-svc
spec:
  selector:
    app: iris-classifier
  type: NodePort
  ports:
    - port: 5000
      targetPort: 5000
      nodePort: 30800
EOF

Apply service:

kubectl apply -f iris-classifier-service.yaml

Verify service:

kubectl get services

You should see:

iris-classifier-svc   NodePort   ...   5000:30800/TCP


---

5️⃣ Verify Pods and Services

kubectl get pods
kubectl get services

(Optional) Check pod logs:

kubectl logs $(kubectl get pod -l app=iris-classifier -o jsonpath='{.items[0].metadata.name}')


---

6️⃣ Set NODE_PORT Environment Variable

export NODE_PORT=$(kubectl get services/iris-classifier-svc \
-o go-template='{{(index .spec.ports 0).nodePort}}')

echo NODE_PORT=$NODE_PORT


---

7️⃣ Access the Application

Get Minikube IP:

minikube ip

Test application using curl:

curl "http://$(minikube ip):$NODE_PORT/classify/?sl=5.1&sw=3.5&pl=1.4&pw=0.3"

✅ Expected output: JSON response with iris flower classification


---

🔍 Common Issues & Fixes

❌ Pod stuck in ImagePullBackOff

kubectl describe pod <pod-name>

➡ Ensure Docker is running and internet access is available.


---

❌ Cannot access service

Use Minikube helper:

minikube service iris-classifier-svc --url


---

❌ Port 30800 not accessible

Minikube runs in a VM. Always use:

http://$(minikube ip):30800


---

✅ Final Checklist

✔ Minikube running
✔ Pod status = Running
✔ Service type = NodePort
✔ Curl returns classification result


---

If you want, I can also:

Convert this into one script

Explain how the ML model works

Show how to expose using Ingress


Just tell me 👍
