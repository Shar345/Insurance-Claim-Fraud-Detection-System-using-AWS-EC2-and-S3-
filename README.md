# Insurance-Claim-Fraud-Detection-System-using-AWS-EC2-and-S3-

STEPS OF AWS PROJECT

--> launch Instance
--> use Ubuntu
--> 22.04LTS
--> use keypair fraud already generated
--> in security groups create
SSH keep it as it is
Custom TCP  TCP  5000  Anywhereipv4 0.0.0.0/0
HTTP Anywhereipv4

###Store in S3
1]Go to AWS Console
2]Open S3
3]Click Create Bucket
4]Give name like: "insurance-fraud-predictions"

5]Keep region same as EC2
Leave default settings → Create
then go to IAM

###Attach IAM Role to EC2
1]Go to IAM → Create Role
2]Select:
Trusted entity → EC2

3]Attach policy:
AmazonS3FullAccess (for project/demo)

4]Create role
5]Go to EC2 → Instance → Actions → Security → Modify IAM Role
Attach the created role

6]Now EC2 can upload to S3 without access keys.


##Commands
sudo apt update && sudo apt upgrade -y (press tab then ok)

sudo apt install python3 python3-pip python3-venv -y (press tab then ok)

python3 --version (to verify)

pip3 --version (to verify)

##create the project folder
mkdir mycloudproject

cd mycloudproject

nano model.py (paste model.py code inside it then ctrl O + enter to save then ctrl X to exit and return the terminal)
python3 model.py (run this to create a pickle file and pip install pandas and scikit-learn)

nano app.py (paste app2.py code inside it then ctrl O + enter to save then ctrl X to exit and return the terminal)

nano insurance.csv (paste your data here then ctrl O + enter to save then ctrl X to exit and return the terminal)

mkdir templates

nano templates/index.html (paste your html code here then ctrl O + enter to save then ctrl X to exit and return the terminal)

ls (to see all files)

##Activate virtual environment
python3 -m venv venv

source venv/bin/activate

pip install flask pandas numpy scikit-learn boto3

python app.py (run the flask app)

##open another page <your_public_ip>:5000 then the page will open


##after that stop the instance then when you restart paste the code (Instance state = Running, Status checks = 2/2 passed)
cd mycloudproject

ls

source venv/bin/activate

python app.py (run the flask code)

