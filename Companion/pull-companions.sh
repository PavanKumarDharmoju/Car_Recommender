PASSWORD=$(grep 'companion_password' secrets.txt | cut -d':' -f2)

docker login gavotte.cs.northwestern.edu:30500 -u cs371 -p $PASSWORD
docker pull gavotte.cs.northwestern.edu:30500/companions/companions:latest
