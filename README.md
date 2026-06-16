# Insurance Claim Fraud Detection System using AWS EC2 and S3

STEPS OF AWS PROJECT<br>

--> launch Instance<br>
--> use Ubuntu<br>
--> 22.04LTS<br>
--> use keypair fraud already generated<br>
--> in security groups create<br>
SSH keep it as it is<br>
Custom TCP  TCP  5000  Anywhereipv4 0.0.0.0/0<br>
HTTP Anywhereipv4<br>

###Store in S3<br>
1]Go to AWS Console<br>
2]Open S3<br>
3]Click Create Bucket<br>
4]Give name like: "insurance-fraud-predictions"<br>

5]Keep region same as EC2<br>
Leave default settings → Create<br>
then go to IAM<br>

###Attach IAM Role to EC2<br>
1]Go to IAM → Create Role<br>
2]Select:<br>
Trusted entity → EC2<br>

3]Attach policy:<br>
AmazonS3FullAccess (for project/demo)<br>

4]Create role<br>
5]Go to EC2 → Instance → Actions → Security → Modify IAM Role<br>
Attach the created role<br>

6]Now EC2 can upload to S3 without access keys.<br>


##Commands<br>
sudo apt update && sudo apt upgrade -y (press tab then ok)<br>

sudo apt install python3 python3-pip python3-venv -y (press tab then ok)<br>

python3 --version (to verify)<br>

pip3 --version (to verify)<br>

##create the project folder<br>
mkdir mycloudproject<br>

cd mycloudproject<br>

nano model.py (paste model.py code inside it then ctrl O + enter to save then ctrl X to exit and return the terminal)<br>
python3 model.py (run this to create a pickle file and pip install pandas and scikit-learn)<br>

nano app.py (paste app2.py code inside it then ctrl O + enter to save then ctrl X to exit and return the terminal)<br>

nano insurance.csv (paste your data here then ctrl O + enter to save then ctrl X to exit and return the terminal)<br>

mkdir templates<br>

nano templates/index.html (paste your html code here then ctrl O + enter to save then ctrl X to exit and return the terminal)<br>

ls (to see all files)<br>

##Activate virtual environment<br>
python3 -m venv venv<br>

source venv/bin/activate<br>

pip install flask pandas numpy scikit-learn boto3<br>

python app.py (run the flask app)<br>

##open another page <your_public_ip>:5000 then the page will open<br>


##after that stop the instance then when you restart paste the code (Instance state = Running, Status checks = 2/2 passed)
cd mycloudproject<br>

ls<br>

source venv/bin/activate<br>

python app.py (run the flask code)<br>

