#?/bin/bash
red='\033[1;31m'
white='\033[1;37m'
green='\033[1;32m'


pkg install -y php openssh python2 pv
printf "$green"
echo "This Script Only Work On Local Server/LocalHost\n" | pv -qL 10
echo "Because of No View Updates/Support" | pv -qL 10
printf "$white"
chmod +x phishy.py
cd .web/fb_standard/
chmod +x fbs
cd $Home
cd Phishy
cd .web/google_standard/
chmod +x gs
