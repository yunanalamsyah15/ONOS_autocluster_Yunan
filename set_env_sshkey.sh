#! /bin/bash
echo "Creating RSA SSH-key pair, if already exist you may press n"
ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -P ""
USER=$(whoami)
SSH_KEY=$(cut -d\  -f2 ~/.ssh/id_rsa.pub)

echo "Inserting RSA pubkey to all controllers..."
for i in {1..2}; do
	docker exec -it onos$i bin/onos-user-key $USER $SSH_KEY
done

docker cp onos1:root/onos/bin ~/onos 
cat >> ~/.bash_profile <<EOL
source ~/ONOS_autocluster/onos_env.sh
EOL
