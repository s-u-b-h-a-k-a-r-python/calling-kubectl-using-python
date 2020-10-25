FROM subhakarkotta/python-kubectl-kustomize:3-1.19.3-3.8.2

ADD lib/ /lib
ADD ssh/ /root/.ssh

ADD run.py /run.py

CMD [ "python", "./run.py" ]
