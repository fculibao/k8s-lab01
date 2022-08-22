#/bin/bash
#Set the subject of the RBAC objects to the current namespace where the provisioner is being deployed
NS=$(kubectl config get-contexts|grep -e "^\*" |awk '{print $5}')
NAMESPACE=${NS:-default}
sed -i'' "s/namespace:.*/namespace: $NAMESPACE/g" rbac.yaml deployment.yaml
kubectl create -f rbac.yaml