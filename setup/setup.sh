echo  
echo "-------------------- Setting up environment for ProductGuideBackend --------------------"
echo 

echo 
echo "-------------------- Updating existing packages --------------------"
echo 
sudo apt-get update
echo 

echo 
echo "-------------------- Upgrading existing packages --------------------"
echo 
sudo apt-get upgrade
echo 

echo 
echo "-------------------- Installing python3 pip3 and Git --------------------"
echo 
sudo apt-get install python3 python3-pip git
echo 

echo 
echo "-------------------- Installing packages from PIP --------------------"
echo 
pip3 install pillow scikit-build cmake pandas xlrd flask easyocr
echo 
