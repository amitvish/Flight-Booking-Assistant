to run :
python chatgpt.py

then it will ask for "Please describe your Travel Plans"

you can ask for: give me flight from departure to arrival on departure dat

it will give you list of all the flights available

you can then ask it to fetch the bbest flight according to your neeeds

If you are satisfied, Smile! If not, feel free to ask again.

pip3.10 install langchain==0.1.5 openai==1.2.3 zeep==4.2.1 requests==2.31.0 beautifulsoup4==4.12.3 chromadb==0.4.22 pysqlite3-binary
 
python version 3.10.12
 
used openai api, langchain
 
to xml parsing used element tree
 
 
wget https://www.python.org/ftp/python/3.10.12/Python-3.10.12.tar.xz
sudo chmod +777 Python-3.10.12.tar.xz 
unzip Python-3.10.12.tar.xz
./configure --enable-loadable-sqlite-extensions --enable-optimizations
 
make -j 2 nproc
make altinstall
sudo make altinstall
 
 
run command using python3.10 chatgpt.py